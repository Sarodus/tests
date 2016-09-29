import datetime
from dateutil import rrule

hours_ago = 48
now = datetime.datetime.now()
cur_hour = now.replace(minute=0, second=0, microsecond=0)
date_from = cur_hour - datetime.timedelta(hours=hours_ago)

print dir(rrule)

print 'HOURLY'

for dt in rrule.rrule(rrule.HOURLY, dtstart=date_from, until=now):
    print dt

print 'DAILY'

for dt in rrule.rrule(rrule.DAILY, dtstart=date_from, until=now):
    print dt
