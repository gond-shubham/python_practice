from datetime import datetime

dt = datetime(2025, 12, 15, 14, 30, 45)

result = dt.strftime("%d-%m-%Y %H:%M:%S")

print(result)
print(type(result))

t1="25-08-2025"
t2="2026/01/15"
t3="2026-03-20 18:45:30"

print(datetime.strptime(t1, "%d-%m-%Y"))
print(datetime.strptime(t2, "%Y/%m/%d"))
print(datetime.strptime(t3, "%Y-%m-%d %H:%M:%S"))
