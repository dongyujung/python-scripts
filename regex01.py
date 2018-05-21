import re

# re.match(pattern, string, flags=0)
re.match(r'Ginger', 'Ginger')

# .: any single character except newline character
a = re.search(r'Gi..er', 'Ginger').group()
print(a)

# \w: Lowercase w. Matches any single letter, digit or underscore.
b = re.search(r'Gi\wg\wr', 'Ginger').group()
print(b)

c = re.search(r'Gi\wg\wr', 'GingerBread').group()
print(c)

d = re.search(r'Gi\wg\wr', 'GingerBread').start()
print(d)

e = re.search(r'Gi\wg\wr', 'GingerBread').end()
print(e)

f = re.search(r'Gi\wg\wr', 'GingerBread').span()
print(f)
