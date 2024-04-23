import pytest
from lib.present import *

def test_present():
    present = Present()
    present.wrap(None)
    with pytest.raises(Exception) as e:
        present.unwrap()
    error = str(e.value)
    assert error == "No contents have been wrapped."
    
def test_present_wrap():
    present = Present()
    present.wrap("something")
    with pytest.raises(Exception) as e:
        present.wrap("something")
    error = str(e.value)
    assert error == "A contents has already been wrapped."