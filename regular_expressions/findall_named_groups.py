import re

text = "Employee: Rahul, ID: EMP12345, Department: Data Science"

match=re.findall(r'(?<=Employee: )[A-Za-z]+|(?<=ID: )EMP\d+|(?<=Department: )[A-Za-z ]+', text)

print(match)