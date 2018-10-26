""" Euromy_play: Stores Euromillions plays and give summary of wins """
from datetime import date
from .euromil import euro_results
from .euromil_utils import EuroResult, EuroPlay, EURO_RANKS_NORMAL, EURO_RANKS_STAR_PLUS


class Plays:
    """ Stores plays and is used to validate if plays are wins or looses """

    def __init__(self):
        self.plays_list = []

    def __len__(self):
        return len(self.plays_list)

    def __bool__(self):
        return bool(self.plays_list)

    def __repr__(self):
        return f"{self.__class__.__name__}({len(self)} play(s): {self.plays_list})"

    def __iter__(self):
        for play in self.plays_list:
            yield play

    def append(self, grid, *, start=None, end=None, tuesday=False, friday=False):
        """ Adds a new grid and dates of play to Plays

        :param grid: The grid played
        :type start_date: Grid
        :param start_date: start date
        :type start_date: date
        :param end_date: end_date
        :type end_date: date
        :param tuesday: Indicates in the grid is played on tuedays
        :type tuesday: date
        :param friday: Indicates in the grid is played on fridays
        :type friday: date
        :raises: ValueError
        """
        if not isinstance(grid, Grid):
            raise ValueError("Expecting a type Grid")

        if not isinstance(start, date) or not isinstance(end, date):
            raise ValueError("Start and end date are mandatory and be of type date")

        self.plays_list.append(EuroPlay(grid, start, end, tuesday, friday))

    @staticmethod
    def ranking(numbers, stars):
        """ returns ranking for a normal game and ranking for a Star Plus game
        Ranking is 0 if nothing was won

        :param numbers: The list of numbers played
        :type numbers: list of int
        :param stars: The list of stars played
        :type stars: list of int
        :returns: normal ranking and Star Plus ranking
        :rtype: int, int
        :raises: ValueError
        """
        if not isinstance(numbers, list) or not isinstance(stars, list):
            raise ValueError("Expecting numbers and stars as type list")

        ranking_normal = EURO_RANKS_NORMAL.get(f"{len(numbers)}-{len(stars)}", 0)
        ranking_star_plus = EURO_RANKS_STAR_PLUS.get(f"{len(numbers)}-{len(stars)}", 0)

        return ranking_normal, ranking_star_plus

    @staticmethod
    def _game_summary(grid, result, only_wins=False):
        """ returns summary of numbers and win rankings for a game """
        numbers_won, stars_won = grid.evaluate_grid(result)
        ranking_normal, ranking_star_plus = Plays.ranking(numbers_won, stars_won)
        if not only_wins or (ranking_normal + ranking_star_plus):
            return {
                "date": result.date,
                "numbers": numbers_won,
                "stars": stars_won,
                "ranking": ranking_normal,
                "ranking_star_plus": ranking_star_plus,
            }
        return None

    @staticmethod
    def play_summary(play, only_wins=False):
        """ returns the summary of numbers and win rankings for a play (ensemble of games)

        :param play: The play the summary will be based upon
        :type play: play
        :param only_wins: show only winning games in summary
        :type only_wins: bool
        :returns: dictionary with date, numbers, stars, ranking and ranking_star_plus keys
        :rtype: dict
        """
        summary = []
        results = euro_results(play.start, play.end)
        for result in results:
            result_day = result.date.weekday()
            if result_day == 1 and play.tuesday or result_day == 4 and play.friday:
                game_summary = Plays._game_summary(play.grid, result, only_wins)
                if game_summary:
                    summary.append(game_summary)
        return summary


class Grid:
    """ contains a grid played at an Euromillions game """

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
        """ check if parameters for the grid are corrects

            :param numbers: The list of numbers played
            :type numbers: list of int
            :param stars: The list of stars played
            :type stars: list of int
            :returns: check status and error message is status is ko
            :rtype: bool, string
            """
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
        """ returns the list of numbers and stars both in a Grid and a result

            :param result: The result we want to check the grid against
            :type result: EuroResult
            :returns: the list of the numbers in the grid and the result and
                the list of the stars in the grid and the result
            :rtype: list of int, list of int
            """
        if not isinstance(result, EuroResult):
            raise ValueError("Type EuroResult is expected")

        numbers_won = []
        stars_won = []

        for number in self.numbers:
            if number in result.numbers:
                numbers_won.append(number)

        for number in self.stars:
            if number in result.stars:
                stars_won.append(number)

        return (numbers_won, stars_won)
