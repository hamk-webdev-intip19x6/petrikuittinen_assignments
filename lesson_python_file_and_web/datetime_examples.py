import datetime
birth = datetime.date(1990, 12, 31)
now = datetime.date.today()
print("%d.%d.%d" % (now.day, now.month, now.year))
print(now.strftime("%d.%m.%Y. Month is %B."))
delta = now-birth
print(delta)
week_in_future = now + datetime.timedelta(days=7)
delta2 = week_in_future-now
print(delta2.days)
