from typing import List

from pkilint import validation, etsi
from pkilint.etsi import (
    etsi_constants,
)
from pkilint.pkioverheid import pkioverheid_constants
from pkilint.pkioverheid.por import (
    NaturalPersonSubjectAttributeAllowanceValidator,
    ValidityValidator,
    AllowedSignatureAlgorithmEncodingValidator,
    NaturalPersonSubjectNameValidator,
    NonRepudiationKeyUsageValidator,
    CertificatePoliciesValidator,
    PolicyQualifierPresenceValidator,
    ExtendedKeyUsageValidator,
    QcStatementIdentifierAllowanceValidator,
)

ETSI_MAPPING = {
    pkioverheid_constants.CertificateType.EUTL_G4_NATURAL_PERSONS_INDIVIDUAL_VALIDATED_ESIG: etsi_constants.CertificateType.QCP_N_QSCD_FINAL_CERTIFICATE
}


def create_validators(
    type: pkioverheid_constants.CertificateType,
) -> List[validation.Validator]:
    subject_validators = []
    validity_validators = []
    top_level_validators = []
    extension_validators = []
    if (
        type
        == pkioverheid_constants.CertificateType.EUTL_G4_NATURAL_PERSONS_INDIVIDUAL_VALIDATED_ESIG
    ):
        subject_validators.extend(
            [
                NaturalPersonSubjectAttributeAllowanceValidator(),
                NaturalPersonSubjectNameValidator(),
            ]
        )
        validity_validators.append(ValidityValidator())
        top_level_validators.extend(
            [
                NonRepudiationKeyUsageValidator(),
                AllowedSignatureAlgorithmEncodingValidator(),
            ]
        )
        extension_validators.extend(
            [
                CertificatePoliciesValidator(type),
                PolicyQualifierPresenceValidator(),
                ExtendedKeyUsageValidator(type),
                QcStatementIdentifierAllowanceValidator(type),
            ]
        )

    return etsi.create_validators(
        ETSI_MAPPING[type],
        additional_validity_validators=validity_validators,
        additional_name_validators=subject_validators,
        additional_top_level_validators=top_level_validators,
        additional_extension_validators=extension_validators,
    )


def create_decoding_validators(type):
    return etsi.create_decoding_validators(ETSI_MAPPING[type])
