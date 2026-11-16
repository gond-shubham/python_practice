import datetime
transactions = [
    ("T101", "15-08-2026", 5000),
    ("T102", "20-08-2026", 2500),
    ("T103", "05-08-2026", 7500),
    ("T104", "22-08-2026", 3000)
]

cutoff_date=datetime.date(2026, 8, 15)


for date in transactions:
    d=date[1]
    trans_date=datetime.date.strptime(d, "%d-%m-%Y")
    if trans_date>cutoff_date:
        print(date[0], date[2])