.. Pyeuromil documentation master file, created by
   sphinx-quickstart on Fri Oct 26 06:59:22 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pyeuromil's documentation!
=====================================

Pyeuromil is a Python library to check and analyse Euromillions results

------------------------------------------

:ref:`genindex` | :ref:`modindex`


Usage
-----
.. code-block:: python

    import pyeuromil as em
    from datetime import date

    # List of draw dates of September 2018
    for result in em.euro_draw_dates(date(2018, 9, 1), date(2018, 9, 30)):
        print(result)

.. code-block:: text

    2018-09-28
    2018-09-25
    2018-09-21
    2018-09-18
    2018-09-14
    2018-09-11
    2018-09-07
    2018-09-04

.. code-block:: python

    import pyeuromil as em
    from datetime import date

    # first week of october 2018 results
    result_list = em.euro_results(date(2018, 10, 1), date(2018, 10, 7))
    for result in result_list:
        print(result)

.. code-block:: text

    Result(date=datetime.date(2018, 10, 5), numbers=[8, 16, 24, 26, 35], stars=[3, 11])
    Result(date=datetime.date(2018, 10, 2), numbers=[7, 17, 29, 37, 45], stars=[3, 11])

.. code-block:: python

    from pyeuromil import Plays, Grid
    from datetime import date
    import pprint

    pp = pprint.PrettyPrinter(indent=2)

    plays = Plays()
    game = Grid([15, 18, 32, 35, 40],[1, 7], star_plus=True)
    plays.append(game, start=date(2018,9,28), end=date(2018,10,30), tuesday=True, friday=True)

    for play in plays:
        pp.pprint(Plays.play_summary(play))

.. code-block:: text

    [ { 'date': datetime.date(2018, 10, 23),
        'numbers': [32],
        'ranking': 0,
        'ranking_star_plus': 0,
        'stars': []},
      { 'date': datetime.date(2018, 10, 19),
        'numbers': [],
        'ranking': 0,
        'ranking_star_plus': 0,
        'stars': []},
      { 'date': datetime.date(2018, 10, 16),
        'numbers': [15, 40],
        'ranking': 12,
        'ranking_star_plus': 9,
        'stars': [1]},
      { 'date': datetime.date(2018, 10, 12),
        'numbers': [],
        'ranking': 0,
        'ranking_star_plus': 0,
        'stars': []},
      { 'date': datetime.date(2018, 10, 9),
        'numbers': [],
        'ranking': 0,
        'ranking_star_plus': 0,
        'stars': []},
      { 'date': datetime.date(2018, 10, 5),
        'numbers': [35],
        'ranking': 0,
        'ranking_star_plus': 0,
        'stars': []},
      { 'date': datetime.date(2018, 10, 2),
        'numbers': [],
        'ranking': 0,
        'ranking_star_plus': 0,
        'stars': []},
      { 'date': datetime.date(2018, 9, 28),
        'numbers': [],
        'ranking': 0,
        'ranking_star_plus': 0,
        'stars': []}]

Installation
------------
Install and update using `pip`_:

.. code-block:: text

    pip install pyeuromil

Compatibility
-------------
python > 3.6

Licence
-------
MIT License (see LICENSE file)

Authors
-------
`pyeuromil` was written by `Acpirience <acpirience@gmail.com>`_.


------------------------------------------


.. toctree::
   :maxdepth: 2

   modules.rst


.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. |PyPI-Status| image:: https://img.shields.io/pypi/v/pyeuromil.svg
    :target: https://pypi.python.org/pypi/pyeuromil





