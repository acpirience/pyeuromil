""" Stores plays and is used to validate if a game was a win or a loose """
from datetime import date
from .euromil_utils import EuroResult, EuroPlay, EURO_RANKS_NORMAL, EURO_RANKS_STAR_PLUS


class Plays:
    """ Stores plays and is used to validate if a game was a win or a loose """

    def __init__(self):
        self.plays_list = []

    def __len__(self):
        return len(self.plays_list)

    def __repr__(self):
        return f"{self.__class__.__name__}({len(self)} play(s): {self.plays_list})"

    def append(self, game, *, start=None, end=None, tuesday=False, friday=False):
        """ Add a new game + date of plays """
        if not isinstance(game, Grid):
            raise ValueError("Expecting a type Grid")

        if not isinstance(start, date) or not isinstance(end, date):
            raise ValueError("Start and end date are mandatory and be of type date")

        self.plays_list.append(EuroPlay(game, start, end, tuesday, friday))

    @staticmethod
    def ranking(numbers, stars):
        """
            returns ranking for a normal game and ranking for a Star Plus game
            Ranking is 0 if nothing was won
        """
        if not isinstance(numbers, list) or not isinstance(stars, list):
            raise ValueError("Expecting numbers and stars as type list")

        ranking_normal = EURO_RANKS_NORMAL.get(f"{len(numbers)}-{len(stars)}", 0)
        ranking_star_plus = EURO_RANKS_STAR_PLUS.get(f"{len(numbers)}-{len(stars)}", 0)

        return ranking_normal, ranking_star_plus


class Grid:
    """ Stores a unitary grid """

    def __init__(self, numbers, stars, star_plus=False):
        if not isinstance(numbers, list) or not isinstance(stars, list):
            raise ValueError("Expecting list of numbers and list of stars")

        status, message = Grid.check_numbers(numbers, stars)
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

    def evaluate_grid(self, result):
        """ returns the list of numbers and stars both in a Grid and a result """
        if not isinstance(result, EuroResult):
            raise ValueError("Type EuroResult is expected")

        numbers_won = []
        stars_won = []

        for number in self.numbers:
            if number in [result.n1, result.n2, result.n3, result.n4, result.n5]:
                numbers_won.append(number)

        for number in self.stars:
            if number in [result.star1, result.star2]:
                stars_won.append(number)

        return (numbers_won, stars_won)
