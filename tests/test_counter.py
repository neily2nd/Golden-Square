from lib.counter import *

def test_counter():
    counter = Counter()
    counter.add(50)
    count = counter.report()
    assert count == "Counted to 50 so far."