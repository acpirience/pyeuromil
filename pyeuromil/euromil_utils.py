""" constants and definition used by the classes """
from datetime import datetime, date
from collections import namedtuple
import pkg_resources


EuroResult = namedtuple("Result", ["date", "numbers", "stars"])
""" A result of the Euromillions, contains numbers, starts
and the date of the draw
"""


EuroPlay = namedtuple("Play", ["grid", "start", "end", "tuesday", "friday"])
""" A play of the Euromillions, contains a grid, a start date,
an end date and if the grid was played on tuesdays of fridays
"""


def _max_date_from_data():
    """ A function that look for the latest draw in the data folder """
    max_date = date(2018, 12, 28)
    year = datetime.now().date().year
    resource_package = __name__
    resource_path = "/".join(("data", f"{year}.txt"))
    with pkg_resources.resource_stream(resource_package, resource_path) as data:
        data.readline()
        line = data.readline().strip().decode("utf-8").split(" ")
        if line[0]:
            max_date = datetime.strptime(line[0], "%d/%m/%Y").date()

    return max_date


EURO_MIN_DATE = date(2011, 5, 10)
EURO_MAX_DATE = _max_date_from_data()
EURO_YEAR_STORAGE = [str(x) for x in range(EURO_MIN_DATE.year, EURO_MAX_DATE.year + 1)]

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
