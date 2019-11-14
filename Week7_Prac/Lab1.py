import re
text = '''
John and Jane went to Coffee #1 on 140 Queen Street.
They had coffees that cost a total of GBP 5.20 and then waited for a couple of friends.
They hadn't seen each other for over 6 years.
Both of them have a sweet tooth so they also spend almost GBP 20 on cakes in a shop at 30 Castle Street.
'''

print(re.findall(r'\w+\.', text))
print(re.findall(r'\w*ee\w*', text))
print(re.findall(r'[A-Z]\w+', text))
print(re.findall(r'[a-zA-Z\']+', text))
print(re.findall(r'GBP\s[0-9\.]+', text))
print(re.findall(r'\b[a-z][a-zA-Z]*' , text))
