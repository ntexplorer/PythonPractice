import re
text = "199.1.123.12"
p = r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

m = re.match(p, text)
if m:
    print(m.group())
