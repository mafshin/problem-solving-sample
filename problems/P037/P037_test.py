from P037 import *

def test1():
    a = 'Today is president resignation date, a vantage point in history of our country. You, the next generation of this soil, will decide who should take control of your country.'

    b = ['soil' , 'prisident' , 'vantage' , 'country']

    ouput = 'Today is resignation date, a point in history of our . You, the next generation of this , will decide who should take control of your .'

    assert P037(a , b) == ouput

def test2():
    A = "This text is a very long text which has many repeated text inside this long text."

    B = ["is" , "This" , "very"]

    OUPUT = "text a long text which has many repeated text inside this long text."

    assert P037(A , B) == OUPUT