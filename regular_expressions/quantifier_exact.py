import re

text = "IDs: EMP12345 EMP6789 EMP123456 EMP54321"

text1 = "Codes: A12 B123 C1234 D12345"

text2 = "Numbers: 12 123 1234 12345 123456"

match= re.findall(r'EMP\d{5}', text)

match1=re.findall(r'[A-Z]\d{2,4}', text1)

match2=re.findall(r'\d{4,}', text2)



print(match, match1, match2, sep='\n')
