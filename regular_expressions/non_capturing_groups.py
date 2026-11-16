import re


text = "Mr. Rahul, Ms. Priya, Mr. Amit, Ms. Neha"

match= re.findall(r'(?<=Mr. )[A-Za-z]+|(?<=Ms. )[A-Za-z]+', text)

print(match)
