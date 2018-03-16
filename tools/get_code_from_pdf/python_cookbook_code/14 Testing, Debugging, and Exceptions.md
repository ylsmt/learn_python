```python

Testing, Debugging, and Exceptions


CHAPTER 14


# mymodule.py


def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)


from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import mymodule


class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)


        with patch('sys.stdout', new=StringIO()) as fake_out:
            mymodule.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)


from unittest.mock import patch
import example


@patch('example.func')
def test1(x, mock_func):
    example.func(x)       # Uses patched example.func
    mock_func.assert_called_with(x)


with patch('example.func') as mock_func:
    example.func(x)      # Uses patched example.func
    mock_func.assert_called_with(x)


p = patch('example.func')
mock_func = p.start()
example.func(x)
mock_func.assert_called_with(x)
p.stop()


@patch('example.func1')
@patch('example.func2')
@patch('example.func3')
def test1(mock1, mock2, mock3):
    ...


def test2():
    with patch('example.patch1') as mock1,


>>> x = 42
>>> with patch('__main__.x'):
...     print(x)
...
<MagicMock name='x' id='4314230032'>
>>> x
42
>>>


>>> x
42
>>> with patch('__main__.x', 'patched_value'):
...     print(x)
...
patched_value
>>> x
42
>>>


>>> from unittest.mock import MagicMock
>>> m = MagicMock(return_value = 10)
>>> m(1, 2, debug=True)
10
>>> m.assert_called_with(1, 2, debug=True)
>>> m.assert_called_with(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".../unittest/mock.py", line 726, in assert_called_with
    raise AssertionError(msg)
AssertionError: Expected call: mock(1, 2)
Actual call: mock(1, 2, debug=True)
>>>


>>> m.upper.return_value = 'HELLO'
>>> m.upper('hello')
'HELLO'
>>> assert m.upper.called


>>> m.split.return_value = ['hello', 'world']
>>> m.split('hello world')
['hello', 'world']
>>> m.split.assert_called_with('hello world')
>>>


>>> m['blah']
<MagicMock name='mock.__getitem__()' id='4314412048'>
>>> m.__getitem__.called
True
>>> m.__getitem__.assert_called_with('blah')
>>>


# example.py
from urllib.request import urlopen
import csv


def dowprices():
    u = urlopen('http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1')
    lines = (line.decode('utf-8') for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = { name:float(price) for name, price in rows }
    return prices


import unittest
from unittest.mock import patch
import io
import example


sample_data = io.BytesIO(b'''


if __name__ == '__main__':
    unittest.main()


import unittest


# A simple function to illustrate
def parse_int(s):
    return int(s)


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')


import errno


class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)


        else:
            self.fail('IOError not raised')


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        try:
            r = parse_int('N/A')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        try:
            r = parse_int('N/A')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail('ValueError not raised')


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaisesRegex(ValueError, 'invalid literal .*',
                                       parse_int, 'N/A')


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        with self.assertRaisesRegex(ValueError, 'invalid literal .*'):
            r = parse_int('N/A')


import unittest


class MyTest(unittest.TestCase):
    ...


if __name__ == '__main__':
    unittest.main()


import sys
def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out,verbosity=verbosity).run(suite)


if __name__ == '__main__':
    with open('testing.out', 'w') as f:
        main(f)


import unittest
import os
import platform


class Tests(unittest.TestCase):
    def test_0(self):
        self.assertTrue(True)


    @unittest.skip('skipped test')
    def test_1(self):
        self.fail('should have failed!')


    @unittest.skipIf(os.name=='posix', 'Not supported on Unix')
    def test_2(self):
        import winreg


    @unittest.skipUnless(platform.system() == 'Darwin', 'Mac specific test')
    def test_3(self):
        self.assertTrue(True)


    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(2+2, 5)


if __name__ == '__main__':
    unittest.main()


    bash % python3 testsample.py -v
    test_0 (__main__.Tests) ... ok
    test_1 (__main__.Tests) ... skipped 'skipped test'
    test_2 (__main__.Tests) ... skipped 'Not supported on Unix'
    test_3 (__main__.Tests) ... ok
    test_4 (__main__.Tests) ... expected failure


    ----------------------------------------------------------------------
    Ran 5 tests in 0.002s


    OK (skipped=2, expected failures=1)


@unittest.skipUnless(platform.system() == 'Darwin', 'Mac specific tests')
class DarwinTests(unittest.TestCase):
    ...


try:
    client_obj.get_url(url)
except (URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)


try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)


try:
    f = open(filename)
except (FileNotFoundError, PermissionError):
    ...


try:
    f = open(filename)
except OSError:
    ...


try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EACCES:
        logger.error('Permission denied')


    else:
        logger.error('Unexpected error: %d', e.errno)


>>> f = open('missing')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'missing'
>>> try:
...     f = open('missing')
... except OSError:
...     print('It failed')
... except FileNotFoundError:
...     print('File not found')
...
It failed
>>>


>>> FileNotFoundError.__mro__
(<class 'FileNotFoundError'>, <class 'OSError'>, <class 'Exception'>,
 <class 'BaseException'>, <class 'object'>)
>>>


try:
   ...
except Exception as e:
   ...
   log('Reason:', e)       # Important!


def parse_int(s):
    try:
        n = int(v)
    except Exception:
        print("Couldn't parse")


>>> parse_int('n/a')
Couldn't parse
>>> parse_int('42')
Couldn't parse
>>>


def parse_int(s):
    try:
        n = int(v)
    except Exception as e:
        print("Couldn't parse")
        print('Reason:', e)


>>> parse_int('42')
Couldn't parse
Reason: global name 'v' is not defined
>>>


class NetworkError(Exception):
    pass


class HostnameError(NetworkError):
    pass


class TimeoutError(NetworkError):
    pass


class ProtocolError(NetworkError):
    pass


try:
    msg = s.recv()
except TimeoutError as e:
    ...
except ProtocolError as e:
    ...


try:
    s.send(msg)
except ProtocolError:
    ...


try:
    s.send(msg)
except NetworkError:
    ...


class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status


>>> try:
...     raise RuntimeError('It failed')
... except RuntimeError as e:
...     print(e.args)
...
('It failed',)
>>> try:
...     raise RuntimeError('It failed', 42, 'spam')
... except RuntimeError as e:


...     print(e.args)
...
('It failed', 42, 'spam')
>>>


>>> def example():
...     try:
...             int('N/A')
...     except ValueError as e:
...             raise RuntimeError('A parsing error occurred') from e...
>>> 
example()
Traceback (most recent call last):
  File "<stdin>", line 3, in example
ValueError: invalid literal for int() with base 10: 'N/A'


The above exception was the direct cause of the following exception:


Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in example
RuntimeError: A parsing error occurred
>>>


try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)


    if e.__cause__:
        print('Cause:', e.__cause__)


>>> def example2():
...     try:
...             int('N/A')
...     except ValueError as e:
...             print("Couldn't parse:", err)
...
>>>
>>> example2()
Traceback (most recent call last):
  File "<stdin>", line 3, in example2
ValueError: invalid literal for int() with base 10: 'N/A'


During handling of the above exception, another exception occurred:


Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in example2
NameError: global name 'err' is not defined
>>>


>>> def example3():
...     try:
...             int('N/A')
...     except ValueError:
...             raise RuntimeError('A parsing error occurred') from None...
>>> 
example3()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in example3
RuntimeError: A parsing error occurred
>>>


try:
   ...
except SomeException as e:
   raise DifferentException() from e


try:
   ...
except SomeException:
   raise DifferentException()


>>> def example():
...     try:
...             int('N/A')
...     except ValueError:
...             print("Didn't work")
...             raise
...


>>> example()
Didn't work
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in example
ValueError: invalid literal for int() with base 10: 'N/A'
>>>


try:
   ...
except Exception as e:
   # Process exception information in some way
   ...


   # Propagate the exception
   raise


import warnings


def func(x, y, logfile=None, debug=False):
    if logfile is not None:
         warnings.warn('logfile argument deprecated', DeprecationWarning)
    ...


    bash % python3 -W all example.py
    example.py:5: DeprecationWarning: logfile argument is deprecated
      warnings.warn('logfile argument is deprecated', DeprecationWarning)


    bash % python3 -W error example.py
    Traceback (most recent call last):
      File "example.py", line 10, in <module>
        func(2, 3, logfile='log.txt')
      File "example.py", line 5, in func
        warnings.warn('logfile argument is deprecated', DeprecationWarning)
    DeprecationWarning: logfile argument is deprecated
    bash %


>>> import warnings
>>> warnings.simplefilter('always')
>>> f = open('/etc/passwd')
>>> del f
__main__:1: ResourceWarning: unclosed file <_io.TextIOWrapper name='/etc/passwd'
 mode='r' encoding='UTF-8'>
>>>


# sample.py


def func(n):
    return n + 10


func('Hello')


bash % python3 -i sample.py
Traceback (most recent call last):
  File "sample.py", line 6, in <module>
    func('Hello')
  File "sample.py", line 4, in func
    return n + 10
TypeError: Can't convert 'int' object to str implicitly
>>> func(10)
20
>>>


>>> import pdb
>>> pdb.pm()
> sample.py(4)func()
-> return n + 10
(Pdb) w
  sample.py(6)<module>()
-> func('Hello')
> sample.py(4)func()
-> return n + 10
(Pdb) print n
'Hello'
(Pdb) q
>>>


import traceback
import sys


try:
    func(arg)
except:
    print('**** AN ERROR OCCURRED ****')
    traceback.print_exc(file=sys.stderr)


>>> def sample(n):
...     if n > 0:
...             sample(n-1)
...     else:
...             traceback.print_stack(file=sys.stderr)
...
>>> sample(5)
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in sample
  File "<stdin>", line 3, in sample
  File "<stdin>", line 3, in sample
  File "<stdin>", line 3, in sample
  File "<stdin>", line 3, in sample
  File "<stdin>", line 5, in sample
>>>


import pdb


def func(arg):
    ...
    pdb.set_trace()
    ...


bash % time python3 someprogram.py
real 0m13.937s
user 0m12.162s
sys  0m0.098s
bash %


bash % python3 -m cProfile someprogram.py
         859647 function calls in 16.016 CPU seconds


   Ordered by: standard name


   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   263169    0.080    0.000    0.080    0.000 someprogram.py:16(frange)
      513    0.001    0.000    0.002    0.000 someprogram.py:30(generate_mandel)
   262656    0.194    0.000   15.295    0.000 someprogram.py:32(<genexpr>)
        1    0.036    0.036   16.077   16.077 someprogram.py:4(<module>)
   262144   15.021    0.000   15.021    0.000 someprogram.py:4(in_mandelbrot)
        1    0.000    0.000    0.000    0.000 os.py:746(urandom)
        1    0.000    0.000    0.000    0.000 png.py:1056(_readable)
        1    0.000    0.000    0.000    0.000 png.py:1073(Reader)
        1    0.227    0.227    0.438    0.438 png.py:163(<module>)
      512    0.010    0.000    0.010    0.000 png.py:200(group)
    ...
bash %


# timethis.py


import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


>>> @timethis
... def countdown(n):
...     while n > 0:
...             n -= 1
...
>>> countdown(10000000)
__main__.countdown : 0.803001880645752
>>>


from contextlib import contextmanager


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))


>>> with timeblock('counting'):
...     n = 10000000
...     while n > 0:
...             n -= 1
...
counting : 1.5551159381866455
>>>


>>> from timeit import timeit
>>> timeit('math.sqrt(2)', 'import math')
0.1432319980012835
>>> timeit('sqrt(2)', 'from math import sqrt')
0.10836604500218527
>>>


>>> timeit('math.sqrt(2)', 'import math', number=10000000)
1.434852126003534
>>> timeit('sqrt(2)', 'from math import sqrt', number=10000000)
1.0270336690009572
>>>


from functools import wraps
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        end = time.process_time()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


# somescript.py


import sys
import csv


with open(sys.argv[1]) as f:
     for row in csv.reader(f):


         # Some kind of processing
         ...


# somescript.py
import sys
import csv


def main(filename):
    with open(filename) as f:
         for row in csv.reader(f):
             # Some kind of processing
             ...


main(sys.argv[1])


import math


def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result


# Test
nums = range(1000000)
for n in range(100):
    r = compute_roots(nums)


from math import sqrt


def compute_roots(nums):


    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


import math


def compute_roots(nums):
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


# Slower
class SomeClass:
    ...
    def method(self):
         for x in s:
             op(self.value)


# Faster
class SomeClass:


    ...
    def method(self):
         value = self.value
         for x in s:
             op(value)


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value


>>> from timeit import timeit
>>> a = A(1,2)
>>> timeit('a.x', 'from __main__ import a')
0.07817923510447145
>>> timeit('a.y', 'from __main__ import a')
0.35766440676525235
>>>


values = [x for x in sequence]
squares = [x*x for x in values]


squares = [x*x for x in sequence]


a = {
    'name' : 'AAPL',
    'shares' : 100,
    'price' : 534.22
}


b = dict(name='AAPL', shares=100, price=534.22)
```