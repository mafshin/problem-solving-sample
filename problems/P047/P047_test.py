from P047 import *

def test_1():
    assert P047(10) == 4

def test_2():
    assert P047(1000000) == 78498

def test_3():
    assert P047(1000000000) == 50847534

def test_4():
    assert P047(100000000000) == 4118054813