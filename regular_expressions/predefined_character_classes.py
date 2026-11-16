import re

text = "Rahul 123 @ Data_Science!"

match_digits= re.findall(r'\d', text)

match_spaces=re.findall(r'\s', text)

match_non_digits=re.findall(r'\D', text)

match_word_char=re.findall(r'\w', text)

match_non_word= re.findall(r'\W', text)

match_non_spaces=re.findall(r'\S', text)

print(match_digits, match_spaces, match_non_digits, match_word_char, match_non_word, match_non_spaces, sep="\n")

