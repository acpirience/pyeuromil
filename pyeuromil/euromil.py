""" A python library to check and analyse Euromillions results """
import os


class Euromil:
    """ Main class for pyeuromil"""
    def __init__(self):
        with open("pyeuromil/data/2011.txt", "r") as data:
            self.test = (data.readline()).strip()


if __name__ == "__main__":
    pass
