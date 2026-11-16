import re

text = "Rahul    Sharma   is   a   Data   Scientist"

output=re.sub(r'\s+', ' ', text)

print(output)