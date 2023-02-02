import pytest

from phoneNumberValidate import phoneNumber


@pytest.mark.parametrize("Phone_number, output",
                         [("phone_number", -1), ('', -1), ("+972123456789", '972123456789'),
                          ("+972 12-345-6789", '972123456789'), (12345678, -1), (0, -1),
                          ('  ', -1), ('1', -1)])
def test_phoneNumber(Phone_number, output):
    test = phoneNumber(Phone_number)
    assert test == output
