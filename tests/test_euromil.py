""" Unit tests for Euromil.py """
from pyeuromil import Euromil


def test_euromil():
    """ simple read test """
    my_euromil = Euromil()
    assert my_euromil.test == "date       n1 n2 n3 n4 n5 *1 *2"
