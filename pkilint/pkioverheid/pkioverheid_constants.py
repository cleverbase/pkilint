import enum
from enum import auto

VERSION = "5.0"


@enum.unique
class CertificateType(enum.IntEnum):
    EUTL_G4_NATURAL_PERSONS_INDIVIDUAL_VALIDATED_ESIG = auto()

    def __str__(self):
        return self.name

    @property
    def to_option_str(self):
        return self.name.replace("_", "-")

    @staticmethod
    def from_option_str(value):
        value = value.replace("-", "_").upper()

        return CertificateType[value]
