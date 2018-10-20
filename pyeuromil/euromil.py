""" A python library to check and analyse Euromillions results """
from datetime import datetime, date
import pkg_resources
from .euromil_helper import EuroResult, EURO_MIN_DATE, EURO_MAX_DATE


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
                result = line.strip().decode("utf-8").split(" ")
                for index, value in enumerate(result):
                    if index > 0:
                        result[index] = int(value)

                result_date = datetime.strptime(result[0], "%d/%m/%Y").date()
                result[0] = result_date
                result_stored = EuroResult(*result)
                self._storage[key][str(result_date)] = result_stored

    def results(self, start_date=None, end_date=None):
        """ get a result list from an interval """
        results = []

        if start_date is None:
            start_date = EURO_MIN_DATE

        if end_date is None:
            end_date = EURO_MAX_DATE

        if not isinstance(start_date, date):
            raise ValueError("If provided, start_date must be a date object")
        if not isinstance(end_date, date):
            raise ValueError("If provided, end_date must be a date object")

        for year in range(start_date.year, end_date.year + 1):
            # lazy load data values if not already loaded in memory
            if str(year) not in self._storage:
                self._load_data(str(year))

            for key in self._storage[str(year)]:
                result = self._storage[str(year)][key]
                if (result.date >= start_date) and (result.date <= end_date):
                    results.append(result)

        return results

    def draw_dates(self, start_date=None, end_date=None):
        """ list the draw for a given year / month """
        draws = []
        for result in self.results(start_date, end_date):
            draws.append(result.date)

        return draws
