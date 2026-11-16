import re

text = "My employee ID is EMP12345"

pattern=re.search(r'EMP\d{5}', text, flags=0)

print(pattern)
print(pattern.group(0))

