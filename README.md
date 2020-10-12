# Python

Regular expression notes: [regex.md](https://github.com/dongyujung/python-scripts/blob/master/regex.md)

### Lambda Function  

With filter(**condition**, seq), or map(function, seq)  

```python
# Lambda function
double = lambda x: x * 2
print(double(3))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# Filter
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
# Map
mapped_list = list(map(lambda x: x ** 2, my_list))
```

### Global Variable  

```python
c = 0
def add():
    global c
    c += 2
    print(c)
add()
print(c)
```
``` 
2
2
```

### Fractions  

```python
import fractions
# Output: 3/2
print(fractions.Fraction(1.5))
# Output: 1/3
print(fractions.Fraction(1,3))
```

### Math  

```python
import math
print(math.pi)
print(math.exp(2))
```

### Random  

```python
import random
# chooses from 1, 2, 3, 4, 5
random.randint(1, 5)    
# chooses from 1, 2, 3, 4
random.randrange(1, 5)
# chooses from 1, 3
random.randrange(1, 5, 2)
# floating point number in the range [0.0, 1.0)
random.random()
# random floating point number N such that a <= N <= b
random.uniform(1.2, 3.6)

x = ['a', 'b', 'c', 'd', 'e']
# Get random choice
random.choice(x)
# Shuffle x
random.shuffle(x)
```

### List  

```python
my_list = ['p','r','o','b','l','e','m']
# delete one item
del my_list[2]
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
# Output: 'o'
print(my_list.pop(1))
# Empty list
my_list.clear()
```

### List Comprehension  

```python
pow2 = [2 ** x for x in range(10)]
pow3 = [x**2 for x in range(10) if x % 2 == 0]
["Even" if i%2==0 else "Odd" for i in range(10)]
```

### Tuple  
Immutable list.  
Can index, negative index, slice, etc.  
```python
my_tuple = (1, 2, 3)
```

### Strings  

```python
str1 = 'Hello'
str2 ='World!'
# Concatenation
print(str1 + str2)
# True
'a' in 'program'
str = 'cold'
# enumerate():  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
list_enumerate = list(enumerate(str))
"PythonProgramming".lower()
"PythonProgramming".upper()
"This will split all words into a list".split()
' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
'Happy New Year'.find('ew')
'Happy New Year'.replace('Happy', 'Brilliant')
'   hello world  \n'.strip()
'---hello====='.strip('-')
# Strips both - and =
'---hello====='.strip('-=')
```

String Formatting  
```
>>> aName = "Dave"
>>> age = 25
>>> print("{} is {} years old.".format(aName, age))
Dave is 25 years old.
>>> print("{0} is {1} years old.".format(aName, age))
Dave is 25 years old.
>>> print("{1} is {0} years old.".format(aName, age))
25 is Dave years old.
>>> print("{:s} is {:d} years old.".format(aName, age))
Dave is 25 years old.
>>> price = 24
>>> item = "banana"
>>> print("The {:10s} costs {:10.2f} cents.".format(item, price))
The banana     costs      24.00 cents.
>>> print("The {0:10s} costs {1:10.2f} cents.".format(item, price))
The banana     costs      24.00 cents.
>>> print("The {:<10s} costs {:<10.2f} cents.".format(item, price))
The banana     costs 24.00      cents.
```

### Sets  

A set is an unordered collection of items. Every element is unique (no duplicates) 
and must be immutable (which cannot be changed).  
However, the set itself is mutable. We can add or remove items from it.  

```python
my_set = {1, 2, 3}
my_set.add(2)
# add multiple elements
my_set.update([2,3,4])
# discard an element: if the item does not exist in the set, it remains unchanged
my_set.discard(4)
# remove an element
my_set.remove(6)
2 in my_set

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
A.union(B)
B.union(A)
# Output: {4, 5}
print(A & B)
A.intersection(B)
# Output: {1, 2, 3}
print(A - B)
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)
```

### Dictionary  

```python
my_dict = {'name':'Jack', 'age': 26}
# Output: Jack
print(my_dict['name'])
# Output: 26
print(my_dict.get('age'))

squares = {1:1, 2:4, 3:9, 4:16, 5:25}  
# remove a particular item
# Output: 16
print(squares.pop(4))

marks = {'math': 1, 'english':2, 'science':1}
# Output [('english', 2), ('math', 1), ('science', 1)]
sorted(marks.items(), key=lambda x: (-x[1], x[0]))

# Dictionary Comprehension
squares = {x: x*x for x in range(6)}
odd_squares = {x: x*x for x in range(11) if x%2 == 1}
```

### File I/O  

#### Reading  
```python
# File Handling

# Open a file
# open() function returns a file object, 
# which has a read() method for reading the content of the file.
f = open(file_path, "r")
print(f.read())
# Specifying encoding type
f = open('./text', mode="r", encoding='utf-8')

# Read parts of the file
f = open(file_path, "r")
# Reads five characters at a time
# Once read, goes on to next part
print(f.read(5))    

# Read lines
f = open(file_path, "r")
print(f.readline())     # Reads one line at a time

# Looping through the lines of the file
f = open(file_path, "r")
for line in f:
    print(line)
# Closing a file will free up the resources that were tied with the file
f.close()

# With statement
# Cleaner syntax and exceptions handling
# Any files opened will be closed automatically after it is done. 
with open(file_path) as f:
    for line in f:
        print(line)

# Read a file line by line, output into a list.
with open(file_path) as f:
    data = f.readlines()
# Without end character \n
with open(file_path) as f:
    lines = f.read().splitlines()

# Drop spaces and new lines (\n) from each line.
with open(file_path) as f:
    for line in f:
        line = line.strip()
        print(line)

# Splitting Lines
for line in data:
    words = line.split(",")
    print(words)
```

#### Writing  

```python
with open('text2', 'w', encoding='utf-8') as f:
    f.write('My first line\n')
    f.write('Second line\n')
    f.write('Third line\n') 
```

### Directory  

```python
import os
os.getcwd()
#>> 'C:\\Program Files\\PyScripter'
print(os.getcwd())
#>> C:\Program Files\PyScripter
os.chdir('C:\\Python33')
# List directories/files
os.listdir()
# Make directory
os.mkdir('test')
# Rename directory
os.rename('test','new_one')
# Remove file
os.remove('old.txt')
# Remove directory
os.rmdir('new_one')
```

### JSON  

```python
import json

data = {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}}

with open('data_file.json', 'w') as write_file:
    # Dictionary to JSON FILE
    json.dump(data, write_file)

with open('data_file.json') as read_file:
    # Reads data from JSON FILE to dictionary
    read_data = json.load(read_file)

# Dictionary to JSON STRING
data_string = json.dumps(read_data)
print(data_string)
# JSON STRING to dictionary
loaded_dict = json.loads(data_string)
print(loaded_dict)
```

### Sort by User-defined Key  

```py
list1 = [(1, 2), (3, 3), (1, 1)] 

list1.sort(key=lambda x: x[1])
```

### Datetime  

```python
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
datetime_object = datetime.now()
date_object = date.today()
# Prints in date/time format
print(date_object)
d = date(2019, 4, 13)
# From Unix timestamp
date.fromtimestamp(1326244364)
datetime.fromtimestamp(1326244364)
# time(hour, minute and second)
a = time(11, 34, 56)
# time(hour, minute, second, microsecond)
b = time(11, 34, 56, 234566)
a.hour
a.minute
a.second
b.microsecond
c = datetime(2017, 11, 28, 23, 55, 59, 342380)
c.year
c.month
c.hour
d = datetime(2017, 11, 26, 10, 55, 59, 342380)
# Timedelta
c-d
e = timedelta(seconds=33)
e.total_seconds()

# Datetime object to string: strftime()
now = datetime.now()
now.strftime("%H:%M:%S")
now.strftime("%m/%d/%Y, %H:%M:%S")
# String to datetime object: strptime()
datetime.strptime("2019-01-15", "%Y-%m-%d")
```

### Regular Expression  

```python
# If it matches in the beginning
re.match(r'\Athe', 'the sun')
# Returns ['12', '89', '34']
re.findall('\d+', 'hello 12 hi 89. Howdy 34')
# Returns ['Twelve:', ' Eighty nine:', '.']
re.split('\d+', 'Twelve:12 Eighty nine:89.')
# Returns 'abc-12-de-23-f45-6'
re.sub('\s+', '-', 'abc 12 de 23 \n f45 6')

```

### Read command line arguments: sys.argv  

```python
import sys

print("First Argument of sys.argv: name of program = ", sys.argv[0])
print("Argument List: ", str(sys.argv))
```

### find_matching_file.py  

```python
def find_matching_file(pattern, path):
    """
    Find file within the path that starts with pattern using re.match
    and return the file path including its name
    """
    for dir_name, subdir_list, file_list in os.walk(path):
        for each_file in file_list:
            if re.match(pattern, each_file):
                return os.path.join(path, each_file)
```

### join_paths.py  

```python
# Join directory path and file name
print(os.path.join('/path/', 'filename'))
```

### regex01.py

```python
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
```

### split_method.py  

```python
x='ginger,garlic,onion'
x.split(',')

y='ginger  garlic  onion'
y.split()
```

### traverse_directory_tree.py  

```python
# Traversing directory tree with os.walk()
for dirName, subdirList, fileList in os.walk(rootDir):
    print 'Found directory: %s' % dirName
    for fname in fileList:
        print '\t%s' % fname
```

### yes_or_no.py

```python
def yes_or_no(question):
    """
    Returns True for input starting with y or Y
    Returns False for input starting with n or N
    Repeat question when neither y nor n was input
    """
    reply = str(raw_input(question+' (y/n): ')).lower()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Please enter ")
```

### serializing_cPickle.py  

```python
'''
Serializing python dictionary with cPickle.
This process turns a Python object into a series of bytes.
By default, the pickle contains only ASCII characters for easier understanding in print.
cPickle uses C instead of Python, therefore many times faster than the Python implementation (pickle)
'''

import cPickle

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]

data_string = cPickle.dumps(data)

print data_string

'''
output:

(dp2
S'a'
S'A'
sS'c'
F3
sS'b'
I2
sa.

'''

data2 = cPickle.loads(data_string)

print data2

'''
output:

[{'a': 'A', 'c': 3.0, 'b': 2}]

'''

```

### rename_files.py  

```python
# Rename files in a directory using os.rename()
for path, subdir, files in os.walk(path):
    for name in files:
        if name[0] == 'M':
            os.rename(os.path.join(path, name), os.path.join(path, 'm' + name[1:]))
```





References:  
https://www.programiz.com/python-programming  
https://realpython.com/python-json/

