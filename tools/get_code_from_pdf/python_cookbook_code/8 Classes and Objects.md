```python

CHAPTER 8


Classes and Objects


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


>>> p = Pair(3, 4)
>>> p
Pair(3, 4)         # __repr__() output
>>> print(p)
(3, 4)             # __str__() output
>>>


>>> p = Pair(3, 4)
>>> print('p is {0!r}'.format(p))
p is Pair(3, 4)
>>> print('p is {0}'.format(p))
p is (3, 4)
>>>


>>> f = open('file.dat')
>>> f
<_io.TextIOWrapper name='file.dat' mode='r' encoding='UTF-8'>
>>>


def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)


def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)


_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


>>> d = Date(2012, 12, 21)
>>> format(d)
'2012-12-21'
>>> format(d, 'mdy')
'12/21/2012'
>>> 'The date is {:ymd}'.format(d)
'The date is 2012-12-21'
>>> 'The date is {:mdy}'.format(d)
'The date is 12/21/2012'
>>>


>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> format(d)
'2012-12-21'
>>> format(d,'%A, %B %d, %Y')
'Friday, December 21, 2012'
>>> 'The end is {:%d %b %Y}. Goodbye'.format(d)
'The end is 21 Dec 2012. Goodbye'
>>>


from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None


    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock


    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


from functools import partial


conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed


from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.connections = []


    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock


    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


# Example use
from functools import partial


conn = LazyConnection(('www.python.org', 80))
with conn as s1:
     ...
     with conn as s2:
          ...
          # s1 and s2 are independent sockets


class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class A:
    def __init__(self):
        self._internal = 0    # An internal attribute
        self.public = 1       # A public attribute


    def public_method(self):
        '''
        A public method
        '''
        ...


    def _internal_method(self):
        ...


class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        ...
    def public_method(self):
        ...
        self.__private_method()
        ...


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1      # Does not override B.__private
    # Does not override B.__private_method()
    def __private_method(self):
        ...


lambda_ = 2.0     # Trailing _ to avoid clash with lambda keyword


class Person:
    def __init__(self, first_name):
        self.first_name = first_name


    # Getter function
    @property
    def first_name(self):
        return self._first_name


    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value


    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


>>> a = Person('Guido')
>>> a.first_name       # Calls the getter
'Guido'
>>> a.first_name = 42  # Calls the setter
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "prop.py", line 14, in first_name
    raise TypeError('Expected a string')
TypeError: Expected a string
>>> del a.first_name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't delete attribute
>>>


class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)


    # Getter function
    def get_first_name(self):
        return self._first_name


    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value


    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")


    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


>>> Person.first_name.fget
<function Person.first_name at 0x1006a60e0>
>>> Person.first_name.fset
<function Person.first_name at 0x1006a6170>
>>> Person.first_name.fdel
<function Person.first_name at 0x1006a62e0>
>>>


class Person:
    def __init__(self, first_name):
        self.first_name = name
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        self._first_name = value


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


>>> c = Circle(4.0)
>>> c.radius
4.0
>>> c.area           # Notice lack of ()
50.26548245743669
>>> c.perimeter      # Notice lack of ()
25.132741228718345
>>>


>>> p = Person('Guido')
>>> p.get_first_name()
'Guido'
>>> p.set_first_name('Larry')
>>>


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @property
    def first_name(self):
        return self._first_name


    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value


    # Repeated property code, but for a different name (bad!)
    @property
    def last_name(self):
        return self._last_name


    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._last_name = value


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()      # Call parent spam()


class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


class Proxy:
    def __init__(self, obj):
        self._obj = obj


    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)


    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)    # Call original __setattr__
        else:
            setattr(self._obj, name, value)


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')


class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')


class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')


>>> c = C()
Base.__init__
A.__init__
Base.__init__


B.__init__
C.__init__
>>>


class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A,B):
    def __init__(self):
        super().__init__()     # Only one call to super() here
        print('C.__init__')


>>> c = C()
Base.__init__
B.__init__
A.__init__
C.__init__
>>>


>>> C.__mro__
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>,
<class '__main__.Base'>, <class 'object'>)
>>>


• Child classes get checked before parents
• Multiple parents get checked in the order listed.
• If there are two valid choices for the next class, pick the one from the first parent.


class A:
    def spam(self):
        print('A.spam')
        super().spam()


>>> a = A()
>>> a.spam()
A.spam
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in spam
AttributeError: 'super' object has no attribute 'spam'
>>>


>>> class B:
...     def spam(self):
...         print('B.spam')
...
>>> class C(A,B):
...     pass
...
>>> c = C()
>>> c.spam()
A.spam
B.spam
>>>


>>> C.__mro__
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>,
<class 'object'>)
>>>


class Person:
    def __init__(self, name):
        self.name = name


    # Getter function
    @property
    def name(self):
        return self._name


    # Setter function
    @name.setter


    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value


    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name


    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


>>> s = SubPerson('Guido')
Setting name to Guido
>>> s.name
Getting name
'Guido'
>>> s.name = 'Larry'
Setting name to Larry
>>> s.name = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 16, in name
       raise TypeError('Expected a string')
TypeError: Expected a string
>>>


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


class SubPerson(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


class SubPerson(Person):
    @property              # Doesn't work
    def name(self):
        print('Getting name')
        return super().name


>>> s = SubPerson('Guido')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 5, in __init__
    self.name = name
AttributeError: can't set attribute
>>>


class SubPerson(Person):
    @Person.getter
    def name(self):
        print('Getting name')
        return super().name


>>> s = SubPerson('Guido')
>>> s.name
Getting name
'Guido'
>>> s.name = 'Larry'
>>> s.name
Getting name
'Larry'
>>> s.name = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 16, in name
    raise TypeError('Expected a string')
TypeError: Expected a string
>>>


# A descriptor
class String:
    def __init__(self, name):
        self.name = name


    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value


# A class with a descriptor
class Person:
    name = String('name')
    def __init__(self, name):
        self.name = name


# Extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):


        print('Getting name')
        return super().name


    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name


    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


>>> p = Point(2, 3)
>>> p.x           # Calls Point.x.__get__(p,Point)
2
>>> p.y = 5       # Calls Point.y.__set__(p, 5)
>>> p.x = 2.3     # Calls Point.x.__set__(p, 2.3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "descrip.py", line 12, in __set__
    raise TypeError('Expected an int')
TypeError: Expected an int
>>>


# Does NOT work
class Point:


    def __init__(self, x, y):
        self.x = Integer('x')    # No! Must be a class variable
        self.y = Integer('y')
        self.x = x
        self.y = y


# Descriptor attribute for an integer type-checked attribute
class Integer:
    ...
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    ...


>>> p = Point(2,3)
>>> p.x      # Calls Point.x.__get__(p, Point)
2
>>> Point.x  # Calls Point.x.__get__(None, Point)
<__main__.Integer object at 0x100671890>
>>>


# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type


    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


class lazyproperty:
    def __init__(self, func):
        self.func = func


    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:


            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius


    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2


    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


>>> c = Circle(4.0)
>>> c.radius
4.0
>>> c.area
Computing area
50.26548245743669
>>> c.area
50.26548245743669
>>> c.perimeter
Computing perimeter
25.132741228718345
>>> c.perimeter
25.132741228718345
>>>


>>> c = Circle(4.0)
>>> # Get instance variables
>>> vars(c)
{'radius': 4.0}


>>> # Compute area and observe variables afterward
>>> c.area
Computing area
50.26548245743669
>>> vars(c)
{'area': 50.26548245743669, 'radius': 4.0}


>>> # Notice access doesn't invoke property anymore
>>> c.area
50.26548245743669


>>> # Delete the variable and see property trigger again
>>> del c.area
>>> vars(c)
{'radius': 4.0}
>>> c.area
Computing area
50.26548245743669
>>>


>>> c.area
Computing area
50.26548245743669
>>> c.area = 25
>>> c.area
25
>>>


def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:


            value = func(self)
            setattr(self, name, value)
            return value
    return lazy


>>> c = Circle(4.0)
>>> c.area
Computing area
50.26548245743669
>>> c.area
50.26548245743669
>>> c.area = 25
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>>


class Structure:
    # Class variable that specifies expected fields
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))


        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# Example class definitions
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']


    class Point(Structure):
        _fields = ['x','y']


    class Circle(Structure):
        _fields = ['radius']
        def area(self):
            return math.pi * self.radius ** 2


>>> s = Stock('ACME', 50, 91.1)
>>> p = Point(2, 3)
>>> c = Circle(4.5)
>>> s2 = Stock('ACME', 50)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 6, in __init__
    raise TypeError('Expected {} arguments'.format(len(self._fields)))
TypeError: Expected 3 arguments


class Structure:
    _fields= []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))


        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))


        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


# Example use
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']


    s1 = Stock('ACME', 50, 91.1)


    s2 = Stock('ACME', 50, price=91.1)
    s3 = Stock('ACME', shares=50, price=91.1)


class Structure:
    # Class variable that specifies expected fields
    _fields= []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))


        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


# Example use
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']


    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, 91.1, date='8/2/2012')


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2


class Structure:
    # Class variable that specifies expected fields
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))


        # Set the arguments (alternate)
        self.__dict__.update(zip(self._fields,args))


>>> help(Stock)
Help on class Stock in module __main__:


class Stock(Structure)
...
 |  Methods inherited from Structure:
 |
 |  __init__(self, *args, **kwargs)
 |
...
>>>


def init_fromlocals(self):
    import sys
    locs = sys._getframe(1).f_locals
    for k, v in locs.items():
        if k != 'self':
            setattr(self, k, v)


class Stock:
    def __init__(self, name, shares, price):
        init_fromlocals(self)


from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass


a = IStream()   # TypeError: Can't instantiate abstract class
                # IStream with abstract methods read, write


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        ...
    def write(self, data):
        ...


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    ...


import io


# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)


# Open a normal file and type check
f = open('foo.txt')
isinstance(f, IStream)      # Returns True


from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass


    @name.setter
    @abstractmethod
    def name(self, value):
        pass


    @classmethod
    @abstractmethod
    def method1(cls):
        pass


    @staticmethod
    @abstractmethod
    def method2():
        pass


import collections


# Check if x is a sequence
if isinstance(x, collections.Sequence):
    ...


# Check if x is iterable
if isinstance(x, collections.Iterable):
    ...


# Check if x has a size
if isinstance(x, collections.Sized):
    ...


# Check if x is a mapping
if isinstance(x, collections.Mapping):
    ...


from decimal import Decimal
import numbers


x = Decimal('3.4')
isinstance(x, numbers.Real)   # Returns False


# Base class. Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)


    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)


    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)


    def __set__(self, instance, value):
        if len(value) >= self.size:


            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


class Stock:
    # Specify constraints
    name = SizedString('name',size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


>>> s = Stock('ACME', 50, 91.1)
>>> s.name
'ACME'
>>> s.shares = 75
>>> s.shares = -10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 17, in __set__
    super().__set__(instance, value)
  File "example.py", line 23, in __set__
    raise ValueError('Expected >= 0')
ValueError: Expected >= 0
>>> s.price = 'a lot'


Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 16, in __set__
    raise TypeError('expected ' + str(self.expected_type))
TypeError: expected <class 'float'>
>>> s.name = 'ABRACADABRA'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 17, in __set__
    super().__set__(instance, value)
  File "example.py", line 35, in __set__
    raise ValueError('size must be < ' + str(self.size))
ValueError: size must be < 8
>>>


# Class decorator to apply constraints
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate


# Example
@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


# Example
class Stock(metaclass=checkedmeta):
    name   = SizedString(size=8)
    shares = UnsignedInteger()
    price  = UnsignedFloat()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# Normal
class Point:
    x = Integer('x')
    y = Integer('y')


# Metaclass
class Point(metaclass=checkedmeta):
    x = Integer()
    y = Integer()


# Base class. Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)


    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Decorator for applying type checking
def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)


    super_set = cls.__set__
    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('expected ' + str(expected_type))
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls


# Decorator for unsigned values
def Unsigned(cls):
    super_set = cls.__set__


    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls


# Decorator for allowing sized values
def MaxSized(cls):
    super_init = cls.__init__
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)
    cls.__init__ = __init__


    super_set = cls.__set__
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls


# Specialized descriptors
@Typed(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass


import collections


class A(collections.Iterable):
    pass


>>> a = A()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class A with abstract methods __iter__
>>>


>>> import collections
>>> collections.Sequence()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 


__getitem__, __len__
>>>


import collections
import bisect


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is None else []


    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]


    def __len__(self):
        return len(self._items)


    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


>>> items = SortedItems([5, 1, 3])
>>> list(items)
[1, 3, 5]
>>> items[0]
1
>>> items[-1]
5
>>> items.add(2)
>>> list(items)
[1, 2, 3, 5]
>>> items.add(-10)
>>> list(items)
[-10, 1, 2, 3, 5]
>>> items[1:4]
[1, 2, 3]
>>> 3 in items
True
>>> len(items)
5
>>> for n in items:
...     print(n)
...
-10
1
2
3


5
>>>


>>> items = SortedItems()
>>> import collections
>>> isinstance(items, collections.Iterable)
True
>>> isinstance(items, collections.Sequence)
True
>>> isinstance(items, collections.Container)
True
>>> isinstance(items, collections.Sized)
True
>>> isinstance(items, collections.Mapping)
False
>>>


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is None else []


    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]


    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value


    def __delitem__(self, index):


        print('Deleting:', index)
        del self._items[index]


    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)


    def __len__(self):
        print('Len')
        return len(self._items)


>>> a = Items([1, 2, 3])
>>> len(a)
Len
3
>>> a.append(4)
Len
Inserting: 3 4
>>> a.append(2)
Len
Inserting: 4 2
>>> a.count(2)
Getting: 0
Getting: 1
Getting: 2
Getting: 3
Getting: 4
Getting: 5
2
>>> a.remove(3)
Getting: 0
Getting: 1
Getting: 2
Deleting: 2
>>>


class A:
    def spam(self, x):
        pass


    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()


    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)


    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()


    def bar(self):
        pass


class A:
    def spam(self, x):
        pass


    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()


    def bar(self):
        pass


    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        return getattr(self._a, name)


b = B()
b.bar()    # Calls B.bar() (exists on B)
b.spam(42) # Calls B.__getattr__('spam') and delegates to A.spam


# A proxy class that wraps around another object, but
# exposes its public attributes


class Proxy:
    def __init__(self, obj):
        self._obj = obj


    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)


    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)


    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x
    def bar(self, y):
        print('Spam.bar:', self.x, y)


# Create an instance
s = Spam(2)


# Create a proxy around it
p = Proxy(s)


# Access the proxy
print(p.x)     # Outputs 2
p.bar(3)       # Outputs "Spam.bar: 2 3"
p.x = 37       # Changes s.x to 37


class A:
    def spam(self, x):
        print('A.spam', x)


    def foo(self):
        print('A.foo')


class B(A):
    def spam(self, x):
        print('B.spam')
        super().spam(x)


    def bar(self):
        print('B.bar')


class A:
    def spam(self, x):
        print('A.spam', x)


    def foo(self):
        print('A.foo')


class B:
    def __init__(self):
        self._a = A()


    def spam(self, x):
        print('B.spam', x)
        self._a.spam(x)


    def bar(self):
        print('B.bar')


    def __getattr__(self, name):
        return getattr(self._a, name)


class ListLike:
    def __init__(self):
        self._items = []
    def __getattr__(self, name):
        return getattr(self._items, name)


>>> a = ListLike()
>>> a.append(2)
>>> a.insert(0, 1)
>>> a.sort()
>>> len(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'ListLike' has no len()
>>> a[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'ListLike' object does not support indexing
>>>


class ListLike:
    def __init__(self):
        self._items = []
    def __getattr__(self, name):
        return getattr(self._items, name)


    # Added special methods to support certain list operations
    def __len__(self):
        return len(self._items)
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        self._items[index] = value
    def __delitem__(self, index):
        del self._items[index]


import time


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)      # Primary
b = Date.today()            # Alternate


class NewDate(Date):
    pass


c = Date.today()      # Creates an instance of Date (cls=Date)
d = NewDate.today()   # Creates an instance of NewDate (cls=NewDate)


class Date:
    def __init__(self, *args):
        if len(args) == 0:
            t = time.localtime()
            args = (t.tm_year, t.tm_mon, t.tm_mday)
        self.year, self.month, self.day = args


a = Date(2012, 12, 21)   # Clear. A specific date.
b = Date()               # ??? What does this do?


# Class method version
c = Date.today()         # Clear. Today's date.


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


>>> d = Date.__new__(Date)
>>> d
<__main__.Date object at 0x1006716d0>
>>> d.year
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Date' object has no attribute 'year'
>>>


>>> data = {'year':2012, 'month':8, 'day':29}
>>> for key, value in data.items():
...     setattr(d, key, value)
...
>>> d.year
2012
>>> d.month
8
>>>


from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


data = { 'year': 2012, 'month': 8, 'day': 29 }


class LoggedMappingMixin:
    '''
    Add logging to get/set/delete operations for debugging.
    '''
    __slots__ = ()


    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)


    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)


    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    '''
    Only allow a key to be set once.
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    '''
    Restrict keys to strings only
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)


>>> class LoggedDict(LoggedMappingMixin, dict):
...     pass
...
>>> d = LoggedDict()
>>> d['x'] = 23
Setting x = 23


>>> d['x']
Getting x
23
>>> del d['x']
Deleting x


>>> from collections import defaultdict
>>> class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
...     pass
...
>>> d = SetOnceDefaultDict(list)
>>> d['x'].append(2)
>>> d['y'].append(3)
>>> d['x'].append(10)
>>> d['x'] = 23
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mixin.py", line 24, in __setitem__
    raise KeyError(str(key) + ' already set')
KeyError: 'x already set'


>>> from collections import OrderedDict
>>> class StringOrderedDict(StringKeysMappingMixin,
...                         SetOnceMappingMixin,
...                         OrderedDict):
...     pass
...
>>> d = StringOrderedDict()
>>> d['x'] = 23
>>> d[42] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mixin.py", line 45, in __setitem__
    '''
TypeError: keys must be strings
>>> d['x'] = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mixin.py", line 46, in __setitem__
    __slots__ = ()
  File "mixin.py", line 24, in __setitem__
    if key in self:
KeyError: 'x already set'
>>>


from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


class RestrictKeysMixin:
    def __init__(self, *args, _restrict_key_type, **kwargs):
        self.__restrict_key_type = _restrict_key_type
        super().__init__(*args, **kwargs)


    def __setitem__(self, key, value):
        if not isinstance(key, self.__restrict_key_type):
            raise TypeError('Keys must be ' + str(self.__restrict_key_type))
        super().__setitem__(key, value)


>>> class RDict(RestrictKeysMixin, dict):
...     pass
...
>>> d = RDict(_restrict_key_type=str)
>>> e = RDict([('name','Dave'), ('n',37)], _restrict_key_type=str)
>>> f = RDict(name='Dave', n=37, _restrict_key_type=str)
>>> f
{'n': 37, 'name': 'Dave'}
>>> f[42] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mixin.py", line 83, in __setitem__
    raise TypeError('Keys must be ' + str(self.__restrict_key_type))
TypeError: Keys must be <class 'str'>
>>>


class LoggedDict(LoggedMappingMixin, dict):
    pass


def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__


    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)


    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)


    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)


    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


@LoggedMapping
class LoggedDict(dict):
    pass


class Connection:
    def __init__(self):


        self.state = 'CLOSED'


    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('reading')


    def write(self, data):
        if self.state != 'OPEN':
           raise RuntimeError('Not open')
        print('writing')


    def open(self):
        if self.state == 'OPEN':
           raise RuntimeError('Already open')
        self.state = 'OPEN'


    def close(self):
        if self.state == 'CLOSED':
           raise RuntimeError('Already closed')
        self.state = 'CLOSED'


class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)


    def new_state(self, newstate):
        self._state = newstate


    # Delegate to the state class
    def read(self):
        return self._state.read(self)


    def write(self, data):
        return self._state.write(self, data)


    def open(self):
        return self._state.open(self)


    def close(self):
        return self._state.close(self)


# Connection state base class
class ConnectionState:


    @staticmethod
    def read(conn):
        raise NotImplementedError()


    @staticmethod
    def write(conn, data):
        raise NotImplementedError()


    @staticmethod
    def open(conn):
        raise NotImplementedError()


    @staticmethod
    def close(conn):
        raise NotImplementedError()


# Implementation of different states
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')


    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')


    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)


    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')


    @staticmethod
    def write(conn, data):
        print('writing')


    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')


    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


>>> c = Connection()
>>> c._state
<class '__main__.ClosedConnectionState'>
>>> c.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 10, in read
    return self._state.read(self)
  File "example.py", line 43, in read
    raise RuntimeError('Not open')
RuntimeError: Not open
>>> c.open()
>>> c._state
<class '__main__.OpenConnectionState'>
>>> c.read()
reading
>>> c.write('hello')
writing
>>> c.close()
>>> c._state
<class '__main__.ClosedConnectionState'>
>>>


class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)


    def new_state(self, newstate):
        self.__class__ = newstate


    def read(self):


        raise NotImplementedError()


    def write(self, data):
        raise NotImplementedError()


    def open(self):
        raise NotImplementedError()


    def close(self):
        raise NotImplementedError()


class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('Not open')


    def write(self, data):
        raise RuntimeError('Not open')


    def open(self):
        self.new_state(OpenConnection)


    def close(self):
        raise RuntimeError('Already closed')


class OpenConnection(Connection):
    def read(self):
        print('reading')


    def write(self, data):
        print('writing')


    def open(self):
        raise RuntimeError('Already open')


    def close(self):
        self.new_state(ClosedConnection)


>>> c = Connection()
>>> c
<__main__.ClosedConnection object at 0x1006718d0>
>>> c.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "state.py", line 15, in read
    raise RuntimeError('Not open')
RuntimeError: Not open
>>> c.open()


>>> c
<__main__.OpenConnection object at 0x1006718d0>
>>> c.read()
reading
>>> c.close()
>>> c
<__main__.ClosedConnection object at 0x1006718d0>
>>>


# Original implementation
class State:
    def __init__(self):
        self.state = 'A'
    def action(self, x):
        if state == 'A':
            # Action for A
            ...
            state = 'B'
        elif state == 'B':
            # Action for B
            ...
            state = 'C'
        elif state == 'C':
            # Action for C
            ...
            state = 'A'


# Alternative implementation
class State:
    def __init__(self):
        self.new_state(State_A)


    def new_state(self, state):
        self.__class__ = state


    def action(self, x):
        raise NotImplementedError()


class State_A(State):
    def action(self, x):
         # Action for A
         ...
         self.new_state(State_B)


class State_B(State):
    def action(self, x):
         # Action for B
         ...
         self.new_state(State_C)


class State_C(State):
    def action(self, x):
         # Action for C
         ...
         self.new_state(State_A)


import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)


    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)     # Calls p.distance(0, 0)


import operator
operator.methodcaller('distance', 0, 0)(p)


points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]


# Sort by distance from origin (0, 0)
points.sort(key=operator.methodcaller('distance', 0, 0))


>>> p = Point(3, 4)
>>> d = operator.methodcaller('distance', 0, 0)
>>> d(p)
5.0
>>>


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


# Representation of 1 + 2 * (3 - 4) / 5
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)


class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)


    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value


    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)


    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)


    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)


    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)


    def visit_Negate(self, node):
        return -node.operand


>>> e = Evaluator()
>>> e.visit(t4)
0.6
>>>


class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions


    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))


    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))


    def visit_Add(self, node):
        self.binop(node, 'ADD')


    def visit_Sub(self, node):
        self.binop(node, 'SUB')


    def visit_Mul(self, node):
        self.binop(node, 'MUL')


    def visit_Div(self, node):
        self.binop(node, 'DIV')


    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction,))


    def visit_Negate(self, node):
        self.unaryop(node, 'NEG')


>>> s = StackCode()
>>> s.generate_code(t4)
[('PUSH', 1), ('PUSH', 2), ('PUSH', 3), ('PUSH', 4), ('SUB',),
 ('MUL',), ('PUSH', 5), ('DIV',), ('ADD',)]
>>>


class NodeVisitor:
    def visit(self, node):
        nodetype = type(node).__name__
        if nodetype == 'Number':


            return self.visit_Number(node)
        elif nodetype == 'Add':
            return self.visit_Add(node)
        elif nodetype == 'Sub':
            return self.visit_Sub(node)
        ...


class Evaluator(NodeVisitor):
    ...
    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)


class HTTPHandler:
    def handle(self, request):
        methname = 'do_' + request.request_method
        getattr(self, methname)(request)


    def do_GET(self, request):
        ...
    def do_POST(self, request):
        ...
    def do_HEAD(self, request):
        ...


import types


class Node:
    pass


import types
class NodeVisitor:
    def visit(self, node):
        stack = [ node ]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result


    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)


    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


# A sample visitor class that evaluates expressions
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value


    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)


    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)


    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)


    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)


    def visit_Negate(self, node):
        return -self.visit(node.operand)


if __name__ == '__main__':
    # 1 + 2*(3-4) / 5
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)


    # Evaluate it
    e = Evaluator()
    print(e.visit(t4))     # Outputs 0.6


>>> a = Number(0)
>>> for n in range(1, 100000):
...     a = Add(a, Number(n))
...
>>> e = Evaluator()
>>> e.visit(a)
Traceback (most recent call last):
...
  File "visitor.py", line 29, in _visit
    return meth(node)
  File "visitor.py", line 67, in visit_Add
    return self.visit(node.left) + self.visit(node.right)
RuntimeError: maximum recursion depth exceeded
>>>


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value


    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)


    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)


    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)


    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)


    def visit_Negate(self, node):
        yield -(yield node.operand)


>>> a = Number(0)
>>> for n in range(1,100000):
...     a = Add(a, Number(n))
...
>>> e = Evaluator()
>>> e.visit(a)
4999950000
>>>


class Evaluator(NodeVisitor):
    ...
    def visit_Add(self, node):
        print('Add:', node)
        lhs = yield node.left
        print('left=', lhs)
        rhs = yield node.right
        print('right=', rhs)
        yield lhs + rhs
    ...


>>> e = Evaluator()
>>> e.visit(t4)
Add: <__main__.Add object at 0x1006a8d90>
left= 1
right= -0.4
0.6
>>>


value = self.visit(node.left)


value = yield node.left


value = yield node.left


try:
    last = stack[-1]
    if isinstance(last, types.GeneratorType):
        stack.append(last.send(last_result))
        last_result = None
    elif isinstance(last, Node):
        stack.append(self._visit(stack.pop()))
    else:
        last_result = stack.pop()


except StopIteration:
    stack.pop()


class Visit:
    def __init__(self, node):
        self.node = node


class NodeVisitor:
    def visit(self, node):
        stack = [ Visit(node) ]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Visit):
                    stack.append(self._visit(stack.pop().node))
                else:
                    last_result = stack.pop()
            except StopIteration:


                stack.pop()
        return last_result


    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)


    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class Evaluator(NodeVisitor):
    ...
    def visit_Add(self, node):
        yield (yield Visit(node.left)) + (yield Visit(node.right))


    def visit_Sub(self, node):
        yield (yield Visit(node.left)) - (yield Visit(node.right))
    ...


import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []


    def __repr__(self):
        return 'Node({!r:})'.format(self.value)


    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()


    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)


    def add_child(self, child):
        self.children.append(child)
        child.parent = self


>>> root = Node('parent')
>>> c1 = Node('child')
>>> root.add_child(c1)
>>> print(c1.parent)
Node('parent')
>>> del root
>>> print(c1.parent)
None
>>>


# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')


# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None


        self.children = []
    def add_child(self, child):
        self.children.append(child)
        child.parent = self


>>> a = Data()
>>> del a               # Immediately deleted
Data.__del__
>>> a = Node()
>>> del a               # Immediately deleted
Data.__del__
>>> a = Node()
>>> a.add_child(Node())
>>> del a               # Not deleted (no message)
>>>


>>> import gc
>>> gc.collect()     # Force collection
Data.__del__
Data.__del__
>>>


# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')


# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []


    # NEVER DEFINE LIKE THIS.


    # Only here to illustrate pathological behavior
    def __del__(self):
        del self.data
        del.parent
        del.children


    def add_child(self, child):
        self.children.append(child)
        child.parent = self


>>> a = Node()
>>> a.add_child(Node()
>>> del a             # No message (not collected)
>>> import gc
>>> gc.collect()      # No message (not collected)
>>>


>>> import weakref
>>> a = Node()
>>> a_ref = weakref.ref(a)
>>> a_ref
<weakref at 0x100581f70; to 'Node' at 0x1005c5410>
>>>


>>> print(a_ref())
<__main__.Node object at 0x1005c5410>
>>> del a
Data.__del__
>>> print(a_ref())
None
>>>


from functools import total_ordering
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()


    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)


    def add_room(self, room):
        self.rooms.append(room)


    def __str__(self):
        return '{}: {} square foot {}'.format(self.name,
                                              self.living_space_footage,
                                              self.style)


    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage


    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


# Build a few houses, and add rooms to them
h1 = House('h1', 'Cape')
h1.add_room(Room('Master Bedroom', 14, 21))
h1.add_room(Room('Living Room', 18, 20))
h1.add_room(Room('Kitchen', 12, 16))
h1.add_room(Room('Office', 12, 12))


h2 = House('h2', 'Ranch')
h2.add_room(Room('Master Bedroom', 14, 21))
h2.add_room(Room('Living Room', 18, 20))
h2.add_room(Room('Kitchen', 12, 16))


h3 = House('h3', 'Split')
h3.add_room(Room('Master Bedroom', 14, 21))
h3.add_room(Room('Living Room', 18, 20))
h3.add_room(Room('Office', 12, 16))
h3.add_room(Room('Kitchen', 15, 17))
houses = [h1, h2, h3]


print('Is h1 bigger than h2?', h1 > h2) # prints True
print('Is h2 smaller than h3?', h2 < h3) # prints True
print('Is h2 greater than or equal to h1?', h2 >= h1) # Prints False
print('Which one is biggest?', max(houses)) # Prints 'h3: 1101-square-foot Split'
print('Which is smallest?', min(houses)) # Prints 'h2: 846-square-foot Ranch'


class House:
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...


    # Methods created by @total_ordering
    __le__ = lambda self, other: self < other or self == other
    __gt__ = lambda self, other: not (self < other or self == other)
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not self == other


>>> import logging
>>> a = logging.getLogger('foo')
>>> b = logging.getLogger('bar')
>>> a is b
False
>>> c = logging.getLogger('foo')
>>> a is c
True
>>>


# The class in question
class Spam:
    def __init__(self, name):
        self.name = name


# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:


        s = _spam_cache[name]
    return s


>>> a = get_spam('foo')
>>> b = get_spam('bar')
>>> a is b
False
>>> c = get_spam('foo')
>>> a is c
True
>>>


# Note: This code doesn't quite work
import weakref


class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self


    def __init__(self, name):
        print('Initializing Spam')
        self.name = name


>>> s = Spam('Dave')
Initializing Spam
>>> t = Spam('Dave')
Initializing Spam
>>> s is t
True
>>>


>>> a = get_spam('foo')
>>> b = get_spam('bar')
>>> c = get_spam('foo')
>>> list(_spam_cache)
['foo', 'bar']
>>> del a
>>> del c
>>> list(_spam_cache)
['bar']
>>> del b
>>> list(_spam_cache)
[]
>>>


import weakref


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s


    def clear(self):
        self._cache.clear()


class Spam:
    manager = CachedSpamManager()


    def __init__(self, name):
        self.name = name


def get_spam(name):
    return Spam.manager.get_spam(name)


>>> a = Spam('foo')
>>> b = Spam('foo')
>>> a is b
False
>>>


class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")


    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name


import weakref


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)          # Modified creation


            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
```