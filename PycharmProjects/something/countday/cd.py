#!/usr/bin/env python3
from datetime import date
from datetime import datetime
from datetime import timedelta

day = date.today()
print(day)
print(type(day))
now = datetime.now()
print(now)
print(type(now))
delta = timedelta(days=5)
n_days_after = now + delta
n_days_before = now - delta
print(n_days_after.strftime('%Y-%m-%d'))
print(n_days_before.strftime('%Y-%m-%d'))