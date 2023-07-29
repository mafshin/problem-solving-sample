from P016 import *

def test_beginning():
    assert slohsen(4) == ["@@@@",
                          "@@@",
                          "@@",
                          "@"]
def test_end():
    assert slohsen(7) == ["@@@@@@@",
                          "@@@@@@",
                          "@@@@@",
                          "@@@@",
                          "@@@",
                          "@@",
                          "@"]