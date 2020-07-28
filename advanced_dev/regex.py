"""
. - anything (letters, numbers...)
+ - one or more of
* zero or more of
? zero or one of
[] any character in the set i.e [abc] or [a-z]
"""

import re

email = 'sharleenhussey@hotmail.com'
expression = '[a-z\.]+'

matches = re.findall(expression,email)
print(matches)

name = matches[0]
domain = matches[1]

print(name)
print(domain)

price = 'Price: $2493.03'
expression = 'Price: \$([0-9\,]*\.[0-9]*)'

matches = re.search(expression,price)
price_number = matches.group(1)
print(price_number)