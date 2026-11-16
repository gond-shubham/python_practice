import re

text = "EMP12345 active EMP67890 inactive EMP11111 active"


match=re.findall(r'EMP\d{5}(?=\sactive)', text)

match1=re.finditer(r'EMP\d{5} active', text)

print(match)

for match in match1:
    m=re.findall(r'^EMP\d{5}', match.group())
    print(m)

