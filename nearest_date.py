import datetime

def nearest_date(dates, pivot):
  return min(dates, key=lambda x: abs(x - pivot))


dates = [datetime.datetime(2015, 10, 3, 14, 0), datetime.datetime(2015, 10, 17, 18, 30), datetime.datetime(2015, 10, 20, 18, 45), datetime.datetime(2015, 10, 25, 17, 15), datetime.datetime(2015, 10, 28, 19, 30), datetime.datetime(2015, 11, 4, 19, 45), datetime.datetime(2015, 11, 8, 15, 0)]
date = datetime.datetime(2015, 10, 23)

for d in dates:
    print abs(date - d)

print nearest_date(dates, date)
