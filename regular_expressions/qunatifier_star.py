import re

text = "A1 B12 C123 D"

matches= re.findall(r'\d*', text)

print(matches)