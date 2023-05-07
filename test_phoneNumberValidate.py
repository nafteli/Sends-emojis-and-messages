import pytest
from phoneNumberValidate import phoneNumber


def test_phoneNumber(monkeypatch):
    inout = {
        "": -1,
        "1": -1,
        "1234567890": -1,
        "string to test": -1,
        "0505050505": "972505050505",
        "+972505050505": "972505050505",
        "+972 50-505-0505": "972505050505",
        # Test phone number with [U+2066] Left-To-Right Isolate (Available when copying a number from WhatsApp)
        "⁦+972 50-505-0505⁩": "972505050505",

    }
    for k, v in inout.items():
        monkeypatch.setattr("builtins.input", lambda prompt: k)
        assert phoneNumber() == v
    # # Test valid phone number without country code
    # monkeypatch.setattr("builtins.input", lambda prompt: "0505050505")
    # assert phoneNumber() == "972505050505"

    # # Test valid phone number with country code
    # monkeypatch.setattr("builtins.input", lambda prompt: "+972505050505")
    # assert phoneNumber() == "972505050505"

    # # Check for a valid phone number with a space and - between the numbers
    # monkeypatch.setattr("builtins.input", lambda prompt: "+972 50-505-0505")
    # assert phoneNumber() == "972505050505"

    # # Test phone number with [U+2066] Left-To-Right Isolate (Available when copying a number from WhatsApp)
    # monkeypatch.setattr("builtins.input", lambda prompt: "⁦+972 50-505-0505⁩")
    # assert phoneNumber() == "972505050505"

    # # Test phone number with non-numeric characters
    # monkeypatch.setattr("builtins.input", lambda prompt: "string to test")
    # assert phoneNumber() == -1
# Test empty phone number
    # 
    # monkeypatch.setattr("builtins.input", lambda prompt: "")
    # assert phoneNumber() == -1

    # # Test phone number with incorrect length
    # monkeypatch.setattr("builtins.input", lambda prompt: "1")
    # assert phoneNumber() == -1
