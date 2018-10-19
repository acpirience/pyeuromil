""" Unit tests for Euromil.py """
import pytest
from pyeuromil import Euromil


def test_year_is_valid():
    """  test year_is_valid method """
    assert Euromil.year_is_valid(2011)
    assert not Euromil.year_is_valid(2000)
    assert not Euromil.year_is_valid("abcd")


def test_month_is_valid():
    """  test month_is_valid method """
    assert Euromil.month_is_valid(9)
    assert not Euromil.month_is_valid(13)
    assert not Euromil.month_is_valid("abcd")


def test_euromil_init():
    """ __init test_ """
    my_euromil = Euromil()
    assert my_euromil._storage == {}


def test_euromil_load_data():
    """ data load test """
    my_euromil = Euromil()

    my_euromil._load_data(2011)
    assert my_euromil._storage["2011"]
    assert my_euromil._storage["2011"]["30/12/2011"].n1 == "16"

    my_euromil._load_data(2012)
    assert my_euromil._storage["2012"]
    assert my_euromil._storage["2012"]["03/01/2012"].star2 == "10"


def test_euromil_results_year_not_exist():
    """ results of year test (year does not exists) """
    my_euromil = Euromil()
    with pytest.raises(ValueError):
        results = my_euromil.results("abcd")
        assert results is None
        results = my_euromil.results(1920)
        assert results is None


def test_euromil_results_year_exist():
    """ results of year test (year exists) """
    my_euromil = Euromil()
    results = my_euromil.results(2011)
    assert results["30/12/2011"].n1 == "16"


def test_euromil_results_year_month_not_exist():
    """ results of year+month test (month does not exists) """
    my_euromil = Euromil()
    with pytest.raises(ValueError):
        results = my_euromil.results(2011, 13)
        assert results is None
        results = my_euromil.results(2011, "abcd")
        assert results is None


def test_euromil_results_year_month_exist():
    """ results of year+month test (month exists) """
    my_euromil = Euromil()
    results = my_euromil.results(2011, 10)
    assert results["14/10/2011"].n1 == "12"
    assert results["04/10/2011"].star1 == "08"


def test_euromil_results_year_month_day_not_exist():
    """ results of year+month+day test (day not exist) """
    my_euromil = Euromil()
    with pytest.raises(ValueError):
        results = my_euromil.results(2011, 10, 5)
        assert results is None
        results = my_euromil.results(2011, 10, "abcd")
        assert results is None


def test_euromil_results_year_month_day_exist():
    """ results of year+month+day test (all exist) """
    my_euromil = Euromil()
    results = my_euromil.results(2011, 10, 4)
    assert results.n1 == "14"
    results = my_euromil.results(2011, 10, 14)
    assert results.star1 == "03"


def test_euromil_draw_dates():
    """ test draw_dates method  """
    my_euromil = Euromil()

    assert my_euromil.draw_dates(2011) is not None
    assert "03/06/2011" in my_euromil.draw_dates(2011)
    assert "16/12/2011" in my_euromil.draw_dates(2011, 12)
