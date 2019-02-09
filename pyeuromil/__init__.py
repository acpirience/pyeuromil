"""pyeuromil - A python library to check and analyse Euromillions results"""


__version__ = "0.2.20190208"
__author__ = "Acpirience <acpirience@gmail.com>"
__all__ = []

from .euromil import euro_results, euro_draw_dates, euro_stats
from .euromil_play import Plays, Grid
from .euromil_utils import EuroResult, EuroPlay
