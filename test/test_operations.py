import sys,os

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import src.hola as opera

def test_suma():
    assert opera.suma(10,12) == 22