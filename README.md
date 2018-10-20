
[![Latest PyPI version](https://img.shields.io/pypi/v/pyeuromil.svg)](https://pypi.python.org/pypi/pyeuromil)
[![Latest Travis CI build status](https://travis-ci.org/acpirience/pyeuromil.png)](https://travis-ci.org/acpirience/pyeuromil)
[![last commit](https://img.shields.io/github/last-commit/acpirience/pyeuromil.svg)](https://github.com/acpirience/pyeuromil/commits/master)
[![Compatibility list](https://img.shields.io/pypi/pyversions/pyeuromil.svg)](https://www.python.org/downloads/)
[![Repository size](https://img.shields.io/github/repo-size/acpirience/pyeuromil.svg)](https://github.com/acpirience/pyeuromil)

# pyeurmil

A python library to check and analyse Euromillions results

## Usage

```python
from pyeuromil import Euromil
from datetime import date

my_euromil = Euromil()
# September draws
for result in my_euromil.draw_dates(date(2018, 9, 1), date(2018, 9, 30)):
    print(result)
```
>2018-09-28  
2018-09-25  
2018-09-21  
2018-09-18  
2018-09-14  
2018-09-11  
2018-09-07  
2018-09-04
```python
from pyeuromil import Euromil
from datetime import date

my_euromil = Euromil()
# first week of october results
result_list = my_euromil.results(date(2018, 10, 1), date(2018, 10, 7))
for result in result_list:
    print(result)
```
>Result(date=datetime.date(2018, 10, 5), n1='08', n2='16', n3='24', n4='26', n5='35', star1='03', star2='11')  
Result(date=datetime.date(2018, 10, 2), n1='07', n2='17', n3='29', n4='37', n5='45', star1='03', star2='11')

## Installation

pip install pyeuromil

## Compatibility

python > 3.6

## Licence

MIT License (see LICENSE file)

# Authors

`pyeuromil` was written by `Acpirience <acpirience@gmail.com>`.
