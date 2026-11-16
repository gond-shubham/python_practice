from datetime import datetime, timedelta

dt= datetime(2025, 12, 15)

new=dt+timedelta(days=20)

new1=dt-timedelta(days=10)

new3=dt+timedelta(days=2, hours=5)

print(new)
print(new1)
print(new3)


dt1= datetime(2027, 12, 15)

dt3=dt1-dt
print(dt3)
print(type(dt3))

