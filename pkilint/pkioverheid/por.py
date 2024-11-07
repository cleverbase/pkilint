import binascii
import operator
from datetime import timedelta
from urllib.parse import urlparse

from pyasn1_alt_modules import rfc5280, rfc3739, rfc9336

from pkilint import validation, oid, common
from pkilint.document import PDUNode
from pkilint.etsi import etsi_shared
from pkilint.etsi.asn1 import en_319_411_2, en_319_411_1, en_319_412_5
from pkilint.pkioverheid import pkioverheid_constants
from pkilint.pkioverheid.asn1 import pkioverheid_por, win_crypto
from pkilint.pkix import name, Rfc2119Word, time, algorithm


class NaturalPersonSubjectAttributeAllowanceValidator(validation.Validator):
    """
    POR: 3.1.3: Pseudonyms SHALL NOT be used in certificates
    """

    VALIDATION_NATURAL_PERSON_PSEUDONYM_USED = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.3.1.3.pseudonym_used",
    )

    _PROHIBITED_ATTRIBUTES = {
        rfc5280.id_at_pseudonym,
    }

    def __init__(self):
        super().__init__(
            validations=[self.VALIDATION_NATURAL_PERSON_PSEUDONYM_USED],
            pdu_class=rfc5280.Name,
        )

    def validate(self, node):
        attr_counts = name.get_name_attribute_counts(node)

        attrs_present = set(attr_counts.keys())

        used_prohibited_attributes = attrs_present.intersection(
            self._PROHIBITED_ATTRIBUTES
        )
        if used_prohibited_attributes:
            formatted = [str(a) for a in used_prohibited_attributes]
            raise validation.ValidationFindingEncountered(
                self.VALIDATION_NATURAL_PERSON_PSEUDONYM_USED,
                f"Prohibited attributes used: {formatted}",
            )


class ValidityValidator(time.ValidityPeriodThresholdsValidator):
    VALIDATION_VALIDITY_PERIOD_EXCEEDS_1185_DAYS = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.6.3.2.1.valid_longer_than_1185_days",
    )

    _THRESHOLDS = [
        (
            operator.le,
            timedelta(days=1185),
            VALIDATION_VALIDITY_PERIOD_EXCEEDS_1185_DAYS,
        ),
    ]

    def __init__(self):
        super().__init__(
            end_validity_node_retriever=lambda n: n.navigate("^.notAfter"),
            inclusive_second=True,
            validity_period_thresholds=self._THRESHOLDS,
            path="certificate.tbsCertificate.validity.notBefore",
        )


class AllowedSignatureAlgorithmEncodingValidator(
    algorithm.AllowedSignatureAlgorithmEncodingValidator
):

    VALIDATION_DISALLOWED_SIGNATURE_ENCODING = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.2.3.3.invalid_signature_algorithm",
    )

    ALLOWED_SIGNATURE_ALGORITHM_ENCODINGS = set(
        map(
            binascii.a2b_hex,
            [
                # RSASSA‐PKCS1‐v1_5 with SHA‐256
                "300d06092a864886f70d01010b0500",
                # RSASSA‐PKCS1‐v1_5 with SHA‐384
                "300d06092a864886f70d01010c0500",
                # ECDSA with SHA‐256
                "300a06082a8648ce3d040302",
                # ECDSA with SHA‐384
                "300a06082a8648ce3d040303",
            ],
        )
    )

    def __init__(self):
        super().__init__(
            validation=self.VALIDATION_DISALLOWED_SIGNATURE_ENCODING,
            allowed_encodings=self.ALLOWED_SIGNATURE_ALGORITHM_ENCODINGS,
            path="certificate.tbsCertificate.signature",
        )


