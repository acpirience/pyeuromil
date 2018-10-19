
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

my_euromil = Euromil()    
for result in my_euromil.draw_dates(2018, 9):
	print(result) 
```
>2018-09-28 00:00:00  
2018-09-25 00:00:00  
2018-09-21 00:00:00  
2018-09-18 00:00:00  
2018-09-14 00:00:00  
2018-09-11 00:00:00  
2018-09-07 00:00:00  
2018-09-04 00:00:00  
```python
from pyeuromil import Euromil

my_euromil = Euromil()    
print(my_euromil.results(2018,9,28))
```
>Result(date=datetime.datetime(2018, 9, 28, 0, 0), n1='02', n2='04', n3='08', n4='27', n5='50', star1='02', star2='09')

## Installation

pip install pyeuromil

## Compatibility

python > 3.6

## Licence

MIT License (see LICENSE file)

# Authors

`pyeuromil` was written by `Acpirience <acpirience@gmail.com>`.
