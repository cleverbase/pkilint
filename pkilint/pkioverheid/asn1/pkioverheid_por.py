from pyasn1.type import univ

# SOURCE: https://cp.pkioverheid.nl/pkioverheid-por-v5.0.html

_ARC = univ.ObjectIdentifier("2.16.528.1.1003.1")

_CP = _ARC + (2,)

_G3_BURGER = _CP + (3,)

_G3_ORG = _CP + (5,)

_G3_AD = _CP + (6,)

_G1_PRIVATE = _CP + (8,)

_G4 = _CP + (44,)

_G4_SMIME = _G4 + (12,)
_G4_SMIME_NP_IND = _G4_SMIME + (11,)
_G4_SMIME_NP_SPON = _G4_SMIME + (13,)
_G4_SMIME_LP_ORG = _G4_SMIME + (25,)

_G4_EUTL = _G4 + (14,)

_G4_PRIVATE_TLS = _G4 + (15, 35)

_G4_PRIVATE_OTHER = _G4 + (16,)
_G4_PRIVATE_OTHER_NP_IND = _G4 + (11,)
_G4_PRIVATE_OTHER_NP_REGP = _G4 + (12,)
_G4_PRIVATE_OTHER_NP_SPON = _G4 + (13,)
_G4_PRIVATE_OTHER_NP_RPSP = _G4 + (14,)
_G4_PRIVATE_OTHER_LP_ORG = _G4 + (25,)

_G4_DEFENCE = _G4 + (36,)

id_Public_G3_Citizen_OCSP_Signing = _G3_BURGER + (1,)
id_Public_G3_Citizen_Authenticity = _G3_BURGER + (1,)
id_Public_G3_Citizen_Non_repudiation_eSignatures = _G3_BURGER + (2,)
id_Public_G3_Citizen_Confidentiality = _G3_BURGER + (3,)
id_Public_G3_Organization_Persons_OCSP_Signing = _G3_ORG + (1,)
id_Public_G3_Organization_Persons_Authenticity = _G3_ORG + (1,)
id_Public_G3_Organization_Persons_Non_repudiation_eSignatures = _G3_ORG + (2,)
id_Public_G3_Organization_Persons_Confidentiality = _G3_ORG + (3,)
id_Public_G3_Organization_Services_OCSP_Signing = _G3_ORG + (4,)
id_Public_G3_Organization_Services_Authenticity = _G3_ORG + (4,)
id_Public_G3_Organization_Services_Confidentiality = _G3_ORG + (5,)
id_Public_G3_Organization_Services_Non_repudiation_eSeals = _G3_ORG + (7,)
id_Public_G3_Autonomous_Devices_OCSP_Signing_Services = _G3_AD + (1,)
id_Public_G3_Autonomous_Devices_Authenticity = _G3_AD + (1,)
id_Public_G3_Autonomous_Devices_Confidentiality = _G3_AD + (2,)
id_Public_G3_Autonomous_Devices_Combination = _G3_AD + (3,)
id_Public_G3_Citizen_2023_Authenticity = _G3_BURGER + (4,)
id_Public_G3_Citizen_2023_Non_repudiation_eSignatures = _G3_BURGER + (5,)
id_Public_G3_Citizen_2023_Confidentiality = _G3_BURGER + (6,)
id_Public_G3_Organization_Persons_2023_Authenticity = _G3_ORG + (10,)
id_Public_G3_Organization_Persons_2023_Non_repudiation_eSignatures = _G3_ORG + (11,)
id_Public_G3_Organization_Persons_2023_Confidentiality = _G3_ORG + (12,)
id_Public_G3_Organization_Services_2023_Authenticity = _G3_ORG + (13,)
id_Public_G3_Organization_Services_2023_Confidentiality = _G3_ORG + (14,)
id_Public_G3_Organization_Services_2023_Non_repudiation_eSeals = _G3_ORG + (15,)
id_Public_G3_SMIME_2023_OCSP_Signing_SMME = _CP + (10, 9)
id_Public_G3_SMIME_2023_Organization_validated_Dual_Use = _CP + (10, 9)
id_Public_G3_SMIME_2023_Sponsor_validated_Dual_Use = _CP + (11, 9)
id_Public_G3_SMIME_2023_Individual_validated_Dual_Use = _CP + (12, 9)
id_Private_G1_Persons_OCSP_Signing = _G1_PRIVATE + (1,)
id_Private_G1_Persons_Authenticity = _G1_PRIVATE + (1,)
id_Private_G1_Persons_Non_repudiation_eSignatures = _G1_PRIVATE + (2,)
id_Private_G1_Persons_Confidentiality = _G1_PRIVATE + (3,)
id_Private_G1_Services_OCSP_Signing = _G1_PRIVATE + (4,)
id_Private_G1_Services_Authenticity = _G1_PRIVATE + (4,)
id_Private_G1_Services_Confidentiality = _G1_PRIVATE + (5,)
id_Private_G1_Services_Server_OV = _G1_PRIVATE + (6,)

