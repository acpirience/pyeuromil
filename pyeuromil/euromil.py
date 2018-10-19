""" A python library to check and analyse Euromillions results """
from collections import namedtuple
import pkg_resources


Result = namedtuple("Result", ["date", "n1", "n2", "n3", "n4", "n5", "star1", "star2"])
MIN_YEAR = 2011
MAX_YEAR = 2018


class Euromil:
    """ Main class for pyeuromil"""

    def __init__(self):
        self._storage = {}

    def _load_data(self, year):
        """ Load data in storage per year """
        key = str(year)
        self._storage[key] = {}
        resource_package = __name__
        resource_path = "/".join(("data", key + ".txt"))

        with pkg_resources.resource_stream(resource_package, resource_path) as data:
            data.readline()
            for line in data.readlines():
                result = Result(*(line.strip().decode("utf-8").split(" ")))
                self._storage[key][result.date] = result

    def results(self, year, month=None, day=None):
        """ get a result list from a date """
        if isinstance(year, int) and year >= MIN_YEAR and year <= MAX_YEAR:
            # lazy load data values if not already loaded in memory
            if str(year) not in self._storage:
                self._load_data(year)

            if month is None and day is None:
                return self._storage[str(year)]

            if isinstance(month, int) and month >= 1 and month <= 12:
                if day is None:
                    month_result = {}
                    for result in self._storage[str(year)]:
                        if int(result[3:5]) == month:
                            month_result[result] = self._storage[str(year)][result]
                    return month_result

                if isinstance(day, int):
                    date = f"{day:02}/{month:02}/{year}"
                    if date in self._storage[str(year)]:
                        return self._storage[str(year)][date]
                ValueError(f"Day must be an int")

            ValueError(f"Month must be an int between 1 and 12")

        raise ValueError(f"Year must be an int between {MIN_YEAR} and {MAX_YEAR}")

    def dummy2(self):
        """ dummy method 2 """
        pass


if __name__ == "__main__":
    pass
