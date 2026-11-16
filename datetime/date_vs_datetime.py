from datetime import date, datetime

d=date(2025, 12, 15)

print(d)
print(d.year)
print(d.month)
print(d.day)

present_date=date.today()

print(present_date)

dt=datetime(2025, 12, 15, 14, 30, 15, 1600)

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.second)
print(dt.microsecond)
print(dt.date())
print(dt.time())

print(datetime.now())
print(dt.today())