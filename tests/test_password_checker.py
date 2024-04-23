import pytest
from lib.password_checker import *

def test_passwordchecker():
    password_checker = PasswordChecker()
    
    with pytest.raises(Exception) as e:
        password_checker.check("passwor")
    error = str(e.value)
    assert error == "Invalid password, must be 8+ characters."
        