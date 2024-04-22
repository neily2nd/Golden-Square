#File test/test_greet.py
from lib.greet import *

def test_greet_returns_name():
    name = greet("Neil")
    assert name == "Hello, Neil!"