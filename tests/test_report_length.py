from lib.report_length import *

def test_report_length():
    length = report_length("testing")
    assert length == "This string was 7 characters long."