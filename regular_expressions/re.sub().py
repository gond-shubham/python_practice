import re

text= "My phone number is 987-654-3210"


operation=re.sub(r'\d+', '*', text)

operation1=re.sub(r'\d', '*', text)

print(operation)
print(operation1)