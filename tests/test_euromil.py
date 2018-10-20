""" Unit tests for Euromil.py """
from datetime import date
import pytest
from pyeuromil import Euromil


@pytest.fixture()
def euromil():
    """ Fixture of an Euromil isntance """
    return Euromil()


def test_euromil_init(euromil):
    """ __init test_ """
    assert euromil._storage == {}


def test_euromil_load_data(euromil):
    """ data load test """
    euromil._load_data(2011)
    assert euromil._storage["2011"]
    assert euromil._storage["2011"]["2011-12-30"].n1 == 16

    euromil._load_data(2012)
    assert euromil._storage["2012"]
    assert euromil._storage["2012"]["2012-01-03"].star2 == 10


def test_euromil_results_year_not_exist(euromil):
    """ results of year test (year does not exists) """
    with pytest.raises(ValueError):
        results = euromil.results("abcd")
        assert results is None
        results = euromil.results(1920)
        assert results is None


def test_euromil_results_invalid_date(euromil):
    """ results method (invalid date) """
    with pytest.raises(ValueError):
        results = euromil.results("111")
        assert results is None

    with pytest.raises(ValueError):
        results = euromil.results(date(2011, 1, 1), "111")
        assert results is None


def test_euromil_results_no_param(euromil):
    """ results method (no param) """
    results = euromil.results()

    assert results[0].date.year == 2011
    assert results[-1].date.year == 2018


def test_euromil_results_start_date_only(euromil):
    """ results method (start_date only) """
    uromil = Euromil()
    results = euromil.results(date(2012, 12, 12))

    assert results[0].date == date(2012, 12, 28)
    assert results[-1].date > date(2018, 1, 1)


def test_euromil_results_both_dates_empty(euromil):
    """ results method (both dates, no results) """
    results = euromil.results(date(2012, 12, 12), date(2012, 12, 13))

    assert results == []


def test_euromil_results_both_dates_wrong_order(euromil):
    """ results method (end_date < start_date) """
    results = euromil.results(date(2018, 12, 12), date(2011, 12, 13))

    assert results == []


def test_euromil_results_both_dates_one_result(euromil):
    """ results method (end_date < start_date) """
    results = euromil.results(date(2018, 10, 18), date(2018, 10, 20))

    assert len(results) == 1
    assert results[0].n1 == 1
    assert results[0].star1 == 3


def test_euromil_draw_dates(euromil):
    """ test draw_dates method  """
    assert date(2018, 10, 19) in euromil.draw_dates()
    assert date(2011, 6, 3) in euromil.draw_dates(
        date(2011, 1, 1), date(2011, 12, 31)
    )
    assert date(2013, 11, 15) in euromil.draw_dates(
        date(2013, 10, 30), date(2013, 11, 15)
    )
