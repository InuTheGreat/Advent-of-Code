from Elves1 import *

def test_elfInput():
    x = elfInput("input.txt")
    assert int(x[0]) == 2000
    assert int(x[3]) == 11485
    
