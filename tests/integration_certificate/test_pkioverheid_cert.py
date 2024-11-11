import glob
import glob
import sys
from os import path

from pkilint import pkioverheid
from pkilint.pkix import certificate
from tests.integration_certificate import register_test

this_module = sys.modules[__name__]


for certificate_type in pkioverheid.pkioverheid_constants.CertificateType:
    cur_dir = path.dirname(__file__)

    test_dir = path.join(cur_dir, "pkioverheid", certificate_type.name.lower())

    files = glob.glob(path.join(test_dir, "*.crttest"))

    for file in files:
        validator = certificate.create_pkix_certificate_validator_container(
            pkioverheid.create_decoding_validators(certificate_type),
            pkioverheid.create_validators(certificate_type),
        )

        file_no_ext, _ = path.splitext(path.basename(file))

        test_name = f"test_{certificate_type}_{file_no_ext}"

        register_test(this_module, file, test_name, validator)
