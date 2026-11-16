import re

text = "Employees: EMP12345, EMP67890, EMP11111"

pattern=re.findall(r'EMP\d{5}', text)

print(pattern)