id_SMIME_G4_Natural_Persons_OCSP_Signing = _G4_SMIME_NP_IND + (10,)
id_SMIME_G4_Natural_Persons_Individual_Validated_Signing_only = _G4_SMIME_NP_IND + (37,)
id_SMIME_G4_Natural_Persons_Individual_Validated_Key_Management = _G4_SMIME_NP_IND + (
    38,
)
id_SMIME_G4_Natural_Persons_Individual_Validated_Dual_Use = _G4_SMIME_NP_IND + (39,)
id_SMIME_G4_Natural_Persons_Sponsor_Validated_Signing_only = _G4_SMIME_NP_SPON + (37,)
id_SMIME_G4_Natural_Persons_Sponsor_Validated_Key_Management = _G4_SMIME_NP_SPON + (38,)
id_SMIME_G4_Natural_Persons_Sponsor_Validated_Dual_Use = _G4_SMIME_NP_SPON + (39,)
id_SMIME_G4_Legal_Entities_OCSP_Signing = _G4_SMIME_LP_ORG + (10,)
id_SMIME_G4_Legal_Entities_Organization_Validated_Signing_only = _G4_SMIME_LP_ORG + (
    37,
)
id_SMIME_G4_Legal_Entities_Organization_Validated_Key_Management = _G4_SMIME_LP_ORG + (
    38,
)
id_SMIME_G4_Legal_Entities_Organization_Validated_Dual_Use = _G4_SMIME_LP_ORG + (39,)
id_EUTL_G4_Natural_Persons_Individual_Validated_eSig = _G4_EUTL + (11, 5)
id_EUTL_G4_Natural_Persons_Regulated_Profession_Validated_eSig = _G4_EUTL + (12, 5)
id_EUTL_G4_Natural_Persons_Sponsor_Validated_eSig = _G4_EUTL + (13, 5)
id_EUTL_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_eSig = _G4_EUTL + (14, 5)
id_EUTL_G4_Natural_Persons_OCSP_Signing = _G4_EUTL + (14, 10)
id_EUTL_G4_Legal_Entities_Organization_Validated_eSeal = _G4_EUTL + (25, 5)
id_EUTL_G4_Legal_Entities_OCSP_Signing = _G4_EUTL + (25, 10)
id_Private_TLS_G4_Devices_OCSP_Signing = _G4_PRIVATE_TLS + (10,)
id_Private_TLS_G4_Devices_Organization_Validated_Server = _G4_PRIVATE_TLS + (11,)
id_Private_Other_Generic_G4_Natural_Persons_Individual_Validated_Authenticity = (
    _G4_PRIVATE_OTHER_NP_IND + (4,)
)
id_Private_Other_Generic_G4_Natural_Persons_Individual_Validated_Confidentiality = (
    _G4_PRIVATE_OTHER_NP_IND + (7,)
)
id_Private_Other_Generic_G4_Natural_Persons_Individual_Validated_Authentication = (
    _G4_PRIVATE_OTHER_NP_IND + (8,)
)
id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_Validated_Authenticity = (
    _G4_PRIVATE_OTHER_NP_REGP + (4,)
)
id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_Validated_Confidentiality = (
    _G4_PRIVATE_OTHER_NP_REGP + (7,)
)
id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_Validated_Authentication = (
    _G4_PRIVATE_OTHER_NP_REGP + (8,)
)
id_Private_Other_Generic_G4_Natural_Persons_Sponsor_Validated_Authenticity = (
    _G4_PRIVATE_OTHER_NP_SPON + (4,)
)
id_Private_Other_Generic_G4_Natural_Persons_Sponsor_Validated_Confidentiality = (
    _G4_PRIVATE_OTHER_NP_SPON + (7,)
)
id_Private_Other_Generic_G4_Natural_Persons_Sponsor_Validated_Authentication = (
    _G4_PRIVATE_OTHER_NP_SPON + (8,)
)
id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authenticity = (
    _G4_PRIVATE_OTHER_NP_RPSP + (4,)
)
id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Confidentiality = (
    _G4_PRIVATE_OTHER_NP_RPSP + (7,)
)
id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authentication = (
    _G4_PRIVATE_OTHER_NP_RPSP + (8,)
)
id_Private_Other_Generic_G4_Natural_Persons_OCSP_Signing = _G4_PRIVATE_OTHER_NP_RPSP + (
    10,
)
id_Private_Other_Generic_G4_Legal_Entities_Org_Validated_Authenticity = (
    _G4_PRIVATE_OTHER_LP_ORG + (4,)
)
id_Private_Other_Generic_G4_Legal_Entities_Org_Validated_Confidentiality = (
    _G4_PRIVATE_OTHER_LP_ORG + (7,)
)
id_Private_Other_Generic_G4_Legal_Entities_Org_Validated_Authentication = (
    _G4_PRIVATE_OTHER_LP_ORG + (8,)
)
id_Private_Other_Generic_G4_Legal_Entities_OCSP_Signing = _G4_PRIVATE_OTHER_LP_ORG + (
    10,
)

