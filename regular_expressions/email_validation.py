import re

emails = [
    "rahul@gmail.com",
    "john.smith@yahoo.com",
    "abc123@company.in",
    "rahul@gmail",
    "john@.com",
    "@gmail.com",
    "john gmail.com"
]

for email in emails:
    match= re.fullmatch(r'[a-zA-Z0-9\.]+@[a-z]+\.[a-z]+', email)
    if match is not None:
        print(f'{email} is valid')
