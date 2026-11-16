import re

text = "EMP12345 EMP67890 EMP11111"

pattern=re.finditer(r'EMP\d{5}', text)

print(pattern)

for match in pattern:
    print(match)
    print(match.group())
    print(match.span())
    print(match.start())
    print(match.end())