_G4_ILT = _G4 + (56,)
_G4_CIBG = _G4 + (46,)

# Private Other Defence G4
_G4_DEFENCE_SPONSOR = _G4_DEFENCE + (13,)

id_Private_Other_Defence_G4_Natural_Persons_Sponsor_Validated_Authenticity = (
    _G4_DEFENCE_SPONSOR + (4,)
)
id_Private_Other_Defence_G4_Natural_Persons_Sponsor_Validated_Confidentiality = (
    _G4_DEFENCE_SPONSOR + (7,)
)
id_Private_Other_Defence_G4_Natural_Persons_Sponsor_Validated_Authentication = (
    _G4_DEFENCE_SPONSOR + (8,)
)
id_Private_Other_Defence_G4_Natural_Persons_OCSP_Signing = _G4_DEFENCE_SPONSOR + (10,)

# Private Other ILT G4
_G4_ILT_REG_PROF = _G4_ILT + (12,)
_G4_ILT_SPONSOR = _G4_ILT + (13,)
_G4_ILT_REG_PROF_SPONSOR = _G4_ILT + (14,)
_G4_ILT_LEGAL_ENTITIES = _G4_ILT + (25,)
_G4_ILT_DEVICES = _G4_ILT + (37,)

id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_Validated_Authenticity = (
    _G4_ILT_REG_PROF + (4,)
)
id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_Validated_Confidentiality = (
    _G4_ILT_REG_PROF + (7,)
)
id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_Validated_Authentication = (
    _G4_ILT_REG_PROF + (8,)
)
id_Private_Other_ILT_G4_Natural_Persons_Sponsor_Validated_Authenticity = (
    _G4_ILT_SPONSOR + (4,)
)
id_Private_Other_ILT_G4_Natural_Persons_Sponsor_Validated_Confidentiality = (
    _G4_ILT_SPONSOR + (7,)
)
id_Private_Other_ILT_G4_Natural_Persons_Sponsor_Validated_Authentication = (
    _G4_ILT_SPONSOR + (8,)
)
id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authenticity = (
    _G4_ILT_REG_PROF_SPONSOR + (4,)
)
id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Confidentiality = (
    _G4_ILT_REG_PROF_SPONSOR + (7,)
)
id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authentication = (
    _G4_ILT_REG_PROF_SPONSOR + (8,)
)
id_Private_Other_ILT_G4_Natural_Persons_OCSP_Signing = _G4_ILT_REG_PROF_SPONSOR + (10,)
id_Private_Other_ILT_G4_Legal_Entities_Org_Validated_Authenticity = (
    _G4_ILT_LEGAL_ENTITIES + (4,)
)
id_Private_Other_ILT_G4_Legal_Entities_Org_Validated_Confidentiality = (
    _G4_ILT_LEGAL_ENTITIES + (7,)
)
id_Private_Other_ILT_G4_Legal_Entities_Org_Validated_Authentication = (
    _G4_ILT_LEGAL_ENTITIES + (8,)
)
id_Private_Other_ILT_G4_Legal_Entities_OCSP_Signing = _G4_ILT_LEGAL_ENTITIES + (10,)
id_Private_Other_ILT_G4_Devices_Device_Validated_Authenticity = _G4_ILT_DEVICES + (4,)
id_Private_Other_ILT_G4_Devices_OCSP_signing = _G4_ILT_DEVICES + (10,)

