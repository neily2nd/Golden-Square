from lib.string_builder import *

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("hello")
    sentence = string_builder.output()
    assert sentence == "hello"


def test_string_builder_two():
    string_builder = StringBuilder()
    string_builder.add("thisislong")
    length = string_builder.size()
    assert length == 10