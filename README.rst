pyeuromil
=========

|PyPI-Status| |Py-Versions| |Git-RepoSize|

|Travis-Status| |Last-Commit| |Codecov|

A python library to check and analyse Euromillions results

------------------------------------------

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


.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. |PyPI-Status| image:: https://img.shields.io/pypi/v/pyeuromil.svg
    :target: https://pypi.python.org/pypi/pyeuromil
.. |Py-Versions| image:: https://img.shields.io/pypi/pyversions/pyeuromil.svg
   :target: https://www.python.org/downloads/
.. |Git-RepoSize| image:: https://img.shields.io/github/repo-size/acpirience/pyeuromil.svg
   :target: https://github.com/acpirience/pyeuromil
.. |Travis-Status| image:: https://travis-ci.org/acpirience/pyeuromil.png
   :target: https://travis-ci.org/acpirience/pyeuromil
.. |Last-Commit| image:: https://img.shields.io/github/last-commit/acpirience/pyeuromil.svg
   :target: https://github.com/acpirience/pyeuromil/commits/master
.. |Codecov| image:: https://codecov.io/gh/acpirience/pyeuromil/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/acpirience/pyeuromil
