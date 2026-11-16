import re

text1 = "My employee ID is EMP12345"

text2= "EMP12345 is my employee id"

pattern1=re.match(r'EMP\d{5}', text1)

pattern2=re.match(r'EMP\d{5}', text2)

print(pattern1, pattern2, sep="\n")

