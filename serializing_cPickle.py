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

