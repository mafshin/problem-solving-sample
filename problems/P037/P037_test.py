from P037 import *

def test1():

    a = ["Today is president resignation date, a vantage point in history of our country. You, the next generation of this soil, will decide who should take control of your country."]

    b = ["soil" , "president" , "vantage" , "country"]

    ouput = "Today is resignation date, a point in history of our . You, the next generation of this , will decide who should take control of your ."

    assert P037(a , b) == ouput