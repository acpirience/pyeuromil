""" A python library to check and analyse Euromillions results """
import pkg_resources


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

            for line in data.readlines():
                line = line.strip().decode("utf-8").split(" ")
                if line[0] != "date":
                    self._storage[key][line[0]] = line[1:]


if __name__ == "__main__":
    pass
