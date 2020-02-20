data = []
with open('tweets.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            data.append(line)
data_str = '\n'.join(data)

import re

print(re.findall(r'[@]\w+', data_str))
print(re.findall(r'([Dd]emonetization\s[Ii]s)\s([a-zA-Z\s]+)', data_str))
