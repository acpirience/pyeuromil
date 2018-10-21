""" Unit tests for Euromil.py """
from datetime import date
from pyeuromil import Plays, Game
import pytest


@pytest.fixture()
def play():
    return Plays()


def test_euromil_dunder(play):
    """ dunder methods test test"""
    # test init
    assert play.game_list == []

    # test len
    assert len(play) == 0
    play.append(
        Game([1, 2, 3, 4, 5], [1, 2]),
        start=date(2018, 1, 1),
        end=date(2018, 1, 1),
        friday=True,
    )
    assert len(play) == 1

    # test repr
    assert (
        str(play)
        == "Plays(1 play(s): [Play(game=Game(Numbers:[1, 2, 3, 4, 5], Stars:[1, 2]), start=datetime.date(2018, 1, 1), end=datetime.date(2018, 1, 1), tuesday=False, friday=True)])"
    )


def test_euromil_append_ko(play):
    """ append ko because of dates """
    with pytest.raises(ValueError):
        play.append(None)

    with pytest.raises(ValueError):
        play.append(Game([1, 2, 3, 4, 5], [1, 2]), start="", end=date(2018, 1, 1))

    with pytest.raises(ValueError):
        play.append(Game([1, 2, 3, 4, 5], [1, 2]), start=date(2018, 1, 1), end="")


def test_euromil_append_ok(play):
    """ append ok """
    play.append(
        Game([1, 2, 3, 4, 5], [1, 2]),
        start=date(2018, 1, 1),
        end=date(2018, 1, 1),
        friday=True,
    )

    assert play.game_list[0].game.stars == [1, 2]
    assert play.game_list[0].start == date(2018, 1, 1)
    assert play.game_list[0].end == date(2018, 1, 1)
    assert not play.game_list[0].tuesday
    assert play.game_list[0].friday
