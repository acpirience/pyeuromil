""" constants and definition used by the classes """
from collections import namedtuple
from datetime import date

Euro_result = namedtuple("Result", ["date", "n1", "n2", "n3", "n4", "n5", "star1", "star2"])
EURO_MIN_DATE = date(2011, 5, 10)
EURO_MAX_DATE = date(2018, 10, 19)
