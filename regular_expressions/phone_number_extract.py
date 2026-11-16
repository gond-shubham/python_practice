import re


text = """Contact Rahul at 9876543210.
          Office: 0712-2567890.
          Emergency: +91-9876543210."""

#Findall phone numbers
match = re.findall(r'[0-9+-]+', text)
print(match)

#match the exact string.
match2=re.match(r'[a-zA-Z\s]+(?P<personal>[0-9]{10})\.\s*Office: (?P<office>[0-9-]+)\.\s*Emergency: (?P<emergency>[0-9+-]+)\.', text)

print(match2)
print(match2.group())


#fullmatch the string.
match3=re.fullmatch(r'[a-zA-Z\s]*(?P<personal>[0-9]{10})\.\s*Office: (?P<office>[0-9-]{12})\.\s*Emergency: (?P<emergency>[0-9+-]{14}).', text)

print(match3)
print(match3.group())