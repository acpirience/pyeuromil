""" Unit tests for Euromil.py """
from datetime import date
from pyeuromil import Plays, Grid, EuroPlay
import pytest


@pytest.fixture()
def play():
    return Plays()


def test_euromil_play_dunder(play):
    """ dunder methods test test"""
    # test init
    assert play.plays_list == []

    # bool
    assert not play

    # test len
    assert len(play) == 0
    play.append(
        Grid([1, 2, 3, 4, 5], [1, 2]),
        start=date(2018, 1, 1),
        end=date(2018, 1, 1),
        friday=True,
    )
    assert len(play) == 1

    # test repr
    assert (
        str(play)
        == "Plays(1 play(s): [Play(grid=Grid(Numbers:[1, 2, 3, 4, 5], Stars:[1, 2], Star Plus:False), start=datetime.date(2018, 1, 1), end=datetime.date(2018, 1, 1), tuesday=False, friday=True)])"
    )

    # bool
    assert play

def test_euromil_play_iter(play):
    play.append(
        Grid([1, 2, 3, 4, 5], [1, 2]),
        start=date(2018, 1, 1),
        end=date(2018, 1, 1),
        friday=True,
    )
    play.append(
        Grid([11, 12, 13, 14, 15], [11, 12]),
        start=date(2018, 1, 1),
        end=date(2018, 1, 1),
        friday=True,
    )

    nb = 0
    for a_play in play:
        assert isinstance(a_play, EuroPlay)
        nb += 1

    assert nb == 2



def test_euromil_play_append_ko(play):
    """ append ko because of dates """
    with pytest.raises(ValueError):
        play.append(None)

    with pytest.raises(ValueError):
        play.append(Grid([1, 2, 3, 4, 5], [1, 2]), start="", end=date(2018, 1, 1))

    with pytest.raises(ValueError):
        play.append(Grid([1, 2, 3, 4, 5], [1, 2]), start=date(2018, 1, 1), end="")


def test_euromil_play_append_ok(play):
    """ append ok """
    play.append(
        Grid([1, 2, 3, 4, 5], [1, 2]),
        start=date(2018, 1, 1),
        end=date(2018, 1, 1),
        friday=True,
    )

    assert play.plays_list[0].grid.stars == [1, 2]
    assert play.plays_list[0].start == date(2018, 1, 1)
    assert play.plays_list[0].end == date(2018, 1, 1)
    assert not play.plays_list[0].tuesday
    assert play.plays_list[0].friday


def test_euromil_play_ranking_ko():
    """ ranking ko test """
    with pytest.raises(ValueError):
        _, _ = Plays.ranking("", [])


def test_euromil_play_ranking_ok():
    """ ranking various passing tests """
    # nothing won
    normal, stars_plus = Plays.ranking([], [])
    assert normal == 0
    assert stars_plus == 0

    # rank 13 normal win
    normal, stars_plus = Plays.ranking([1, 2], [])
    assert normal == 13
    assert stars_plus == 0

    # rank 6 normal win and rank 4 Star Plus win
    normal, stars_plus = Plays.ranking([1, 2, 3], [1, 2])
    assert normal == 6
    assert stars_plus == 4

    # rank 1 normal win and rank 1 Star Plus win
    normal, stars_plus = Plays.ranking([1, 2, 3, 4, 5], [1, 2])
    assert normal == 1
    assert stars_plus == 1
