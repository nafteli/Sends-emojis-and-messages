import pytest

from phoneNumberValidate import phoneNumber


def test_phoneNumber(monkeypatch):
    # Test valid phone number without country code
    monkeypatch.setattr("builtins.input", lambda prompt: "0505050505")
    assert phoneNumber() == "972505050505"

    # Test valid phone number with country code
    monkeypatch.setattr("builtins.input", lambda prompt: "+972505050505")
    assert phoneNumber() == "972505050505"

    # Check for a valid phone number with a space and - between the numbers
    monkeypatch.setattr("builtins.input", lambda prompt: "+972 50-505-0505")
    assert phoneNumber() == "972505050505"

    # Test phone number with non-numeric characters
    monkeypatch.setattr("builtins.input", lambda prompt: "abcdefghijkl")
    assert phoneNumber() == -1

    # Test empty phone number
    monkeypatch.setattr("builtins.input", lambda prompt: "")
    assert phoneNumber() == -1

    # Test phone number with incorrect length
    monkeypatch.setattr("builtins.input", lambda prompt: "1")
    assert phoneNumber() == -1
