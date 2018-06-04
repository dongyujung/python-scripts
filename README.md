# python_algorithms

### find_matching_file.py  

```python
def find_matching_file(pattern, path):
    """
    Find file within the path that starts with pattern
    using re.match
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



