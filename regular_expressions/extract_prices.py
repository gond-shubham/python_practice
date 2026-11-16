import re

text = """
Laptop price: ₹55,999
Mouse price: ₹799
Keyboard price: ₹1,499
Discount: ₹500
"""

prices = re.findall(r'[0-9,₹]+', text)

print(prices)