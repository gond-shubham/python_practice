import re

text= "apple,banana;orange mango"

pattern=re.split(r',|;|\s', text)

print(pattern)

for part in pattern:
    print(part)