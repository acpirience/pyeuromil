""" A python library to check and analyse Euromillions results """
from datetime import datetime, date
import pkg_resources
from .euromil_utils import EuroResult, EURO_MIN_DATE, EURO_MAX_DATE

STORAGE = {}


def _load_data(year):
    """ Load data in storage per year """
    key = str(year)
    STORAGE[key] = {}
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
            result_stored = EuroResult(result_date, result[1:6], result[6:8])
            STORAGE[key][str(result_date)] = result_stored


def euro_results(start_date=None, end_date=None):
    """ get a result list from an interval """
    results = []

    if start_date is None:
        start_date = EURO_MIN_DATE

    if end_date is None:
        end_date = EURO_MAX_DATE

    if not isinstance(start_date, date):
        raise ValueError("If provided, start_date must be of type date")
    if not isinstance(end_date, date):
        raise ValueError("If provided, end_date must be of type date")

    for year in range(start_date.year, end_date.year + 1):
        # lazy load data values if not already loaded in memory
        if str(year) not in STORAGE:
            _load_data(str(year))

        for key in STORAGE[str(year)]:
            result = STORAGE[str(year)][key]
            if (result.date >= start_date) and (result.date <= end_date):
                results.append(result)

    return results


def euro_draw_dates(start_date=None, end_date=None):
    """ list the draw for a interval """
    draws = []
    for result in euro_results(start_date, end_date):
        draws.append(result.date)

    return draws
