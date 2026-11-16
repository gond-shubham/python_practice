import re

text1 = "EMP12345"
text2 = "EMP12345 is my employee ID"
text3 = "My employee ID is EMP12345"

pattern1=re.fullmatch(r'EMP\d{5}', text1)
pattern2=re.fullmatch(r'EMP\d{5}', text2)
pattern3=re.fullmatch(r'EMP\d{5}', text3)

print(pattern1)
print(pattern2)
print(pattern3)

