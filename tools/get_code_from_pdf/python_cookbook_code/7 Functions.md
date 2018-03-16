```python

CHAPTER 7


Functions


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# Sample use
avg(1, 2)          # 1.5
avg(1, 2, 3, 4)    # 2.5


import html


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                  name=name,
                  attrs=attr_str,
                  value=html.escape(value))
    return element


# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
make_element('item', 'Albatross', size='large', quantity=6)


# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')


def anyargs(*args, **kwargs):
    print(args)      # A tuple
    print(kwargs)    # A dict


def a(x, *args, y):
    pass


def b(x, *args, y, **kwargs):
    pass


def recv(maxsize, *, block):
    'Receives a message'
    pass


recv(1024, True)        #  TypeError
recv(1024, block=True)  # Ok


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


minimum(1, 5, 2, -5, 10)          # Returns -5
minimum(1, 5, 2, -5, 10, clip=0)  # Returns 0


msg = recv(1024, False)


msg = recv(1024, block=False)


>>> help(recv)
Help on function recv in module __main__:


recv(maxsize, *, block)
    Receives a message


def add(x:int, y:int) -> int:
    return x + y


>>> help(add)
Help on function add in module __main__:


add(x: int, y: int) -> int
>>>


>>> add.__annotations__
{'y': <class 'int'>, 'return': <class 'int'>, 'x': <class 'int'>}


>>> def myfun():
...     return 1, 2, 3
...
>>> a, b, c = myfun()
>>> a
1
>>> b
2
>>> c
3


>>> a = (1, 2)     # With parentheses
>>> a
(1, 2)
>>> b = 1, 2       # Without parentheses
>>> b
(1, 2)
>>>


>>> x = myfun()
>>> x


(1, 2, 3)
>>>


def spam(a, b=42):
    print(a, b)


spam(1)      # Ok. a=1, b=42
spam(1, 2)   # Ok. a=1, b=2


# Using a list as a default value
def spam(a, b=None):
    if b is None:
        b = []
    ...


_no_value = object()


def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    ...


>>> spam(1)
No b value supplied
>>> spam(1, 2)     # b = 2
>>> spam(1, None)  # b = None
>>>


>>> x = 42
>>> def spam(a, b=x):
...     print(a, b)
...
>>> spam(1)
1 42
>>> x = 23     # Has no effect
>>> spam(1)
1 42
>>>


def spam(a, b=[]):     # NO!
    ...


>>> def spam(a, b=[]):
...     print(b)
...     return b
...
>>> x = spam(1)
>>> x
[]
>>> x.append(99)
>>> x.append('Yow!')
>>> x
[99, 'Yow!']
>>> spam(1)       # Modified list gets returned!
[99, 'Yow!']
>>>


def spam(a, b=None):
    if not b:      # NO! Use 'b is None' instead
        b = []
    ...


>>> spam(1)        # OK
>>> x = []
>>> spam(1, x)     # Silent error. x value overwritten by default
>>> spam(1, 0)     # Silent error. 0 ignored
>>> spam(1, '')    # Silent error. '' ignored
>>>


>>> add = lambda x, y: x + y
>>> add(2,3)
5
>>> add('hello', 'world')
'helloworld'
>>>


>>> def add(x, y):
...     return x + y
...
>>> add(2,3)
5
>>>


>>> names = ['David Beazley', 'Brian Jones',
...           'Raymond Hettinger', 'Ned Batchelder']
>>> sorted(names, key=lambda name: name.split()[-1].lower())
['Ned Batchelder', 'David Beazley', 'Raymond Hettinger', 'Brian Jones']
>>>


>>> x = 10
>>> a = lambda y: x + y
>>> x = 20
>>> b = lambda y: x + y
>>>


>>> a(10)
30
>>> b(10)
30
>>>


>>> x = 15
>>> a(10)
25
>>> x = 3
>>> a(10)
13
>>>


>>> x = 10
>>> a = lambda y, x=x: x + y
>>> x = 20
>>> b = lambda y, x=x: x + y
>>> a(10)
20
>>> b(10)
30
>>>


>>> funcs = [lambda x: x+n for n in range(5)]
>>> for f in funcs:
...     print(f(0))
...
4
4
4
4
4
>>>


>>> funcs = [lambda x, n=n: x+n for n in range(5)]
>>> for f in funcs:
...     print(f(0))
...
0
1
2
3
4
>>>


def spam(a, b, c, d):
    print(a, b, c, d)


>>> from functools import partial
>>> s1 = partial(spam, 1)       # a = 1
>>> s1(2, 3, 4)
1 2 3 4
>>> s1(4, 5, 6)
1 4 5 6
>>> s2 = partial(spam, d=42)    # d = 42
>>> s2(1, 2, 3)
1 2 3 42
>>> s2(4, 5, 5)
4 5 5 42
>>> s3 = partial(spam, 1, 2, d=42) # a = 1, b = 2, d = 42
>>> s3(3)
1 2 3 42
>>> s3(4)
1 2 4 42
>>> s3(5)
1 2 5 42
>>>


points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]


import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


>>> pt = (4, 3)
>>> points.sort(key=partial(distance,pt))
>>> points
[(3, 4), (1, 2), (5, 6), (7, 8)]
>>>


def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)


# A sample function
def add(x, y):
    return x + y


if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial


    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')


    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()


from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)


serv = TCPServer(('', 15000), EchoHandler)
serv.serve_forever()


class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)


Exception happened during processing of request from ('127.0.0.1', 59834)
Traceback (most recent call last):
 ...
TypeError: __init__() missing 1 required keyword-only argument: 'ack'


from functools import partial
serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
serv.serve_forever()


points.sort(key=lambda p: distance(pt, p))


p.apply_async(add, (3, 4), callback=lambda result: output_result(result,log))


serv = TCPServer(('', 15000),
                 lambda *args, **kwargs: EchoHandler(*args,
                                                     ack=b'RECEIVED:',
                                                     **kwargs))


from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template
    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# Example use. Download stock data from yahoo
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener


# Example use
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)


    # Invoke the callback with the result
    callback(result)


>>> def print_result(result):
...     print('Got:', result)
...
>>> def add(x, y):
...     return x + y
...
>>> apply_async(add, (2, 3), callback=print_result)
Got: 5
>>> apply_async(add, ('hello', 'world'), callback=print_result)
Got: helloworld
>>>


class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


>>> r = ResultHandler()
>>> apply_async(add, (2, 3), callback=r.handler)
[1] Got: 5
>>> apply_async(add, ('hello', 'world'), callback=r.handler)
[2] Got: helloworld
>>>


def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler


>>> handler = make_handler()
>>> apply_async(add, (2, 3), callback=handler)
[1] Got: 5
>>> apply_async(add, ('hello', 'world'), callback=handler)
[2] Got: helloworld
>>>


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


>>> handler = make_handler()
>>> next(handler)        # Advance to the yield


>>> apply_async(add, (2, 3), callback=handler.send)
[1] Got: 5
>>> apply_async(add, ('hello', 'world'), callback=handler.send)
[2] Got: helloworld
>>>


>>> class SequenceNo:
...     def __init__(self):
...         self.sequence = 0
...
>>> def handler(result, seq):
...     seq.sequence += 1
...     print('[{}] Got: {}'.format(seq.sequence, result))
...
>>> seq = SequenceNo()
>>> from functools import partial
>>> apply_async(add, (2, 3), callback=partial(handler, seq=seq))
[1] Got: 5
>>> apply_async(add, ('hello', 'world'), callback=partial(handler, seq=seq))
[2] Got: helloworld
>>>


>>> apply_async(add, (2, 3), callback=lambda r: handler(r, seq))
[1] Got: 5
>>>


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)


    # Invoke the callback with the result
    callback(result)


from queue import Queue
from functools import wraps


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


def add(x, y):
    return x + y


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')


5
helloworld
0
2
4
6
8
10
12
14
16
18
Goodbye


if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async


    # Run the test function
    test()


def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)


    # Accessor methods for n
    def get_n():
        return n


    def set_n(value):
        nonlocal n
        n = value


    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


>>> f = sample()
>>> f()
n= 0
>>> f.set_n(10)
>>> f()
n= 10
>>> f.get_n()
10
>>>


import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals


        # Update instance dictionary with callables
        self.__dict__.update((key,value) for key, value in locals.items()
                             if callable(value) )
    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()


# Example use
def Stack():
    items = []


    def push(item):
        items.append(item)


    def pop():
        return items.pop()


    def __len__():
        return len(items)


    return ClosureInstance()


>>> s = Stack()
>>> s
<__main__.ClosureInstance object at 0x10069ed10>
>>> s.push(10)
>>> s.push(20)
>>> s.push('Hello')
>>> len(s)
3
>>> s.pop()
'Hello'


>>> s.pop()
20
>>> s.pop()
10
>>>


class Stack2:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()


    def __len__(self):
        return len(self.items)


>>> from timeit import timeit
>>> # Test involving closures
>>> s = Stack()
>>> timeit('s.push(1);s.pop()', 'from __main__ import s')
0.9874754269840196
>>> # Test involving a class
>>> s = Stack2()
>>> timeit('s.push(1);s.pop()', 'from __main__ import s')
1.0707052160287276
>>>
```