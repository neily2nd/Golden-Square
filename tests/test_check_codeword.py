#File: tests/test_check_codeword.py  why am i writing this its just telling us what to call the file

from lib.check_codeword import *

def test_check_codeword_correct():
    codeword = check_codeword("horse")
    assert codeword == "Correct! Come in."
    
def test_check_codeword_close():
    codeword = check_codeword("house")
    assert codeword == "Close, but nope."
    
def test_check_codeword_wrong():
    codeword = check_codeword("car")
    assert codeword == "WRONG"