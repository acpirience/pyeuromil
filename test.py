from pyeuromil import euro_stats
from datetime import date

stats = euro_stats(date(2017,10,27), date(2018,10,27))

for key in sorted(stats, key=lambda x: stats[x], reverse=True):
    print(f"{key:>4} => {stats[key]}")