class NaturalPersonSubjectNameValidator(validation.Validator):
    VALIDATION_PROHIBITED_COMMON_NAME = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.4.2.2.1.subject_common_name_neq_surname_givenname",
    )
    VALIDATION_MISSING_ATTRIBUTE = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.4.2.2.2.subject_missing_attribute",
    )
    VALIDATION_NULL_ATTRIBUTE = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.4.2.2.2.subject_attribute_null_value",
    )
    VALIDATION_SUBJECT_SERIAL_20_CHAR = validation.ValidationFinding(
        validation.ValidationFindingSeverity.WARNING,
        "pkioverheid.por.7.1.4.2.2.3.subject_serialname_20_chars",
    )

    def __init__(self):
        super().__init__(
            validations=[
                self.VALIDATION_PROHIBITED_COMMON_NAME,
                self.VALIDATION_MISSING_ATTRIBUTE,
                self.VALIDATION_NULL_ATTRIBUTE,
                self.VALIDATION_SUBJECT_SERIAL_20_CHAR,
            ],
            pdu_class=rfc5280.Name,
        )

    def validate(self, node):
        findings = []

        def str_value_for(oid, value_path):
            values = name.get_name_attributes_by_type(node, oid)
            if not values:
                findings.append(
                    validation.ValidationFindingDescription(
                        self.VALIDATION_MISSING_ATTRIBUTE, f"Missing a value for {oid}"
                    )
                )

            str_value = str(values[0][0].navigate(value_path).pdu)
            if not str_value:
                findings.append(
                    validation.ValidationFindingDescription(
                        self.VALIDATION_NULL_ATTRIBUTE, f"Empty value for {oid}"
                    )
                )
            return str_value

        given_name = str_value_for(rfc5280.id_at_givenName, "value.x520name.utf8String")
        surname = str_value_for(rfc5280.id_at_surname, "value.x520name.utf8String")
        common_name = str_value_for(
            rfc5280.id_at_commonName, "value.x520CommonName.utf8String"
        )

        if f"{given_name} {surname}" != common_name:
            findings.append(
                validation.ValidationFindingDescription(
                    self.VALIDATION_PROHIBITED_COMMON_NAME, None
                )
            )

        serial_number = str_value_for(
            rfc5280.id_at_serialNumber, "value.x520SerialNumber"
        )

        if len(serial_number) == 20:
            findings.append(
                validation.ValidationFindingDescription(
                    self.VALIDATION_SUBJECT_SERIAL_20_CHAR, None
                )
            )

        return validation.ValidationResult(self, node, findings)


class NonRepudiationKeyUsageValidator(etsi_shared.KeyUsageValidator):
    VALIDATION_INVALID_KEYUSAGE = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.2.3.9.keyusage_not_non_repudiation",
    )

    def __init__(self):
        super().__init__(
            True,
            self.VALIDATION_INVALID_KEYUSAGE,
            self.VALIDATION_INVALID_KEYUSAGE,
        )
        self._CONTENT_COMMITMENT_SETTINGS = {self.KeyUsageSetting.A}


class CertificatePoliciesValidator(validation.Validator):

    VALIDATION_REQUIRED_POLICY_MISSING = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.6.4.missing_required_policy_oid",
    )

    _CERTIFICATE_TYPE_SET_TO_POLICY_OID_MAPPINGS = {
        pkioverheid_constants.CertificateType.EUTL_G4_NATURAL_PERSONS_INDIVIDUAL_VALIDATED_ESIG: {
            pkioverheid_por.id_EUTL_G4_Natural_Persons_Individual_Validated_eSig,
            en_319_411_2.id_qcp_natural_qscd,
            en_319_411_1.id_ncp_plus,
        },
    }

    def __init__(self, certificate_type):
        super().__init__(
            validations=[
                self.VALIDATION_REQUIRED_POLICY_MISSING,
            ],
            pdu_class=rfc5280.CertificatePolicies,
        )
        self._certificate_type = certificate_type

    def validate(self, node):
        policies = set(node.document.policy_oids)
        required_policies = self._CERTIFICATE_TYPE_SET_TO_POLICY_OID_MAPPINGS[
            self._certificate_type
        ]

        missing_policies = required_policies - policies

        if missing_policies:
            oids = oid.format_oids(missing_policies)

            raise validation.ValidationFindingEncountered(
                self.VALIDATION_REQUIRED_POLICY_MISSING,
                f"Policy OIDs missing: {oids}",
            )


class PolicyQualifierPresenceValidator(validation.Validator):
    VALIDATION_POLICY_QUALIFIER_MISSING = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.6.4.missing_required_policy_qualifier",
    )
    VALIDATION_MISSING_HTTPS_CPS_URI = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.6.4.missing_https_cps_uri",
    )

    REQUIRED_POLICY_QUALIFIER = pkioverheid_por.PKIO_OIDS

    def match(self, node: PDUNode) -> bool:
        if super().match(node):
            policy_identifier = node.children["policyIdentifier"]
            if not policy_identifier:
                return False
            return policy_identifier.pdu in self.REQUIRED_POLICY_QUALIFIER

        return False

    def __init__(self):
        super().__init__(
            validations=[
                self.VALIDATION_POLICY_QUALIFIER_MISSING,
                self.VALIDATION_MISSING_HTTPS_CPS_URI,
            ],
            pdu_class=rfc5280.PolicyInformation,
        )

    def validate(self, node: PDUNode):
        qualifiers = node.children.get("policyQualifiers")
        if not qualifiers:
            raise validation.ValidationFindingEncountered(
                self.VALIDATION_POLICY_QUALIFIER_MISSING,
                "No policyQualifiers specified",
            )

        qualifiers_by_id = dict(
            [
                [policy_qualifier.children["policyQualifierId"].pdu, policy_qualifier]
                for policy_qualifier in qualifiers.children.values()
            ]
        )

        if rfc5280.id_qt_cps not in qualifiers_by_id:
            raise validation.ValidationFindingEncountered(
                self.VALIDATION_POLICY_QUALIFIER_MISSING,
                f"Cannot find {rfc5280.id_qt_cps}",
            )

        cps_uri_node = qualifiers_by_id[rfc5280.id_qt_cps].navigate("qualifier.cPSuri")
        if not cps_uri_node:
            raise validation.ValidationFindingEncountered(
                self.VALIDATION_POLICY_QUALIFIER_MISSING,
                f"Cannot find cPSuri",
            )

        parsed_url = urlparse(str(cps_uri_node.pdu))

        if parsed_url.scheme.lower() != "https":
            raise validation.ValidationFindingEncountered(
                self.VALIDATION_MISSING_HTTPS_CPS_URI,
                f"Non-HTTPS URL scheme found: {parsed_url.scheme}",
            )

        return None


