""" A python library to check and analyse Euromillions results """
import pkg_resources

class Euromil:
    """ Main class for pyeuromil"""
    def __init__(self):
        resource_package = __name__
        resource_path = '/'.join(('data', '2011.txt'))
        with pkg_resources.resource_stream(resource_package, resource_path) as data:
            self.test = data.readline().strip().decode("utf-8")

if __name__ == "__main__":
    pass
