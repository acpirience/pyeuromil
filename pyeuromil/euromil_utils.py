""" constants and definition used by the classes """
from datetime import date
from collections import namedtuple


EuroResult = namedtuple(
    "Result", ["date", "n1", "n2", "n3", "n4", "n5", "star1", "star2"]
)
EuroPlay = namedtuple("Play", ["game", "start", "end", "tuesday", "friday"])

EURO_MIN_DATE = date(2011, 5, 10)
EURO_MAX_DATE = date(2018, 10, 19)