class ExtendedKeyUsageValidator(validation.Validator):
    VALIDATION_MISSING_EXT_KEYUSAGE = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.2.3.15.missing_ext_key_usage",
    )
    VALIDATION_INVALID_KEYPURPOSE = validation.ValidationFinding(
        validation.ValidationFindingSeverity.ERROR,
        "pkioverheid.por.7.1.2.3.15.invalid_key_purpose",
    )

    _REQUIRED_KEYPURPOSES = {
        pkioverheid_constants.CertificateType.EUTL_G4_NATURAL_PERSONS_INDIVIDUAL_VALIDATED_ESIG: {
            rfc9336.id_kp_documentSigning,
            win_crypto.szOID_KP_DOCUMENT_SIGNING,
        }
    }

    def __init__(self, certificate_type):
        self._certificate_type = certificate_type
        super().__init__(
            validations=[
                self.VALIDATION_INVALID_KEYPURPOSE,
                self.VALIDATION_MISSING_EXT_KEYUSAGE,
            ],
            pdu_class=rfc5280.CertificatePolicies,
        )

    def validate(self, node: PDUNode):
        ext_key_usage_pack = node.document.get_extension_by_oid(
            rfc5280.id_ce_extKeyUsage
        )
        if not ext_key_usage_pack:
            raise validation.ValidationFindingEncountered(
                self.VALIDATION_MISSING_EXT_KEYUSAGE, None
            )

        key_usages = ext_key_usage_pack[0].navigate("extnValue.extKeyUsageSyntax")
        key_usage_oids = {k.pdu for k in key_usages.children.values()}

        findings = []

        unneeded_oids = (
            key_usage_oids - self._REQUIRED_KEYPURPOSES[self._certificate_type]
        )
        if unneeded_oids != set():
            findings.append(
                validation.ValidationFindingDescription(
                    self.VALIDATION_INVALID_KEYPURPOSE,
                    f"Ext Key Usage lists unallowed key purposes: {oid.format_oids(unneeded_oids)}",
                )
            )
        missing_oids = (
            self._REQUIRED_KEYPURPOSES[self._certificate_type] - key_usage_oids
        )
        if missing_oids != set():
            findings.append(
                validation.ValidationFindingDescription(
                    self.VALIDATION_INVALID_KEYPURPOSE,
                    f"Ext Key Usage is missing key purposes: {oid.format_oids(missing_oids)}",
                )
            )

        return validation.ValidationResult(self, node, findings)


class QcStatementIdentifierAllowanceValidator(
    common.ElementIdentifierAllowanceValidator
):
    _CODE_CLASSIFIER = "pkioverheid.por.7.1.2.3.17.qc_statements"

    # qualified statements
    _OID_TO_CODE_NAME = {
        en_319_412_5.id_etsi_qcs_QcPDS: "qc_pds",
    }

    def __init__(self, certificate_type: pkioverheid_constants.CertificateType):
        allowances = {}

        if (
            certificate_type
            == pkioverheid_constants.CertificateType.EUTL_G4_NATURAL_PERSONS_INDIVIDUAL_VALIDATED_ESIG
        ):
            allowances[en_319_412_5.id_etsi_qcs_QcPDS] = Rfc2119Word.MUST

        super().__init__(
            "qualified statement",
            lambda node: node.children["statementId"],
            allowances,
            None,
            f"{self._CODE_CLASSIFIER}.{{oid}}_qualified_statement_absent",
            None,
            pdu_class=rfc3739.QCStatements,
        )
