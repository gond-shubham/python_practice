import re

texts = [
    "EMP12345 ",
    "EMP67890959 is active",
    "Employee EMP11111",
    "EMP54321jjdj completed"
]


for text in texts:
    match = re.search(r'^EMP\d{5}(?!\S)', text)

    if match is not None:
        print(f'{text}--> match')
    else:
        print(f'{text}--> no match')