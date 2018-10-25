""" Unit tests for Euromil.py """
from datetime import date
from pyeuromil import Grid, EuroResult
import pytest


def test_euromil_repr():
    """ __repr__ test"""
    test_grid = Grid(list(range(1, 6)), list(range(1, 3)))
    assert (
        str(test_grid) == "Grid(Numbers:[1, 2, 3, 4, 5], Stars:[1, 2], Star Plus:False)"
    )


def test_euromil_grid_init_ko_basic():
    """ __init__ test Ko wrong params """
    with pytest.raises(ValueError):
        test_grid = Grid("", [])

    with pytest.raises(ValueError):
        test_grid = Grid([], "")


def test_euromil_grid_init_ko_number_of_values():
    """ __init__ test Ko wrong number of values """
    with pytest.raises(ValueError):
        _ = Grid(list(range(1, 12)), [1, 2])

    with pytest.raises(ValueError):
        _ = Grid(list(range(1, 11)), list(range(1, 14)))


def test_euromil_grid_init_ko_type_of_values():
    """ __init__ test Ko wrong number of values """
    with pytest.raises(ValueError):
        _ = Grid(list(range(1, 11)), ["1", "2"])

    with pytest.raises(ValueError):
        _ = Grid([str(x) for x in range(1, 5)], [1, 2])


def test_euromil_grid_init_ko_outofbounds_of_values():
    """ __init__ test Ko out of bonds values """
    with pytest.raises(ValueError):
        _ = Grid(list(range(45, 55)), [1, 2])

    with pytest.raises(ValueError):
        _ = Grid(list(range(1, 6)), [1, 13])


def test_euromil_grid_init_ko_duplicates():
    """ __init__ test Ko out of bonds values """
    with pytest.raises(ValueError):
        _ = Grid([1, 1, 2, 3, 4], [1, 2])

    with pytest.raises(ValueError):
        _ = Grid(list(range(1, 6)), [2, 2, 3])


def test_euromil_grid_init_ok_basic():
    """ __init__ test Ok simple cases """
    test_grid = Grid(list(range(1, 6)), list(range(1, 3)), star_plus=True)
    assert test_grid.numbers == [1, 2, 3, 4, 5]
    assert test_grid.stars == [1, 2]
    assert test_grid.start_plus

    test_grid = Grid(list(range(21, 31)), list(range(1, 12)))
    assert test_grid.numbers == [x for x in range(21, 31)]
    assert test_grid.stars == [x for x in range(1, 12)]
    assert not test_grid.start_plus


def test_euromil_grid_evaluate_grid_ko():
    """ grid_evaluate ko """
    with pytest.raises(ValueError):
        test_grid = Grid(list(range(1, 6)), list(range(1, 3)), star_plus=True)
        _, _ = test_grid.evaluate_grid("")


def test_euromil_grid_evaluate_grid_ok_results():
    """ grid_evaluate ok with results"""
    result = EuroResult(date(2018, 1, 1), [1, 2, 3, 4, 5], [1, 2])
    test_grid = Grid(list(range(1, 6)), list(range(1, 3)), star_plus=True)
    test_numbers, test_stars = test_grid.evaluate_grid(result)

    assert test_numbers == [1, 2, 3, 4, 5]
    assert test_stars == [1, 2]

    test_grid = Grid(list(range(5, 13)), list(range(2, 4)), star_plus=True)
    test_numbers, test_stars = test_grid.evaluate_grid(result)

    assert test_numbers == [5]
    assert test_stars == [2]


def test_euromil_grid_evaluate_grid_ok_no_results():
    """ grid_evaluate ok without result"""
    result = EuroResult(date(2018, 1, 1), [1, 2, 3, 4, 5], [1, 2])
    test_grid = Grid(list(range(11, 16)), list(range(10, 13)), star_plus=False)

    test_numbers, test_stars = test_grid.evaluate_grid(result)

    assert test_numbers == []
    assert test_stars == []
