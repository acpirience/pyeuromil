""" Unit tests for Euromil.py """
from pyeuromil import Euromil


def test_euromil_load_data():
    """ data load test """
    my_euromil = Euromil()
    my_euromil._load_data(2011)
    my_euromil._load_data(2012)

    assert my_euromil._storage["2011"]["30/12/2011"], "16 36 43 44 50 07 08"
    assert my_euromil._storage["2012"]["03/01/2012"], "03 30 42 45 49 05 10"
