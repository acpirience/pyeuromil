""" Unit tests for euromil.py """
from datetime import date
import pytest
from pyeuromil import euro_results, euro_draw_dates, euro_stats


def test_euromil_results_year_not_exist():
    """ results of year test (year does not exists) """
    with pytest.raises(ValueError):
        results = euro_results("abcd")
        assert results is None
        results = euro_results(1920)
        assert results is None
        results = euro_results(2999)
        assert results is None

def test_euromil_results_invalid_date():
    """ results method (invalid date) """
    with pytest.raises(ValueError):
        results = euro_results("111")
        assert results is None

    with pytest.raises(ValueError):
        results = euro_results(date(2011, 1, 1), "111")
        assert results is None


def test_euromil_results_no_param():
    """ results method (no param) """
    results = euro_results()

    assert results[0].date.year == 2011
    assert results[-1].date.year == 2021


def test_euromil_results_start_date_only():
    """ results method (start_date only) """
    results = euro_results(date(2012, 12, 12))

    assert results[0].date == date(2012, 12, 28)
    assert results[-1].date > date(2018, 1, 1)


def test_euromil_results_both_dates_empty():
    """ results method (both dates, no results) """
    results = euro_results(date(2012, 12, 12), date(2012, 12, 13))

    assert results == []


def test_euromil_results_both_dates_wrong_order():
    """ results method (end_date < start_date) """
    results = euro_results(date(2018, 12, 12), date(2011, 12, 13))

    assert results == []


def test_euromil_results_both_dates_one_result():
    """ results method (end_date < start_date) """
    results = euro_results(date(2018, 10, 18), date(2018, 10, 20))

    assert len(results) == 1
    assert results[0].numbers[0] == 1
    assert results[0].stars[0] == 3


def test_euromil_draw_dates():
    """ test draw_dates method  """
    assert date(2018, 10, 19) in euro_draw_dates()
    assert date(2011, 6, 3) in euro_draw_dates(date(2011, 1, 1), date(2011, 12, 31))
    assert date(2013, 11, 15) in euro_draw_dates(date(2013, 10, 30), date(2013, 11, 15))


def test_euromil_stats():
    """  test euro_stats method """
    stats = euro_stats(date(2017, 10, 27), date(2018, 10, 27))
    assert (stats["st4"]) == 25
    assert (stats["15"]) == 17
