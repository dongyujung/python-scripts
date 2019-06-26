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
