from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("life")
    
    assert gratitudes.format() == "Be grateful for: life"
    
    