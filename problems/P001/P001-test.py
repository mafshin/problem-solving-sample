from P001 import *

def test_even():
    assert even_odd(50) == '50 is even'

def test_even():
    assert even_odd(11) == '11 is odd'

def test_zero():
    assert even_odd(0) == '0 is even'

def test_larg():
    assert even_odd(10003203) == '10003203 is odd'

def test_number1():
    assert even_odd(46) == '46 is even'

def test_number2():
    assert even_odd(94) == '94 is even'

def test_number3():
    assert even_odd(39) == '39 is odd'

def test_number4():
    assert even_odd(58) == '58 is even'