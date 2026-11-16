import re


text = "Python 123 Data456 Science789"

match=re.findall(r'[0-9]', text)
match1=re.findall(r'[0-9]+', text)

print(match)
print(match1)
