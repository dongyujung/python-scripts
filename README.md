# Python

### List Complrehension  


### Lambda Function  

With filter(fun, seq), or map(fun, seq)  

```python
# Lambda function
double = lambda x: x * 2
print(double(3))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
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

### file_open_read.py
```py
# File Handling

# Open a file
# open() function returns a file object, 
# which has a read() method for reading the content of the file.
f = open(file_path, "r")
print(f.read())

# Read parts of the file
f = open(file_path, "r")
print(f.read(5))    # Reads five characters at a time

# Read lines
f = open(file_path, "r")
print(f.readline())     # Reads one line at a time

# Looping through the lines of the file
f = open(file_path, "r")
for line in f:
    print(line)

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

# Splitting Lines
for line in data:
    words = line.split(",")
    print(words)

# Drop spaces and new lines (\n) from each line.
with open(file_path) as f:
    for line in f:
        line = line.strip()
        print(line)
```

### Sort by User-defined Key  

```py
list1 = [(1, 2), (3, 3), (1, 1)] 

list1.sort(key=lambda x: x[1])
```



