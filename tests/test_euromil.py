""" Unit tests for Euromil.py """
from datetime import date
import pytest
from pyeuromil import Euromil


def test_euromil_init():
    """ __init test_ """
    my_euromil = Euromil()
    assert my_euromil._storage == {}


def test_euromil_load_data():
    """ data load test """
    my_euromil = Euromil()

    my_euromil._load_data(2011)
    assert my_euromil._storage["2011"]
    assert my_euromil._storage["2011"]["2011-12-30"].n1 == "16"

    my_euromil._load_data(2012)
    assert my_euromil._storage["2012"]
    assert my_euromil._storage["2012"]["2012-01-03"].star2 == "10"


def test_euromil_results_year_not_exist():
    """ results of year test (year does not exists) """
    my_euromil = Euromil()
    with pytest.raises(ValueError):
        results = my_euromil.results("abcd")
        assert results is None
        results = my_euromil.results(1920)
        assert results is None


def test_euromil_results_invalid_date():
    """ results method (invalid date) """
    my_euromil = Euromil()
    with pytest.raises(ValueError):
        results = my_euromil.results("111")
        assert results is None

    with pytest.raises(ValueError):
        results = my_euromil.results(date(2011, 1, 1), "111")
        assert results is None


def test_euromil_results_no_param():
    """ results method (no param) """
    my_euromil = Euromil()
    results = my_euromil.results()

    assert results[0].date.year == 2011
    assert results[-1].date.year == 2018


def test_euromil_results_start_date_only():
    """ results method (start_date only) """
    my_euromil = Euromil()
    results = my_euromil.results(date(2012, 12, 12))

    assert results[0].date == date(2012, 12, 28)
    assert results[-1].date > date(2018, 1, 1)


def test_euromil_results_both_dates_empty():
    """ results method (both dates, no results) """
    my_euromil = Euromil()
    results = my_euromil.results(date(2012, 12, 12), date(2012, 12, 13))

    assert results == []


def test_euromil_results_both_dates_wrong_order():
    """ results method (end_date < start_date) """
    my_euromil = Euromil()
    results = my_euromil.results(date(2018, 12, 12), date(2011, 12, 13))

    assert results == []


def test_euromil_results_both_dates_one_result():
    """ results method (end_date < start_date) """
    my_euromil = Euromil()
    results = my_euromil.results(date(2018, 10, 18), date(2018, 10, 20))

    assert len(results) == 1
    assert results[0].n1 == "01"
    assert results[0].star1 == "03"


def test_euromil_draw_dates():
    """ test draw_dates method  """
    my_euromil = Euromil()

    assert date(2018, 10, 19) in my_euromil.draw_dates()
    assert date(2011, 6, 3) in my_euromil.draw_dates(
        date(2011, 1, 1), date(2011, 12, 31)
    )
    assert date(2013, 11, 15) in my_euromil.draw_dates(
        date(2013, 10, 30), date(2013, 11, 15)
    )