# Private Other CIBG G4
_G4_CIBG_REG_PROF = _G4_CIBG + (12,)
_G4_CIBG_SPONSOR = _G4_CIBG + (13,)
_G4_CIBG_REG_PROF_SPONSOR = _G4_CIBG + (14,)
_G4_CIBG_LEGAL_ENTITIES = _G4_CIBG + (25,)

id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_Validated_Authenticity = (
    _G4_CIBG_REG_PROF + (4,)
)
id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_Validated_Confidentiality = (
    _G4_CIBG_REG_PROF + (7,)
)
id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_Validated_Authentication = (
    _G4_CIBG_REG_PROF + (8,)
)
id_Private_Other_CIBG_G4_Natural_Persons_Sponsor_Validated_Authenticity = (
    _G4_CIBG_SPONSOR + (4,)
)
id_Private_Other_CIBG_G4_Natural_Persons_Sponsor_Validated_Confidentiality = (
    _G4_CIBG_SPONSOR + (7,)
)
id_Private_Other_CIBG_G4_Natural_Persons_Sponsor_Validated_Authentication = (
    _G4_CIBG_SPONSOR + (8,)
)
id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authenticity = (
    _G4_CIBG_REG_PROF_SPONSOR + (4,)
)
id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Confidentiality = (
    _G4_CIBG_REG_PROF_SPONSOR + (7,)
)
id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authentication = (
    _G4_CIBG_REG_PROF_SPONSOR + (8,)
)
id_Private_Other_CIBG_G4_Natural_Persons_OCSP_Signing = _G4_CIBG_REG_PROF_SPONSOR + (
    10,
)
id_Private_Other_CIBG_G4_Legal_Entities_Org_Validated_Authenticity = (
    _G4_CIBG_LEGAL_ENTITIES + (4,)
)
id_Private_Other_CIBG_G4_Legal_Entities_Org_Validated_Confidentiality = (
    _G4_CIBG_LEGAL_ENTITIES + (7,)
)
id_Private_Other_CIBG_G4_Legal_Entities_Org_Validated_Authentication = (
    _G4_CIBG_LEGAL_ENTITIES + (8,)
)
id_Private_Other_CIBG_G4_Legal_Entities_OCSP_Signing = _G4_CIBG_LEGAL_ENTITIES + (10,)

