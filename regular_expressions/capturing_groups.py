import re

text = "Employee: Rahul, ID: EMP12345, Department: Data Science"


match= re.search(r'Employee: (?P<name>[A-Za-z]+), ID: (?P<ID>EMP\d{5})', text)

print(match)

print(match.group())
print(match.groups())
print(match.group("name"))
print(match.group("ID"))


text1="Date: 20-08-2026"

match1=re.search(r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})', text1)

print(match1.groups())
print(match1.groupdict())