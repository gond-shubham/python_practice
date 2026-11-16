import re

text = """
Today's date is 22-08-2026.
The project started on 15/07/2026.
Deadline: 30-09-2026.
"""


dates = re.findall(r'[0-9]{2}-[0-9]{2}-[0-9]{4}|[0-9]{2}/[0-9]{2}/[0-9]{4}', text)

print(dates)