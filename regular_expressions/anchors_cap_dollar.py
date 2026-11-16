import re

text = "EMP12345"

texts = [
    "EMP12345",
    "XEMP12345",
    "EMP123456",
    "EMP12345XYZ",
    "EMP1234"
]

for text in texts:
    match=re.fullmatch(r'EMP\d{5}', text)

    if match is None:
        print("no match")
    else:
        print('match')


for text in texts:
    match = re.search(r'^EMP\d{5}$', text)

    if match is None:
        print("no match")
    else:
        print('match')