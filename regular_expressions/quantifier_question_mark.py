import re


text = "color colour colouur colouuur"

match1=re.findall(r'colour?', text)

match2=re.findall(r'color?', text)

match3=re.findall(r'colou+r?', text)

match4=re.findall(r'colou?r', text)

print(match1, match2,match3,match4,  sep="\n")