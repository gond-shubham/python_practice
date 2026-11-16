import re

text = "Products: A123, B45, C7890"

matches=re.finditer(r'\d+', text)

for match in matches:
    print(match)
    print(match.group())