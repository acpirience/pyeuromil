""" Stores plays and is used to validate if a game was a win or a loose """
from collections import namedtuple
from datetime import date


EuroPlay = namedtuple("Play", ["game", "start", "end", "tuesday", "friday"])


class Plays:
    """ Stores plays and is used to validate if a game was a win or a loose """

    def __init__(self):
        self.game_list = []

    def __len__(self):
        return len(self.game_list)

    def __repr__(self):
        return f"{self.__class__.__name__}({len(self)} play(s): {self.game_list})"

    def append(self, game, *, start=None, end=None, tuesday=False, friday=False):
        """ Add a new game + date of plays """
        if not isinstance(game, Game):
            raise ValueError("Expecting a Game object")

        if not isinstance(start, date) or not isinstance(end, date):
            raise ValueError("Start and end date are mandatory and be date objects")

        self.game_list.append(EuroPlay(game, start, end, tuesday, friday))


class Game:
    """ Stores a unitary game """

    def __init__(self, numbers, stars, star_plus=False):
        if not isinstance(numbers, list) or not isinstance(stars, list):
            raise ValueError("Expecting list of numbers and list of stars")

        status, message = Game.check_numbers(numbers, stars)
        if not status:
            raise ValueError(message)

        self.numbers = numbers
        self.stars = stars
        self.start_plus = star_plus

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(Numbers:{self.numbers},"
            + f" Stars:{self.stars}, Star Plus:{self.start_plus})"
        )

    @staticmethod
    def check_numbers(numbers, stars):
        """ check if parameters for the game are corrects """
        if len(numbers) < 5 or len(numbers) > 10:
            return False, "Expecting 5 to 10 numbers"

        if len(stars) < 2 or len(stars) > 12:
            return False, "Expecting 2 to 12 stars"

        if len(set(numbers)) != len(numbers) or len(set(stars)) != len(stars):
            return False, "Duplicates are forbidden"

        for value in numbers:
            if not isinstance(value, int) or value < 1 or value > 50:
                return False, "Numbers should be int between 1 and 50"

        for value in stars:
            if not isinstance(value, int) or value < 1 or value > 12:
                return False, "Stars should be int between 1 and 12"

        return True, ""
