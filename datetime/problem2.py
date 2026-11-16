import datetime
records = [
    ("R101", "01-08-2026"),
    ("R102", "10-08-2026"),
    ("R103", "15-08-2026"),
    ("R104", "20-08-2026")
]


today_date=datetime.date.today()

for record in records:
    record_date=datetime.date.strptime(record[1], "%d-%m-%Y")
    output=today_date-record_date
    print(record[0],output.days)

