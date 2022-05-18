import re


text = 'ЫВПисиа И ии иыва и'
match = re.findall(r'D', text)
ind = text.index(match[0])

print(ind)
