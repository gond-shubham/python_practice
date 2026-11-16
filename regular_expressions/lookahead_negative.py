import re

text = "EMP12345 active EMP67890 inactive EMP11111 active EMP22222 blocked"

#printing the id's which are not blocked.

match = re.findall(r'EMP\d{5}(?!\sblocked)', text)

print(match)