```python

CHAPTER 5


Files and I/O


# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()


# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
        # process line
        ...


# Write chunks of text data
with open('somefile.txt', 'wt') as f:
    f.write(text1)


    f.write(text2)
    ...


# Redirected print statement
with open('somefile.txt', 'wt') as f:
    print(line1, file=f)
    print(line2, file=f)
    ...


with open('somefile.txt', 'rt', encoding='latin-1') as f:
     ...


f = open('somefile.txt', 'rt')
data = f.read()
f.close()


# Read with disabled newline translation
with open('somefile.txt', 'rt', newline='') as f:
     ...


>>> # Newline translation enabled (the default)
>>> f = open('hello.txt', 'rt')
>>> f.read()
'hello world!\n'


>>> # Newline translation disabled
>>> g = open('hello.txt', 'rt', newline='')
>>> g.read()
'hello world!\r\n'
>>>


>>> f = open('sample.txt', 'rt', encoding='ascii')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.3/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position
12: ordinal not in range(128)
>>>


>>> # Replace bad chars with Unicode U+fffd replacement char
>>> f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
>>> f.read()
'Spicy Jalape?o!'
>>> # Ignore bad chars entirely
>>> g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
>>> g.read()
'Spicy Jalapeo!'
>>>


with open('somefile.txt', 'rt') as f:
    print('Hello World!', file=f)


>>> print('ACME', 50, 91.5)
ACME 50 91.5
>>> print('ACME', 50, 91.5, sep=',')
ACME,50,91.5
>>> print('ACME', 50, 91.5, sep=',', end='!!\n')
ACME,50,91.5!!
>>>


>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>> for i in range(5):
...     print(i, end=' ')
...
0 1 2 3 4 >>>


>>> print(','.join('ACME','50','91.5'))
ACME,50,91.5
>>>


>>> row = ('ACME', 50, 91.5)
>>> print(','.join(row))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 1: expected str instance, int found
>>> print(','.join(str(x) for x in row))
ACME,50,91.5
>>>


>>> print(*row, sep=',')
ACME,50,91.5
>>>


# Read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
    data = f.read()


# Write binary data to a file
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')


>>> # Text string
>>> t = 'Hello World'
>>> t[0]
'H'
>>> for c in t:
...     print(c)
...
H
e
l
l
o
...
>>> # Byte string
>>> b = b'Hello World'
>>> b[0]
72
>>> for c in b:
...     print(c)
...
72
101
108
108
111
...
>>>


with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')


with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))


import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin','wb') as f:
    f.write(nums)


>>> import array
>>> a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
>>> with open('data.bin', 'rb') as f:
...     f.readinto(a)
...
16
>>> a
array('i', [1, 2, 3, 4, 0, 0, 0, 0])
>>>


>>> with open('somefile', 'wt') as f:
...     f.write('Hello\n')
...
>>> with open('somefile', 'xt') as f:
...     f.write('Hello\n')
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileExistsError: [Errno 17] File exists: 'somefile'
>>>


>>> import os
>>> if not os.path.exists('somefile'):
...     with open('somefile', 'wt') as f:
...         f.write('Hello\n')
... else:
...     print('File already exists!')
...
File already exists!
>>>


>>> s = io.StringIO()
>>> s.write('Hello World\n')
12
>>> print('This is a test', file=s)
15
>>> # Get all of the data written so far
>>> s.getvalue()
'Hello World\nThis is a test\n'
>>>


>>> # Wrap a file interface around an existing string
>>> s = io.StringIO('Hello\nWorld\n')
>>> s.read(4)
'Hell'
>>> s.read()
'o\nWorld\n'
>>>


>>> s = io.BytesIO()
>>> s.write(b'binary data')
>>> s.getvalue()
b'binary data'
>>>


# gzip compression
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()


# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


# gzip compression
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)


# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)


with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
     f.write(text)


import gzip


f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
     text = g.read()


from functools import partial


RECORD_SIZE = 32


with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        ...


import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
         f.readinto(buf)
    return buf


>>> # Write a sample file
>>> with open('sample.bin', 'wb') as f:
...      f.write(b'Hello World')
...
>>> buf = read_into_buffer('sample.bin')
>>> buf
bytearray(b'Hello World')
>>> buf[0:5] = b'Hallo'
>>> buf
bytearray(b'Hallo World')
>>> with open('newsample.bin', 'wb') as f:
...     f.write(buf)
...
11
>>>


record_size = 32           # Size of each record (adjust value)


buf = bytearray(record_size)
with open('somefile', 'rb') as f:


    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        # Use the contents of buf
        ...


>>> buf
bytearray(b'Hello World')
>>> m1 = memoryview(buf)
>>> m2 = m1[-5:]
>>> m2
<memory at 0x100681390>
>>> m2[:] = b'WORLD'
>>> buf
bytearray(b'Hello WORLD')
>>>


import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


>>> size = 1000000
>>> with open('data', 'wb') as f:
...      f.seek(size-1)
...      f.write(b'\x00')
...
>>>


>>> m = memory_map('data')
>>> len(m)
1000000
>>> m[0:10]
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> m[0]
0
>>> # Reassign a slice
>>> m[0:11] = b'Hello World'
>>> m.close()


>>> # Verify that changes were made
>>> with open('data', 'rb') as f:
...      print(f.read(11))
...
b'Hello World'
>>>


>>> with memory_map('data') as m:
...      print(len(m))
...      print(m[0:10])
...
1000000
b'Hello World'
>>> m.closed
True
>>>


m = memory_map(filename, mmap.ACCESS_READ)


m = memory_map(filename, mmap.ACCESS_COPY)


>>> m = memory_map('data')
>>> # Memoryview of unsigned integers
>>> v = memoryview(m).cast('I')
>>> v[0] = 7
>>> m[0:4]
b'\x07\x00\x00\x00'
>>> m[0:4] = b'\x07\x01\x00\x00'
>>> v[0]
263
>>>


>>> import os
>>> path = '/Users/beazley/Data/data.csv'


>>> # Get the last component of the path
>>> os.path.basename(path)
'data.csv'


>>> # Get the directory name
>>> os.path.dirname(path)
'/Users/beazley/Data'


>>> # Join path components together
>>> os.path.join('tmp', 'data', os.path.basename(path))
'tmp/data/data.csv'


>>> # Expand the user's home directory
>>> path = '~/Data/data.csv'
>>> os.path.expanduser(path)
'/Users/beazley/Data/data.csv'


>>> # Split the file extension
>>> os.path.splitext(path)
('~/Data/data', '.csv')
>>>


>>> import os
>>> os.path.exists('/etc/passwd')
True
>>> os.path.exists('/tmp/spam')
False
>>>


>>> # Is a regular file
>>> os.path.isfile('/etc/passwd')
True


>>> # Is a directory
>>> os.path.isdir('/etc/passwd')
False


>>> # Is a symbolic link
>>> os.path.islink('/usr/local/bin/python3')
True


>>> # Get the file linked to
>>> os.path.realpath('/usr/local/bin/python3')
'/usr/local/bin/python3.3'
>>>


>>> os.path.getsize('/etc/passwd')
3669
>>> os.path.getmtime('/etc/passwd')
1272478234.0
>>> import time
>>> time.ctime(os.path.getmtime('/etc/passwd'))


'Wed Apr 28 13:10:34 2010'
>>>


>>> os.path.getsize('/Users/guido/Desktop/foo.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.3/genericpath.py", line 49, in getsize
    return os.stat(filename).st_size
PermissionError: [Errno 13] Permission denied: '/Users/guido/Desktop/foo.txt'
>>>


import os
names = os.listdir('somedir')


import os.path
# Get all regular files
names = [name for name in os.listdir('somedir')
         if os.path.isfile(os.path.join('somedir', name))]


# Get all dirs
dirnames = [name for name in os.listdir('somedir')
            if os.path.isdir(os.path.join('somedir', name))]


pyfiles = [name for name in os.listdir('somedir')
           if name.endswith('.py')]


import glob
pyfiles = glob.glob('somedir/*.py')


from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
           if fnmatch(name, '*.py')]


# Example of getting a directory listing


import os
import os.path
import glob


pyfiles = glob.glob('*.py')


# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]


for name, size, mtime in name_sz_date:
    print(name, size, mtime)


# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)


>>> sys.getfilesystemencoding()
'utf-8'
>>>


>>> # Wrte a file using a unicode filename
>>> with open('jalape\xf1o.txt', 'w') as f:
...     f.write('Spicy!')
...
6
>>> # Directory listing (decoded)
>>> import os
>>> os.listdir('.')
['jalapeño.txt']


>>> # Directory listing (raw)
>>> os.listdir(b'.')        # Note: byte string
[b'jalapen\xcc\x83o.txt']


>>> # Open file with raw filename
>>> with open(b'jalapen\xcc\x83o.txt') as f:
...     print(f.read())
...
Spicy!
>>>


def bad_filename(filename):
    return repr(filename)[1:-1]


try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))


>>> import os
>>> files = os.listdir('.')
>>> files
['spam.py', 'b\udce4d.txt', 'foo.txt']
>>>


>>> for name in files:
...     print(name)
...
spam.py
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
UnicodeEncodeError: 'utf-8' codec can't encode character '\udce4' in
position 1: surrogates not allowed
>>>


>>> for name in files:
...     try:
...             print(name)
...     except UnicodeEncodeError:
...             print(bad_filename(name))
...
spam.py
b\udce4d.txt
foo.txt
>>>


def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')


>>> for name in files:
...     try:
...             print(name)
...     except UnicodeEncodeError:
...             print(bad_filename(name))
...


spam.py
bäd.txt
foo.txt
>>>


import urllib.request
import io


u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u,encoding='utf-8')
text = f.read()


>>> import sys
>>> sys.stdout.encoding
'UTF-8'
>>> sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
>>> sys.stdout.encoding
'latin-1'
>>>


>>> f = open('sample.txt','w')
>>> f
<_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
>>> f.buffer
<_io.BufferedWriter name='sample.txt'>
>>> f.buffer.raw
<_io.FileIO name='sample.txt' mode='wb'>
>>>


>>> f
<_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
>>> f = io.TextIOWrapper(f.buffer, encoding='latin-1')
>>> f
<_io.TextIOWrapper name='sample.txt' encoding='latin-1'>
>>> f.write('Hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>>


>>> f = open('sample.txt', 'w')
>>> f
<_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
>>> b = f.detach()
>>> b
<_io.BufferedWriter name='sample.txt'>
>>> f.write('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: underlying buffer has been detached
>>>


>>> f = io.TextIOWrapper(b, encoding='latin-1')
>>> f


<_io.TextIOWrapper name='sample.txt' encoding='latin-1'>
>>>


>>> sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',
...                               errors='xmlcharrefreplace')
>>> print('Jalape\u00f1o')
Jalape&#241;o
>>>


>>> import sys
>>> sys.stdout.write(b'Hello\n')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not bytes
>>> sys.stdout.buffer.write(b'Hello\n')
Hello
5
>>>


# Open a low-level file descriptor
import os
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)


# Turn into a proper file
f = open(fd, 'wt')
f.write('hello world\n')
f.close()


# Create a file object, but don't close underlying fd when done
f = open(fd, 'wt', closefd=False)
...


from socket import socket, AF_INET, SOCK_STREAM


def echo_client(client_sock, addr):
    print('Got connection from', addr)


    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                         closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                          closefd=False)


    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)


import sys
# Create a binary-mode file for stdout
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()


from tempfile import TemporaryFile


with TemporaryFile('w+t') as f:
     # Read/write to the file
     f.write('Hello World\n')
     f.write('Testing\n')


     # Seek back to beginning and read the data
     f.seek(0)
     data = f.read()


# Temporary file is destroyed


f = TemporaryFile('w+t')
# Use the temporary file
...
f.close()
# File is destroyed


with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
     ...


from tempfile import NamedTemporaryFile


with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)
    ...


# File automatically destroyed


with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)
    ...


from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
     print('dirname is:', dirname)
     # Use the directory
     ...
# Directory and all contents destroyed


>>> import tempfile
>>> tempfile.mkstemp()
(3, '/var/folders/7W/7WZl5sfZEF0pljrEB1UMWE+++TI/-Tmp-/tmp7fefhv')
>>> tempfile.mkdtemp()
'/var/folders/7W/7WZl5sfZEF0pljrEB1UMWE+++TI/-Tmp-/tmp5wvcv6'
>>>


>>> tempfile.gettempdir()
'/var/folders/7W/7WZl5sfZEF0pljrEB1UMWE+++TI/-Tmp-'
>>>


>>> f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
>>> f.name
'/tmp/mytemp8ee899.txt'
>>>


import serial
ser = serial.Serial('/dev/tty.usbmodem641',  # Device name varies
                     baudrate=9600,
                     bytesize=8,
                     parity='N',
                     stopbits=1)


ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()


import pickle


data = ...   # Some Python object
f = open('somefile', 'wb')
pickle.dump(data, f)


s = pickle.dumps(data)


# Restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)


# Restore from a string
data = pickle.loads(s)


>>> import pickle
>>> f = open('somedata', 'wb')
>>> pickle.dump([1, 2, 3, 4], f)
>>> pickle.dump('hello', f)
>>> pickle.dump({'Apple', 'Pear', 'Banana'}, f)
>>> f.close()
>>> f = open('somedata', 'rb')
>>> pickle.load(f)
[1, 2, 3, 4]
>>> pickle.load(f)
'hello'
>>> pickle.load(f)
{'Apple', 'Pear', 'Banana'}
>>>


>>> import math
>>> import pickle.
>>> pickle.dumps(math.cos)
b'\x80\x03cmath\ncos\nq\x00.'
>>>


pickle.load() should never be used on untrusted data. As a side effect
of loading, pickle will automatically load modules and make instances.
However, an evildoer who knows how pickle works can create “mal‐
formed” data that causes Python to execute arbitrary system com‐
mands. Thus, it’s essential that pickle only be used internally with in‐
terpreters that have some ability to authenticate one another.


# countdown.py
import time
import threading


class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()


    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


    def __getstate__(self):
        return self.n


    def __setstate__(self, n):
        self.__init__(n)


>>> import countdown
>>> c = countdown.Countdown(30)
>>> T-minus 30
T-minus 29
T-minus 28
...


>>> # After a few moments
>>> f = open('cstate.p', 'wb')
>>> import pickle
>>> pickle.dump(c, f)
>>> f.close()


>>> f = open('cstate.p', 'rb')
>>> pickle.load(f)
countdown.Countdown object at 0x10069e2d0>
T-minus 19
T-minus 18
...
```