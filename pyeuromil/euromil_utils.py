""" constants and definition used by the classes """
from datetime import date
from collections import namedtuple


EuroResult = namedtuple(
    "Result", ["date", "n1", "n2", "n3", "n4", "n5", "star1", "star2"]
)
EuroPlay = namedtuple("Play", ["grid", "start", "end", "tuesday", "friday"])

EURO_MIN_DATE = date(2011, 5, 10)
EURO_MAX_DATE = date(2018, 10, 19)

EURO_RANKS_NORMAL = {
    "5-2": 1,
    "5-1": 2,
    "5-0": 3,
    "4-2": 4,
    "4-1": 5,
    "3-2": 6,
    "4-0": 7,
    "2-2": 8,
    "3-1": 9,
    "3-0": 10,
    "1-2": 11,
    "2-1": 12,
    "2-0": 13,
}

EURO_RANKS_STAR_PLUS = {
    "5-2": 1,
    "5-1": 1,
    "4-2": 2,
    "4-1": 3,
    "3-2": 4,
    "2-2": 5,
    "3-1": 6,
    "1-2": 7,
    "0-2": 8,
    "2-1": 9,
    "0-1": 10,
}
