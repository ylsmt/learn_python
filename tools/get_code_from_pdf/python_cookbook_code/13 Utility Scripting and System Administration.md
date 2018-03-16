```python

CHAPTER 13


#!/usr/bin/env python3
import fileinput


with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')


$ ls | ./filein.py          # Prints a directory listing to stdout.
$ ./filein.py /etc/passwd   # Reads /etc/passwd to stdout.
$ ./filein.py < /etc/passwd # Reads /etc/passwd to stdout.


>>> import fileinput
>>> with fileinput.input('/etc/passwd') as f:
>>>     for line in f:
...         print(f.filename(), f.lineno(), line, end='')
...
/etc/passwd 1 ##
/etc/passwd 2 # User Database
/etc/passwd 3 #


<other output omitted>


raise SystemExit('It failed!')


import sys
sys.stderr.write('It failed!\n')
raise SystemExit(1)


# search.py
'''
Hypothetical command-line tool for searching a collection of
files for one or more text patterns.
'''
import argparse
parser = argparse.ArgumentParser(description='Search some files')


parser.add_argument(dest='filenames',metavar='filename', nargs='*')


parser.add_argument('-p', '--pat',metavar='pattern', required=True,
                    dest='patterns', action='append',
                    help='text pattern to search for')


parser.add_argument('-v', dest='verbose', action='store_true',
                    help='verbose mode')


parser.add_argument('-o', dest='outfile', action='store',
                    help='output file')


parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='slow',
                    help='search speed')


args = parser.parse_args()


# Output the collected arguments
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)


bash % python3 search.py -h
usage: search.py [-h] [-p pattern] [-v] [-o OUTFILE] [--speed {slow,fast}]
                 [filename [filename ...]]


Search some files


positional arguments:
  filename


optional arguments:
  -h, --help            show this help message and exit
  -p pattern, --pat pattern
                        text pattern to search for
  -v                    verbose mode
  -o OUTFILE            output file
  --speed {slow,fast}   search speed


bash % python3 search.py foo.txt bar.txt
usage: search.py [-h] -p pattern [-v] [-o OUTFILE] [--speed {fast,slow}]
                 [filename [filename ...]]
search.py: error: the following arguments are required: -p/--pat


bash % python3 search.py -v -p spam --pat=eggs foo.txt bar.txt
filenames = ['foo.txt', 'bar.txt']
patterns  = ['spam', 'eggs']
verbose   = True
outfile   = None
speed     = slow


bash % python3 search.py -v -p spam --pat=eggs foo.txt bar.txt -o results
filenames = ['foo.txt', 'bar.txt']
patterns  = ['spam', 'eggs']
verbose   = True
outfile   = results
speed     = slow


parser.add_argument(dest='filenames',metavar='filename', nargs='*')


parser.add_argument('-v', dest='verbose', action='store_true',
                    help='verbose mode')


parser.add_argument('-o', dest='outfile', action='store',
                    help='output file')


parser.add_argument('-p', '--pat',metavar='pattern', required=True,
                    dest='patterns', action='append',
                    help='text pattern to search for')


parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='slow',
                    help='search speed')


import getpass


user = getpass.getuser()
passwd = getpass.getpass()


if svc_login(user, passwd):    # You must write svc_login()
   print('Yay!')
else:
   print('Boo!')


user = input('Enter your username: ')


>>> import os
>>> sz = os.get_terminal_size()
>>> sz
os.terminal_size(columns=80, lines=24)
>>> sz.columns
80
>>> sz.lines
24
>>>


import subprocess
out_bytes = subprocess.check_output(['netstat','-a'])


out_text = out_bytes.decode('utf-8')


try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output       # Output generated before error
    code      = e.returncode   # Return code


out_bytes = subprocess.check_output(['cmd','arg1','arg2'],
                                    stderr=subprocess.STDOUT)


try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'], timeout=5)
except subprocess.TimeoutExpired as e:
    ...


out_bytes = subprocess.check_output('grep python | wc > out', shell=True)


import subprocess


# Some text to send
text = b'''
hello world
this is a test
goodbye
'''


# Launch a command with pipes
p = subprocess.Popen(['wc'],
          stdout = subprocess.PIPE,
          stdin = subprocess.PIPE)


# Send the data and get the output
stdout, stderr = p.communicate(text)


# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')


import shutil


# Copy src to dst. (cp src dst)
shutil.copy(src, dst)


# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)


# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)


# Move src to dst (mv src dst)
shutil.move(src, dst)


shutil.copy2(src, dst, follow_symlinks=False)


shutil.copytree(src, dst, symlinks=True)


def ignore_pyc_files(dirname, filenames):
    return [name in filenames if name.endswith('.pyc')]


shutil.copytree(src, dst, ignore=ignore_pyc_files)


shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~','*.pyc'))


>>> filename = '/Users/guido/programs/spam.py'
>>> import os.path
>>> os.path.basename(filename)
'spam.py'
>>> os.path.dirname(filename)
'/Users/guido/programs'
>>> os.path.split(filename)
('/Users/guido/programs', 'spam.py')
>>> os.path.join('/new/dir', os.path.basename(filename))
'/new/dir/spam.py'
>>> os.path.expanduser('~/guido/programs/spam.py')
'/Users/guido/programs/spam.py'
>>>


try:
    shutil.copytree(src, dst)
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
         # src is source name
         # dst is destination name
         # msg is error message from exception
         print(dst, src, msg)


>>> import shutil
>>> shutil.unpack_archive('Python-3.3.0.tgz')


>>> shutil.make_archive('py33','zip','Python-3.3.0')
'/Users/beazley/Downloads/py33.zip'
>>>


>>> shutil.get_archive_formats()
[('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"),
 ('tar', 'uncompressed tar file'), ('zip', 'ZIP file')]
>>>


#!/usr/bin/env python3.3
import os


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


if __name__ == '__main__':
    findfile(sys.argv[1], sys.argv[2])


bash % ./findfile.py . myfile.txt


#!/usr/bin/env python3.3


import os
import time


def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: {} dir seconds'.format(sys.argv[0]))
        raise SystemExit(1)


    modified_within(sys.argv[1], float(sys.argv[2]))


; config.ini
; Sample configuration file


[installation]
library=%(prefix)s/lib
include=%(prefix)s/include
bin=%(prefix)s/bin
prefix=/usr/local


# Setting related to debug configuration
[debug]
log_errors=true
show_warnings=False


[server]
port: 8080
nworkers: 32
pid-file=/tmp/spam.pid
root=/www/root
signature:
    =================================
    Brought to you by the Python Cookbook
    =================================


>>> from configparser import ConfigParser
>>> cfg = ConfigParser()
>>> cfg.read('config.ini')
['config.ini']
>>> cfg.sections()
['installation', 'debug', 'server']
>>> cfg.get('installation','library')
'/usr/local/lib'
>>> cfg.getboolean('debug','log_errors')


True
>>> cfg.getint('server','port')
8080
>>> cfg.getint('server','nworkers')
32
>>> print(cfg.get('server','signature'))


=================================
Brought to you by the Python Cookbook
=================================
>>>


>>> cfg.set('server','port','9000')
>>> cfg.set('debug','log_errors','False')
>>> import sys
>>> cfg.write(sys.stdout)
[installation]
library = %(prefix)s/lib
include = %(prefix)s/include
bin = %(prefix)s/bin
prefix = /usr/local


[debug]
log_errors = False
show_warnings = False


[server]
port = 9000
nworkers = 32
pid-file = /tmp/spam.pid
root = /www/root
signature =
          =================================
          Brought to you by the Python Cookbook
          =================================
>>>


prefix=/usr/local
prefix: /usr/local


>>> cfg.get('installation','PREFIX')
'/usr/local'
>>> cfg.get('installation','prefix')
'/usr/local'
>>>


    log_errors = true
    log_errors = TRUE
    log_errors = Yes
    log_errors = 1


    [installation]
    library=%(prefix)s/lib
    include=%(prefix)s/include
    bin=%(prefix)s/bin
    prefix=/usr/local


    ; ~/.config.ini
    [installation]
    prefix=/Users/beazley/test


    [debug]
    log_errors=False


>>> # Previously read configuration
>>> cfg.get('installation', 'prefix')
'/usr/local'


>>> # Merge in user-specific configuration
>>> import os
>>> cfg.read(os.path.expanduser('~/.config.ini'))
['/Users/beazley/.config.ini']


>>> cfg.get('installation', 'prefix')
'/Users/beazley/test'
>>> cfg.get('installation', 'library')
'/Users/beazley/test/lib'
>>> cfg.getboolean('debug', 'log_errors')
False
>>>


>>> cfg.get('installation','library')
'/Users/beazley/test/lib'
>>> cfg.set('installation','prefix','/tmp/dir')
>>> cfg.get('installation','library')
'/tmp/dir/lib'
>>>


import logging


def main():
    # Configure the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR
    )


    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'


    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')


if __name__ == '__main__':
    main()


    CRITICAL:root:Host www.python.org unknown
    ERROR:root:Could not find 'spam'


logging.basicConfig(
     filename='app.log',
     level=logging.WARNING,
     format='%(levelname)s:%(asctime)s:%(message)s')


    CRITICAL:2012-11-20 12:27:13,595:Host www.python.org unknown
    ERROR:2012-11-20 12:27:13,595:Could not find 'spam'
    WARNING:2012-11-20 12:27:13,595:Feature is deprecated


import logging
import logging.config


def main():
    # Configure the logging system
    logging.config.fileConfig('logconfig.ini')
    ...


    [loggers]
    keys=root


    [handlers]
    keys=defaultHandler


    [formatters]
    keys=defaultFormatter


    [logger_root]
    level=INFO
    handlers=defaultHandler
    qualname=root


    [handler_defaultHandler]
    class=FileHandler
    formatter=defaultFormatter
    args=('app.log', 'a')


    [formatter_defaultFormatter]
    format=%(levelname)s:%(name)s:%(message)s


logging.basicConfig(level=logging.INFO)


logging.getLogger().level = logging.DEBUG


# somelib.py


import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


# Example function (for testing)
def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')


>>> import somelib
>>> somelib.func()
>>>


>>> import logging
>>> logging.basicConfig()
>>> somelib.func()
CRITICAL:somelib:A Critical Error!
>>>


>>> import logging
>>> logging.basicConfig(level=logging.ERROR)
>>> import somelib
>>> somelib.func()
CRITICAL:somelib:A Critical Error!


>>> # Change the logging level for 'somelib' only
>>> logging.getLogger('somelib').level=logging.DEBUG
>>> somelib.func()
CRITICAL:somelib:A Critical Error!
DEBUG:somelib:A debug message
>>>


import time


class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None


    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()


    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None


    def reset(self):
        self.elapsed = 0.0


    @property
    def running(self):
        return self._start is not None


    def __enter__(self):
        self.start()
        return self


    def __exit__(self, *args):
        self.stop()


def countdown(n):
    while n > 0:
        n -= 1


# Use 1: Explicit start/stop
t = Timer()
t.start()
countdown(1000000)
t.stop()
print(t.elapsed)


# Use 2: As a context manager
with t:
    countdown(1000000)


print(t.elapsed)


with Timer() as t2:
    countdown(1000000)
print(t2.elapsed)


t = Timer(time.process_time)
with t:
    countdown(1000000)
print(t.elapsed)


import signal
import resource
import os


def time_exceeded(signo, frame):
    print("Time's up!")
    raise SystemExit(1)


def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


if __name__ == '__main__':
    set_max_runtime(15)
    while True:
        pass


import resource


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


>>> import webbrowser
>>> webbrowser.open('http://www.python.org')
True
>>>


>>> # Open the page in a new browser window
>>> webbrowser.open_new('http://www.python.org')
True
>>>


>>> # Open the page in a new browser tab
>>> webbrowser.open_new_tab('http://www.python.org')
True
>>>


>>> c = webbrowser.get('firefox')
>>> c.open('http://www.python.org')
True
>>> c.open_new_tab('http://docs.python.org')
True
>>>
```