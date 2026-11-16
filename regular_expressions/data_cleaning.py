import re

text = """
Name:   Rahul   Sharma
Phone:  +91-98765-43210
Email:  rahul.sharma@gmail.com
"""

clean_data= re.sub(r' +', ' ', text)

print(clean_data)


clean_data1=re.sub(r'\s+', ' ', text)

print(clean_data1)