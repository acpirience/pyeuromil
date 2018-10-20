""" Unit tests for Euromil.py """
from pyeuromil import Game
import pytest


def test_euromil_repr():
    """ __repr__ test"""
    test_game = Game(list(range(1, 6)), list(range(1, 3)))
    assert str(test_game) == "Game(Numbers:[1, 2, 3, 4, 5], Stars:[1, 2])"


def test_euromil_game_init_ko_basic():
    """ __init__ test Ko wrong params """
    with pytest.raises(ValueError):
        test_game = Game("", [])

    with pytest.raises(ValueError):
        test_game = Game([], "")


def test_euromil_game_init_ko_number_of_values():
    """ __init__ test Ko wrong number of values """
    with pytest.raises(ValueError):
        test_game = Game(list(range(1, 12)), [1, 2])
        assert test_game == None

    with pytest.raises(ValueError):
        test_game = Game(list(range(1, 11)), list(range(1, 14)))
        assert test_game == None


def test_euromil_game_init_ko_type_of_values():
    """ __init__ test Ko wrong number of values """
    with pytest.raises(ValueError):
        test_game = Game(list(range(1, 11)), ["1", "2"])
        assert test_game == None

    with pytest.raises(ValueError):
        test_game = Game([str(x) for x in range(1, 5)], [1, 2])
        assert test_game == None


def test_euromil_game_init_ko_outofbounds_of_values():
    """ __init__ test Ko out of bonds values """
    with pytest.raises(ValueError):
        test_game = Game(list(range(45, 55)), [1, 2])
        assert test_game == None

    with pytest.raises(ValueError):
        test_game = Game(list(range(1, 6)), [1, 13])
        assert test_game == None


def test_euromil_game_init_ko_duplicates():
    """ __init__ test Ko out of bonds values """
    with pytest.raises(ValueError):
        test_game = Game([1, 1, 2, 3, 4], [1, 2])
        assert test_game == None

    with pytest.raises(ValueError):
        test_game = Game(list(range(1, 6)), [2, 2, 3])
        assert test_game == None


def test_euromil_game_init_ok_basic():
    """ __init__ test Ok simple cases """
    test_game = Game(list(range(1, 6)), list(range(1, 3)))
    assert test_game.numbers == [1, 2, 3, 4, 5]
    assert test_game.stars == [1, 2]

    test_game = Game(list(range(21, 31)), list(range(1, 12)))
    assert test_game.numbers == [x for x in range(21, 31)]
    assert test_game.stars == [x for x in range(1, 12)]
