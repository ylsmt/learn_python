```python

CHAPTER 10


Modules and Packages


    graphics/
        __init__.py
        primitive/
             __init__.py
             line.py
             fill.py
             text.py
        formats/
             __init__.py
             png.py
             jpg.py


import graphics.primitive.line
from graphics.primitive import line
import graphics.formats.jpg as jpg


# graphics/formats/__init__.py


from . import jpg
from . import png


# somemodule.py


def spam():
    pass


def grok():
    pass


blah = 42


# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']


    mypackage/
        __init__.py
        A/
            __init__.py


            spam.py
            grok.py
        B/
            __init__.py
            bar.py


# mypackage/A/spam.py


from . import grok


# mypackage/A/spam.py


from ..B import bar


# mypackage/A/spam.py


from mypackage.A import grok      # OK
from . import grok                # OK
import grok                       # Error (not found)


from . import grok         # OK
import .grok               # ERROR


% python3 mypackage/A/spam.py      # Relative imports fail


% python3 -m mypackage.A.spam      # Relative imports work


# mymodule.py


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def bar(self):
        print('B.bar')


    mymodule/
        __init__.py
        a.py
        b.py


# a.py


class A:
    def spam(self):
        print('A.spam')


# b.py


from .a import A


class B(A):
    def bar(self):
        print('B.bar')


# __init__.py


from .a import A
from .b import B


>>> import mymodule
>>> a = mymodule.A()
>>> a.spam()
A.spam
>>> b = mymodule.B()
>>> b.bar()
B.bar
>>>


from mymodule.a import A
from mymodule.b import B
...


from mymodule import A, B


# __init__.py


def A():
    from .a import A
    return A()


def B():
    from .b import B
    return B()


>>> import mymodule
>>> a = mymodule.A()
>>> a.spam()
A.spam
>>>


if isinstance(x, mymodule.A):       # Error
   ...


if isinstance(x, mymodule.a.A):    # Ok
   ...


    foo-package/
        spam/
             blah.py


    bar-package/
        spam/
             grok.py


>>> import sys
>>> sys.path.extend(['foo-package', 'bar-package'])
>>> import spam.blah
>>> import spam.grok
>>>


>>> import spam
>>> spam.__path__
_NamespacePath(['foo-package/spam', 'bar-package/spam'])
>>>


    my-package/
         spam/
             custom.py


>>> import spam.custom
>>> import spam.grok
>>> import spam.blah
>>>


>>> spam.__file__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute '__file__'


>>> spam
<module 'spam' (namespace)>
>>>


>>> import spam
>>> import imp
>>> imp.reload(spam)
<module 'spam' from './spam.py'>
>>>


# spam.py


def bar():
    print('bar')


def grok():
    print('grok')


>>> import spam
>>> from spam import grok
>>> spam.bar()
bar


>>> grok()
grok
>>>


def grok():
    print('New grok')


>>> import imp
>>> imp.reload(spam)
<module 'spam' from './spam.py'>
>>> spam.bar()
bar
>>> grok()             # Notice old output
grok
>>> spam.grok()        # Notice new output
New grok
>>>


    myapplication/
         spam.py
         bar.py
         grok.py
         __main__.py


bash % python3 myapplication


    bash % ls
    spam.py    bar.py   grok.py   __main__.py
    bash % zip -r myapp.zip *.py
    bash % python3 myapp.zip
    ... output from __main__.py ...


    #!/usr/bin/env python3 /usr/local/bin/myapp.zip


mypackage/
    __init__.py
    somedata.dat
    spam.py


# spam.py


import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')


    bash % env PYTHONPATH=/some/dir:/other/dir python3
    Python 3.3.0 (default, Oct  4 2012, 10:17:33)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin


    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> sys.path
    ['', '/some/dir', '/other/dir', ...]
    >>>


    # myapplication.pth
    /some/dir
    /other/dir


import sys
sys.path.insert(0, '/some/dir')
sys.path.insert(0, '/other/dir')


import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(dirname('__file__'), 'src'))


>>> import importlib
>>> math = importlib.import_module('math')
>>> math.sin(2)
0.9092974268256817
>>> mod = importlib.import_module('urllib.request')
>>> u = mod.urlopen('http://www.python.org')
>>>


import importlib


# Same as 'from . import b'
b = importlib.import_module('.b', __package__)


testcode/
    spam.py
    fib.py
    grok/
        __init__.py
        blah.py


# spam.py
print("I'm spam")


def hello(name):
    print('Hello %s' % name)


# fib.py
print("I'm fib")


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# grok/__init__.py
print("I'm grok.__init__")


# grok/blah.py
print("I'm grok.blah")


bash % cd testcode
bash % python3 -m http.server 15000
Serving HTTP on 0.0.0.0 port 15000 ...


>>> from urllib.request import urlopen
>>> u = urlopen('http://localhost:15000/fib.py')
>>> data = u.read().decode('utf-8')
>>> print(data)
# fib.py
print("I'm fib")


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


>>>


import imp
import urllib.request
import sys


def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


>>> fib = load_module('http://localhost:15000/fib.py')
I'm fib
>>> fib.fib(10)
89
>>> spam = load_module('http://localhost:15000/spam.py')
I'm spam
>>> spam.hello('Guido')
Hello Guido
>>> fib
<module 'http://localhost:15000/fib.py' from 'http://localhost:15000/fib.py'>
>>> spam
<module 'http://localhost:15000/spam.py' from 'http://localhost:15000/spam.py'>
>>>


# urlimport.py


import sys
import importlib.abc
import imp
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser


# Debugging
import logging
log = logging.getLogger(__name__)


# Get links from a given URL
def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                attrs = dict(attrs)
                links.add(attrs.get('href').rstrip('/'))


    links = set()
    try:
        log.debug('Getting links from %s' % url)
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode('utf-8'))


    except Exception as e:
        log.debug('Could not get links. %s', e)
    log.debug('links: %r', links)
    return links


class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links   = { }
        self._loaders = { baseurl : UrlModuleLoader(baseurl) }


    def find_module(self, fullname, path=None):
        log.debug('find_module: fullname=%r, path=%r', fullname, path)
        if path is None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]


        parts = fullname.split('.')
        basename = parts[-1]
        log.debug('find_module: baseurl=%r, basename=%r', baseurl, basename)


        # Check link cache
        if basename not in self._links:
            self._links[baseurl] = _get_links(baseurl)


        # Check if it's a package
        if basename in self._links[baseurl]:
            log.debug('find_module: trying package %r', fullname)
            fullurl = self._baseurl + '/' + basename
            # Attempt to load the package (which accesses __init__.py)
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug('find_module: package %r loaded', fullname)
            except ImportError as e:
                log.debug('find_module: package failed. %s', e)
                loader = None
            return loader


        # A normal module
        filename = basename + '.py'
        if filename in self._links[baseurl]:
            log.debug('find_module: module %r found', fullname)
            return self._loaders[baseurl]
        else:
            log.debug('find_module: module %r not found', fullname)
            return None


    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links.clear()


# Module Loader for a URL
class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}


    def module_repr(self, module):
        return '<urlmodule %r from %r>' % (module.__name__, module.__file__)


    # Required method
    def load_module(self, fullname):
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition('.')[0]
        exec(code, mod.__dict__)
        return mod


    # Optional extensions
    def get_code(self, fullname):
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), 'exec')


    def get_data(self, path):
        pass


    def get_filename(self, fullname):
        return self._baseurl + '/' + fullname.split('.')[-1] + '.py'


    def get_source(self, fullname):
        filename = self.get_filename(fullname)
        log.debug('loader: reading %r', filename)
        if filename in self._source_cache:
            log.debug('loader: cached %r', filename)
            return self._source_cache[filename]
        try:
            u = urlopen(filename)
            source = u.read().decode('utf-8')
            log.debug('loader: %r loaded', filename)
            self._source_cache[filename] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug('loader: %r failed.  %s', filename, e)
            raise ImportError("Can't load %s" % filename)


    def is_package(self, fullname):
        return False


# Package loader for a URL
class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, fullname):
        mod = super().load_module(fullname)
        mod.__path__ = [ self._baseurl ]
        mod.__package__ = fullname


    def get_filename(self, fullname):
        return self._baseurl + '/' + '__init__.py'


    def is_package(self, fullname):
        return True


# Utility functions for installing/uninstalling the loader
_installed_meta_cache = { }
def install_meta(address):
    if address not in _installed_meta_cache:
        finder = UrlMetaFinder(address)
        _installed_meta_cache[address] = finder
        sys.meta_path.append(finder)
        log.debug('%r installed on sys.meta_path', finder)


def remove_meta(address):
    if address in _installed_meta_cache:
        finder = _installed_meta_cache.pop(address)
        sys.meta_path.remove(finder)
        log.debug('%r removed from sys.meta_path', finder)


>>> # importing currently fails
>>> import fib
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'fib'


>>> # Load the importer and retry (it works)
>>> import urlimport
>>> urlimport.install_meta('http://localhost:15000')
>>> import fib
I'm fib
>>> import spam
I'm spam
>>> import grok.blah
I'm grok.__init__
I'm grok.blah
>>> grok.blah.__file__
'http://localhost:15000/grok/blah.py'
>>>


# urlimport.py


# ... include previous code above ...


# Path finder class for a URL
class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._links = None
        self._loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl


    def find_loader(self, fullname):
        log.debug('find_loader: %r', fullname)
        parts = fullname.split('.')
        basename = parts[-1]
        # Check link cache
        if self._links is None:
            self._links = []     # See discussion
            self._links = _get_links(self._baseurl)


        # Check if it's a package
        if basename in self._links:
            log.debug('find_loader: trying package %r', fullname)
            fullurl = self._baseurl + '/' + basename
            # Attempt to load the package (which accesses __init__.py)
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                log.debug('find_loader: package %r loaded', fullname)
            except ImportError as e:
                log.debug('find_loader: %r is a namespace package', fullname)


                loader = None
            return (loader, [fullurl])


        # A normal module
        filename = basename + '.py'
        if filename in self._links:
            log.debug('find_loader: module %r found', fullname)
            return (self._loader, [])
        else:
            log.debug('find_loader: module %r not found', fullname)
            return (None, [])


    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links = None


# Check path to see if it looks like a URL
_url_path_cache = {}
def handle_url(path):
    if path.startswith(('http://', 'https://')):
        log.debug('Handle path? %s. [Yes]', path)
        if path in _url_path_cache:
            finder = _url_path_cache[path]
        else:
            finder = UrlPathFinder(path)
            _url_path_cache[path] = finder
        return finder
    else:
        log.debug('Handle path? %s. [No]', path)


def install_path_hook():
    sys.path_hooks.append(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Installing handle_url')


def remove_path_hook():
    sys.path_hooks.remove(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Removing handle_url')


>>> # Initial import fails
>>> import fib
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'fib'


>>> # Install the path hook
>>> import urlimport
>>> urlimport.install_path_hook()


>>> # Imports still fail (not on path)


>>> import fib
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'fib'


>>> # Add an entry to sys.path and watch it work
>>> import sys
>>> sys.path.append('http://localhost:15000')
>>> import fib
I'm fib
>>> import grok.blah
I'm grok.__init__
I'm grok.blah
>>> grok.blah.__file__
'http://localhost:15000/grok/blah.py'
>>>


>>> fib
<urlmodule 'fib' from 'http://localhost:15000/fib.py'>
>>> fib.__name__
'fib'
>>> fib.__file__
'http://localhost:15000/fib.py'
>>> import inspect
>>> print(inspect.getsource(fib))
# fib.py
print("I'm fib")


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


>>>


>>> import imp
>>> m = imp.new_module('spam')
>>> m
<module 'spam'>
>>> m.__name__
'spam'
>>>


>>> import sys
>>> import imp
>>> m = sys.modules.setdefault('spam', imp.new_module('spam'))
>>> m
<module 'spam'>
>>>


>>> import math
>>> m = sys.modules.setdefault('math', imp.new_module('math'))
>>> m
<module 'math' from '/usr/local/lib/python3.3/lib-dynload/math.so'>
>>> m.sin(2)
0.9092974268256817
>>> m.cos(2)
-0.4161468365471424
>>>


>>> from pprint import pprint
>>> pprint(sys.meta_path)
[<class '_frozen_importlib.BuiltinImporter'>,
 <class '_frozen_importlib.FrozenImporter'>,
 <class '_frozen_importlib.PathFinder'>]
>>>


>>> class Finder:
...     def find_module(self, fullname, path):
...             print('Looking for', fullname, path)
...             return None
...
>>> import sys
>>> sys.meta_path.insert(0, Finder())   # Insert as first entry
>>> import math
Looking for math None
>>> import types
Looking for types None
>>> import threading
Looking for threading None
Looking for time None
Looking for traceback None
Looking for linecache None
Looking for tokenize None
Looking for token None
>>>


>>> import xml.etree.ElementTree
Looking for xml None
Looking for xml.etree ['/usr/local/lib/python3.3/xml']
Looking for xml.etree.ElementTree ['/usr/local/lib/python3.3/xml/etree']
Looking for warnings None


Looking for contextlib None
Looking for xml.etree.ElementPath ['/usr/local/lib/python3.3/xml/etree']
Looking for _elementtree None
Looking for copy None
Looking for org None
Looking for pyexpat None
Looking for ElementC14N None
>>>


>>> del sys.meta_path[0]
>>> sys.meta_path.append(Finder())
>>> import urllib.request
>>> import datetime


>>> import fib
Looking for fib None
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'fib'
>>> import xml.superfast
Looking for xml.superfast ['/usr/local/lib/python3.3/xml']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'xml.superfast'
>>>


>>> from pprint import pprint
>>> import sys
>>> pprint(sys.path)
['',
 '/usr/local/lib/python33.zip',
 '/usr/local/lib/python3.3',
 '/usr/local/lib/python3.3/plat-darwin',
 '/usr/local/lib/python3.3/lib-dynload',
 '/usr/local/lib/...3.3/site-packages']
>>>


>>> pprint(sys.path_importer_cache)
{'.': FileFinder('.'),
 '/usr/local/lib/python3.3': FileFinder('/usr/local/lib/python3.3'),
 '/usr/local/lib/python3.3/': FileFinder('/usr/local/lib/python3.3/'),
 '/usr/local/lib/python3.3/collections': FileFinder('...python3.3/collections'),
 '/usr/local/lib/python3.3/encodings': FileFinder('...python3.3/encodings'),
 '/usr/local/lib/python3.3/lib-dynload': FileFinder('...python3.3/lib-dynload'),
 '/usr/local/lib/python3.3/plat-darwin': FileFinder('...python3.3/plat-darwin'),
 '/usr/local/lib/python3.3/site-packages': FileFinder('...python3.3/site-packages'),
 '/usr/local/lib/python33.zip': None}
>>>


>>> class Finder:
...     def find_loader(self, name):
...             print('Looking for', name)
...             return (None, [])
...
>>> import sys
>>> # Add a "debug" entry to the importer cache
>>> sys.path_importer_cache['debug'] = Finder()
>>> # Add a "debug" directory to sys.path
>>> sys.path.insert(0, 'debug')
>>> import threading
Looking for threading
Looking for time
Looking for traceback
Looking for linecache
Looking for tokenize


Looking for token
>>>


>>> sys.path_importer_cache.clear()
>>> def check_path(path):
...     print('Checking', path)
...     raise ImportError()
...
>>> sys.path_hooks.insert(0, check_path)
>>> import fib
Checked debug
Checking .
Checking /usr/local/lib/python33.zip
Checking /usr/local/lib/python3.3
Checking /usr/local/lib/python3.3/plat-darwin
Checking /usr/local/lib/python3.3/lib-dynload
Checking /Users/beazley/.local/lib/python3.3/site-packages
Checking /usr/local/lib/python3.3/site-packages
Looking for fib
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'fib'
>>>


>>> def check_url(path):
...     if path.startswith('http://'):
...             return Finder()
...     else:
...             raise ImportError()
...
>>> sys.path.append('http://localhost:15000')
>>> sys.path_hooks[0] = check_url
>>> import fib
Looking for fib             # Finder output!
Traceback (most recent call last):


  File "<stdin>", line 1, in <module>
ImportError: No module named 'fib'


>>> # Notice installation of Finder in sys.path_importer_cache
>>> sys.path_importer_cache['http://localhost:15000']
<__main__.Finder object at 0x10064c850>
>>>


>>> import xml.etree.ElementTree
>>> xml.__path__
['/usr/local/lib/python3.3/xml']
>>> xml.etree.__path__
['/usr/local/lib/python3.3/xml/etree']
>>>


        # Check link cache
        if self._links is None:
            self._links = []     # See discussion
            self._links = _get_links(self._baseurl)


>>> import logging
>>> logging.basicConfig(level=logging.DEBUG)
>>> import urlimport
>>> urlimport.install_path_hook()
DEBUG:urlimport:Installing handle_url
>>> import fib
DEBUG:urlimport:Handle path? /usr/local/lib/python33.zip. [No]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'fib'
>>> import sys
>>> sys.path.append('http://localhost:15000')
>>> import fib
DEBUG:urlimport:Handle path? http://localhost:15000. [Yes]
DEBUG:urlimport:Getting links from http://localhost:15000
DEBUG:urlimport:links: {'spam.py', 'fib.py', 'grok'}
DEBUG:urlimport:find_loader: 'fib'
DEBUG:urlimport:find_loader: module 'fib' found
DEBUG:urlimport:loader: reading 'http://localhost:15000/fib.py'
DEBUG:urlimport:loader: 'http://localhost:15000/fib.py' loaded
I'm fib
>>>


# postimport.py


import importlib
import sys
from collections import defaultdict


_post_import_hooks = defaultdict(list)


class PostImportFinder:
    def __init__(self):
        self._skip = set()


    def find_module(self, fullname, path=None):
        if fullname in self._skip:
            return None
        self._skip.add(fullname)
        return PostImportLoader(self)


class PostImportLoader:
    def __init__(self, finder):
        self._finder = finder


    def load_module(self, fullname):
        importlib.import_module(fullname)
        module = sys.modules[fullname]
        for func in _post_import_hooks[fullname]:
            func(module)
        self._finder._skip.remove(fullname)
        return module


def when_imported(fullname):
    def decorate(func):
        if fullname in sys.modules:
            func(sys.modules[fullname])
        else:
            _post_import_hooks[fullname].append(func)
        return func
    return decorate


sys.meta_path.insert(0, PostImportFinder())


>>> from postimport import when_imported
>>> @when_imported('threading')
... def warn_threads(mod):
...     print('Threads?  Are you crazy?')
...
>>>
>>> import threading
Threads?  Are you crazy?
>>>


from functools import wraps
from postimport import when_imported


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper


# Example
@when_imported('math')
def add_logging(mod):
    mod.cos = logged(mod.cos)
    mod.sin = logged(mod.sin)


     python3 setup.py install --user


     pip install --user packagename


    bash % pyvenv Spam
    bash %


    bash % cd Spam
    bash % ls
    bin               include             lib           pyvenv.cfg
    bash %


    bash % Spam/bin/python3
    Python 3.3.0 (default, Oct  6 2012, 15:45:22)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from pprint import pprint
    >>> import sys
    >>> pprint(sys.path)
    ['',


     '/usr/local/lib/python33.zip',
     '/usr/local/lib/python3.3',
     '/usr/local/lib/python3.3/plat-darwin',
     '/usr/local/lib/python3.3/lib-dynload',
     '/Users/beazley/Spam/lib/python3.3/site-packages']
    >>>


    bash % pyvenv --system-site-packages Spam
    bash %


    projectname/
         README.txt
         Doc/
             documentation.txt
         projectname/
            __init__.py
            foo.py
            bar.py
            utils/
                 __init__.py
                 spam.py
                 grok.py
         examples/
            helloworld.py
            ...


# setup.py
from distutils.core import setup


setup(name='projectname',
      version='1.0',
      author='Your Name',
      author_email='you@youraddress.com',
      url='http://www.you.com/projectname',
      packages=['projectname', 'projectname.utils'],
)


    # MANIFEST.in
    include *.txt
    recursive-include examples *
    recursive-include Doc *


% bash python3 setup.py sdist
```