""" Unit tests for Euromil.py """
from datetime import date
from pyeuromil import euro_results, Plays, Grid, EuroPlay
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


def test_euromil_game_summary():
    """ game_summary tests """
    summary = Plays._game_summary(
        Grid([1, 2, 3, 4, 5], [1, 2]),
        euro_results(date(2018, 10, 23), date(2018, 10, 23))[0],
    )

    assert summary["date"] == date(2018, 10, 23)
    assert summary["numbers"] == [1, 2, 5]
    assert summary["stars"] == [2]
    assert summary["ranking"] == 9
    assert summary["ranking_star_plus"] == 6


def test_euromil_play_summary_one_date():
    """ play_summary tests only 1 date """
    play = EuroPlay(
        Grid([1, 2, 3, 4, 5], [1, 2]),
        date(2018, 10, 23),
        date(2018, 10, 23),
        True,
        True,
    )

    summary = Plays.play_summary(play)[0]

    assert summary["date"] == date(2018, 10, 23)
    assert summary["numbers"] == [1, 2, 5]
    assert summary["stars"] == [2]
    assert summary["ranking"] == 9
    assert summary["ranking_star_plus"] == 6


def test_euromil_play_summary_multiple_dates():
    """ play_summary tests only 1 date """
    play = EuroPlay(
        Grid([1, 2, 3, 4, 5], [1, 2]),
        date(2018, 10, 16),
        date(2018, 10, 23),
        True,
        False,
    )
    summary = Plays.play_summary(play)

    assert len(summary) == 2

    summary0 = summary[0]
    assert summary0["date"] == date(2018, 10, 23)
    assert summary0["numbers"] == [1, 2, 5]
    assert summary0["stars"] == [2]
    assert summary0["ranking"] == 9
    assert summary0["ranking_star_plus"] == 6

    summary1 = summary[1]
    assert summary1["date"] == date(2018, 10, 16)
    assert summary1["numbers"] == []
    assert summary1["stars"] == [1]
    assert summary1["ranking"] == 0
    assert summary1["ranking_star_plus"] == 10
