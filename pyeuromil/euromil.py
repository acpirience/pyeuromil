""" A python library to check and analyse Euromillions results """
from collections import namedtuple
from datetime import date
import pkg_resources


Result = namedtuple("Result", ["date", "n1", "n2", "n3", "n4", "n5", "star1", "star2"])
MIN_YEAR = 2011
MAX_YEAR = 2018


class Euromil:
    """ Main class for pyeuromil"""

    def __init__(self):
        self._storage = {}

    @staticmethod
    def year_is_valid(year):
        """  returns true is the year is a valid draw year """
        return isinstance(year, int) and year >= MIN_YEAR and year <= MAX_YEAR

    @staticmethod
    def month_is_valid(month):
        """  returns true is the month is valid """
        return isinstance(month, int) and month >= 1 and month <= 12

    def _load_data(self, year):
        """ Load data in storage per year """
        key = str(year)
        self._storage[key] = {}
        resource_package = __name__
        resource_path = "/".join(("data", key + ".txt"))

        with pkg_resources.resource_stream(resource_package, resource_path) as data:
            data.readline()
            for line in data.readlines():
                result = line.strip().decode("utf-8").split(" ")
                result_date = result[0]
                result[0] = date(
                    int(result_date[6:10]), int(result_date[3:5]), int(result_date[0:2])
                )
                result_stored = Result(*result)
                self._storage[key][result_date] = result_stored

    def results(self, year, month=None, day=None):
        """ get a result list from a date """
        if Euromil.year_is_valid(year):
            # lazy load data values if not already loaded in memory
            if str(year) not in self._storage:
                self._load_data(year)

            if month is None and day is None:
                return self._storage[str(year)]

            if Euromil.month_is_valid(month):
                if day is None:
                    month_result = {}
                    for result in self._storage[str(year)]:
                        if int(result[3:5]) == month:
                            month_result[result] = self._storage[str(year)][result]
                    return month_result

                if isinstance(day, int):
                    stored_date = f"{day:02}/{month:02}/{year}"
                    if stored_date in self._storage[str(year)]:
                        return self._storage[str(year)][stored_date]
                ValueError(f"Day must be an int")

            ValueError(f"Month must be an int between 1 and 12")

        raise ValueError(f"Year must be an int between {MIN_YEAR} and {MAX_YEAR}")

    def draw_dates(self, year, month=None):
        """ list the draw for a given year / month """
        draws = []
        for result in self.results(year, month):
            draws.append(self._storage[str(year)][result].date)

        return draws


if __name__ == "__main__":
    pass