PKIO_OIDS = {
    id_Public_G3_Citizen_OCSP_Signing,
    id_Public_G3_Citizen_Authenticity,
    id_Public_G3_Citizen_Non_repudiation_eSignatures,
    id_Public_G3_Citizen_Confidentiality,
    id_Public_G3_Organization_Persons_OCSP_Signing,
    id_Public_G3_Organization_Persons_Authenticity,
    id_Public_G3_Organization_Persons_Non_repudiation_eSignatures,
    id_Public_G3_Organization_Persons_Confidentiality,
    id_Public_G3_Organization_Services_OCSP_Signing,
    id_Public_G3_Organization_Services_Authenticity,
    id_Public_G3_Organization_Services_Confidentiality,
    id_Public_G3_Organization_Services_Non_repudiation_eSeals,
    id_Public_G3_Autonomous_Devices_OCSP_Signing_Services,
    id_Public_G3_Autonomous_Devices_Authenticity,
    id_Public_G3_Autonomous_Devices_Confidentiality,
    id_Public_G3_Autonomous_Devices_Combination,
    id_Public_G3_Citizen_2023_Authenticity,
    id_Public_G3_Citizen_2023_Non_repudiation_eSignatures,
    id_Public_G3_Citizen_2023_Confidentiality,
    id_Public_G3_Organization_Persons_2023_Authenticity,
    id_Public_G3_Organization_Persons_2023_Non_repudiation_eSignatures,
    id_Public_G3_Organization_Persons_2023_Confidentiality,
    id_Public_G3_Organization_Services_2023_Authenticity,
    id_Public_G3_Organization_Services_2023_Confidentiality,
    id_Public_G3_Organization_Services_2023_Non_repudiation_eSeals,
    id_Public_G3_SMIME_2023_OCSP_Signing_SMME,
    id_Public_G3_SMIME_2023_Organization_validated_Dual_Use,
    id_Public_G3_SMIME_2023_Sponsor_validated_Dual_Use,
    id_Public_G3_SMIME_2023_Individual_validated_Dual_Use,
    id_Private_G1_Persons_OCSP_Signing,
    id_Private_G1_Persons_Authenticity,
    id_Private_G1_Persons_Non_repudiation_eSignatures,
    id_Private_G1_Persons_Confidentiality,
    id_Private_G1_Services_OCSP_Signing,
    id_Private_G1_Services_Authenticity,
    id_Private_G1_Services_Confidentiality,
    id_Private_G1_Services_Server_OV,
    id_SMIME_G4_Natural_Persons_OCSP_Signing,
    id_SMIME_G4_Natural_Persons_Individual_Validated_Signing_only,
    id_SMIME_G4_Natural_Persons_Individual_Validated_Key_Management,
    id_SMIME_G4_Natural_Persons_Individual_Validated_Dual_Use,
    id_SMIME_G4_Natural_Persons_Sponsor_Validated_Signing_only,
    id_SMIME_G4_Natural_Persons_Sponsor_Validated_Key_Management,
    id_SMIME_G4_Natural_Persons_Sponsor_Validated_Dual_Use,
    id_SMIME_G4_Legal_Entities_OCSP_Signing,
    id_SMIME_G4_Legal_Entities_Organization_Validated_Signing_only,
    id_SMIME_G4_Legal_Entities_Organization_Validated_Key_Management,
    id_SMIME_G4_Legal_Entities_Organization_Validated_Dual_Use,
    id_EUTL_G4_Natural_Persons_Individual_Validated_eSig,
    id_EUTL_G4_Natural_Persons_Regulated_Profession_Validated_eSig,
    id_EUTL_G4_Natural_Persons_Sponsor_Validated_eSig,
    id_EUTL_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_eSig,
    id_EUTL_G4_Natural_Persons_OCSP_Signing,
    id_EUTL_G4_Legal_Entities_Organization_Validated_eSeal,
    id_EUTL_G4_Legal_Entities_OCSP_Signing,
    id_Private_TLS_G4_Devices_OCSP_Signing,
    id_Private_TLS_G4_Devices_Organization_Validated_Server,
    id_Private_Other_Generic_G4_Natural_Persons_Individual_Validated_Authenticity,
    id_Private_Other_Generic_G4_Natural_Persons_Individual_Validated_Confidentiality,
    id_Private_Other_Generic_G4_Natural_Persons_Individual_Validated_Authentication,
    id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_Validated_Authenticity,
    id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_Validated_Confidentiality,
    id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_Validated_Authentication,
    id_Private_Other_Generic_G4_Natural_Persons_Sponsor_Validated_Authenticity,
    id_Private_Other_Generic_G4_Natural_Persons_Sponsor_Validated_Confidentiality,
    id_Private_Other_Generic_G4_Natural_Persons_Sponsor_Validated_Authentication,
    id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authenticity,
    id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Confidentiality,
    id_Private_Other_Generic_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authentication,
    id_Private_Other_Generic_G4_Natural_Persons_OCSP_Signing,
    id_Private_Other_Generic_G4_Legal_Entities_Org_Validated_Authenticity,
    id_Private_Other_Generic_G4_Legal_Entities_Org_Validated_Confidentiality,
    id_Private_Other_Generic_G4_Legal_Entities_Org_Validated_Authentication,
    id_Private_Other_Generic_G4_Legal_Entities_OCSP_Signing,
    id_Private_Other_Defence_G4_Natural_Persons_Sponsor_Validated_Authenticity,
    id_Private_Other_Defence_G4_Natural_Persons_Sponsor_Validated_Confidentiality,
    id_Private_Other_Defence_G4_Natural_Persons_Sponsor_Validated_Authentication,
    id_Private_Other_Defence_G4_Natural_Persons_OCSP_Signing,
    id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_Validated_Authenticity,
    id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_Validated_Confidentiality,
    id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_Validated_Authentication,
    id_Private_Other_ILT_G4_Natural_Persons_Sponsor_Validated_Authenticity,
    id_Private_Other_ILT_G4_Natural_Persons_Sponsor_Validated_Confidentiality,
    id_Private_Other_ILT_G4_Natural_Persons_Sponsor_Validated_Authentication,
    id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authenticity,
    id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Confidentiality,
    id_Private_Other_ILT_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authentication,
    id_Private_Other_ILT_G4_Natural_Persons_OCSP_Signing,
    id_Private_Other_ILT_G4_Legal_Entities_Org_Validated_Authenticity,
    id_Private_Other_ILT_G4_Legal_Entities_Org_Validated_Confidentiality,
    id_Private_Other_ILT_G4_Legal_Entities_Org_Validated_Authentication,
    id_Private_Other_ILT_G4_Legal_Entities_OCSP_Signing,
    id_Private_Other_ILT_G4_Devices_Device_Validated_Authenticity,
    id_Private_Other_ILT_G4_Devices_OCSP_signing,
    id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_Validated_Authenticity,
    id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_Validated_Confidentiality,
    id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_Validated_Authentication,
    id_Private_Other_CIBG_G4_Natural_Persons_Sponsor_Validated_Authenticity,
    id_Private_Other_CIBG_G4_Natural_Persons_Sponsor_Validated_Confidentiality,
    id_Private_Other_CIBG_G4_Natural_Persons_Sponsor_Validated_Authentication,
    id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authenticity,
    id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Confidentiality,
    id_Private_Other_CIBG_G4_Natural_Persons_Reg_Prof_w_Sponsor_Val_Authentication,
    id_Private_Other_CIBG_G4_Natural_Persons_OCSP_Signing,
    id_Private_Other_CIBG_G4_Legal_Entities_Org_Validated_Authenticity,
    id_Private_Other_CIBG_G4_Legal_Entities_Org_Validated_Confidentiality,
    id_Private_Other_CIBG_G4_Legal_Entities_Org_Validated_Authentication,
    id_Private_Other_CIBG_G4_Legal_Entities_OCSP_Signing,
}
