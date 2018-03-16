```python

Data Encoding and Processing


CHAPTER 6


    Symbol,Price,Date,Time,Change,Volume
    "AA",39.48,"6/11/2007","9:36am",-0.18,181800
    "AIG",71.38,"6/11/2007","9:36am",-0.15,195500
    "AXP",62.58,"6/11/2007","9:36am",-0.46,935000
    "BA",98.31,"6/11/2007","9:36am",+0.12,104800
    "C",53.08,"6/11/2007","9:36am",-0.25,360900
    "CAT",78.29,"6/11/2007","9:36am",-0.23,225400


import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:


        # Process row
        ...


from collections import namedtuple
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        # Process row
        ...


import csv
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        ...


headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]


with open('stocks.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)


headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]


with open('stocks.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)


with open('stocks.csv') as f:
    for line in f:
        row = line.split(',')
        # process row
        ...


# Example of reading tab-separated values
with open('stock.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        # Process row
        ...


Street Address,Num-Premises,Latitude,Longitude
5412 N CLARK,10,41.980262,-87.668452


import re
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        # Process row
        ...


col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        ...


print('Reading as dicts with type conversion')
field_types = [ ('Price', float),
                ('Change', float),
                ('Volume', int) ]


with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)


import json


data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}


json_str = json.dumps(data)


data = json.loads(json_str)


# Writing JSON data
with open('data.json', 'w') as f:
     json.dump(data, f)


# Reading data back
with open('data.json', 'r') as f:
     data = json.load(f)


>>> json.dumps(False)
'false'
>>> d = {'a': True,
...      'b': 'Hello',
...      'c': None}
>>> json.dumps(d)
'{"b": "Hello", "c": null, "a": true}'
>>>


>>> from urllib.request import urlopen
>>> import json
>>> u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
>>> resp = json.loads(u.read().decode('utf-8'))
>>> from pprint import pprint
>>> pprint(resp)
{'completed_in': 0.074,
 'max_id': 264043230692245504,
 'max_id_str': '264043230692245504',
 'next_page': '?page=2&max_id=264043230692245504&q=python&rpp=5',
 'page': 1,
 'query': 'python',
 'refresh_url': '?since_id=264043230692245504&q=python',
 'results': [{'created_at': 'Thu, 01 Nov 2012 16:36:26 +0000',
              'from_user': ...
             },
             {'created_at': 'Thu, 01 Nov 2012 16:36:14 +0000',
              'from_user': ...
             },
             {'created_at': 'Thu, 01 Nov 2012 16:36:13 +0000',
              'from_user': ...
             },
             {'created_at': 'Thu, 01 Nov 2012 16:36:07 +0000',
              'from_user': ...
             }
             {'created_at': 'Thu, 01 Nov 2012 16:36:04 +0000',
              'from_user': ...
             }],


 'results_per_page': 5,
 'since_id': 0,
 'since_id_str': '0'}
>>>


>>> s = '{"name": "ACME", "shares": 50, "price": 490.1}'
>>> from collections import OrderedDict
>>> data = json.loads(s, object_pairs_hook=OrderedDict)
>>> data
OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])
>>>


>>> class JSONObject:
...     def __init__(self, d):
...             self.__dict__ = d
...
>>>
>>> data = json.loads(s, object_hook=JSONObject)
>>> data.name
'ACME'
>>> data.shares
50
>>> data.price
490.1
>>>


>>> print(json.dumps(data))
{"price": 542.23, "name": "ACME", "shares": 100}
>>> print(json.dumps(data, indent=4))
{
    "price": 542.23,
    "name": "ACME",
    "shares": 100
}
>>>


>>> print(json.dumps(data, sort_keys=True))
{"name": "ACME", "price": 542.23, "shares": 100}
>>>


>>> class Point:
...     def __init__(self, x, y):
...             self.x = x
...             self.y = y
...
>>> p = Point(2, 3)
>>> json.dumps(p)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.3/json/__init__.py", line 226, in dumps
    return _default_encoder.encode(obj)
  File "/usr/local/lib/python3.3/json/encoder.py", line 187, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/local/lib/python3.3/json/encoder.py", line 245, in iterencode
    return _iterencode(o, 0)
  File "/usr/local/lib/python3.3/json/encoder.py", line 169, in default
    raise TypeError(repr(o) + " is not JSON serializable")
TypeError: <__main__.Point object at 0x1006f2650> is not JSON serializable
>>>


def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d


# Dictionary mapping names to known classes
classes = {
    'Point' : Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)   # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d


>>> p = Point(2,3)
>>> s = json.dumps(p, default=serialize_instance)
>>> s
'{"__classname__": "Point", "y": 3, "x": 2}'
>>> a = json.loads(s, object_hook=unserialize_object)
>>> a
<__main__.Point object at 0x1017577d0>
>>> a.x
2
>>> a.y
3
>>>


from urllib.request import urlopen
from xml.etree.ElementTree import parse


# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)


# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')


    print(title)
    print(date)
    print(link)
    print()


    Steve Holden: Python for Data Analysis
    Mon, 19 Nov 2012 02:13:51 +0000
    http://holdenweb.blogspot.com/2012/11/python-for-data-analysis.html


    Vasudev Ram: The Python Data model (for v2 and v3)
    Sun, 18 Nov 2012 22:06:47 +0000
    http://jugad2.blogspot.com/2012/11/the-python-data-model.html


    Python Diary: Been playing around with Object Databases
    Sun, 18 Nov 2012 20:40:29 +0000
    http://www.pythondiary.com/blog/Nov.18,2012/been-...-object-databases.html


    Vasudev Ram: Wakari, Scientific Python in the cloud
    Sun, 18 Nov 2012 20:19:41 +0000
    http://jugad2.blogspot.com/2012/11/wakari-scientific-python-in-cloud.html


    Jesse Jiryu Davis: Toro: synchronization primitives for Tornado coroutines
    Sun, 18 Nov 2012 20:17:49 +0000
    http://feedproxy.google.com/~r/EmptysquarePython/~3/_DOZT2Kd0hQ/


    <?xml version="1.0"?>
    <rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
    <channel>
      <title>Planet Python</title>
      <link>http://planet.python.org/</link>
      <language>en</language>
      <description>Planet Python - http://planet.python.org/</description>
      <item>
        <title>Steve Holden: Python for Data Analysis</title>
          <guid>http://holdenweb.blogspot.com/...-data-analysis.html</guid>
          <link>http://holdenweb.blogspot.com/...-data-analysis.html</link>
          <description>...</description>
          <pubDate>Mon, 19 Nov 2012 02:13:51 +0000</pubDate>
      </item>
      <item>


        <title>Vasudev Ram: The Python Data model (for v2 and v3)</title>
        <guid>http://jugad2.blogspot.com/...-data-model.html</guid>
        <link>http://jugad2.blogspot.com/...-data-model.html</link>
        <description>...</description>
        <pubDate>Sun, 18 Nov 2012 22:06:47 +0000</pubDate>
        </item>
      <item>
        <title>Python Diary: Been playing around with Object Databases</title>
        <guid>http://www.pythondiary.com/...-object-databases.html</guid>
        <link>http://www.pythondiary.com/...-object-databases.html</link>
        <description>...</description>
        <pubDate>Sun, 18 Nov 2012 20:40:29 +0000</pubDate>
      </item>
        ...
    </channel>
    </rss>


>>> doc
<xml.etree.ElementTree.ElementTree object at 0x101339510>
>>> e = doc.find('channel/title')
>>> e
<Element 'title' at 0x10135b310>
>>> e.tag
'title'
>>> e.text
'Planet Python'
>>> e.get('some_attribute')
>>>


from xml.etree.ElementTree import iterparse


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)


    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


    <response>
      <row>
        <row ...>
          <creation_date>2012-11-18T00:00:00</creation_date>


          <status>Completed</status>
          <completion_date>2012-11-18T00:00:00</completion_date>
          <service_request_number>12-01906549</service_request_number>
          <type_of_service_request>Pot Hole in Street</type_of_service_request>
          <current_activity>Final Outcome</current_activity>
          <most_recent_action>CDOT Street Cut ... Outcome</most_recent_action>
          <street_address>4714 S TALMAN AVE</street_address>
          <zip>60632</zip>
          <x_coordinate>1159494.68618856</x_coordinate>
          <y_coordinate>1873313.83503384</y_coordinate>
          <ward>14</ward>
          <police_district>9</police_district>
          <community_area>58</community_area>
          <latitude>41.808090232127896</latitude>
          <longitude>-87.69053684711305</longitude>
          <location latitude="41.808090232127896"
                           longitude="-87.69053684711305" />
        </row>
        <row ...>
          <creation_date>2012-11-18T00:00:00</creation_date>
          <status>Completed</status>
          <completion_date>2012-11-18T00:00:00</completion_date>
          <service_request_number>12-01906695</service_request_number>
          <type_of_service_request>Pot Hole in Street</type_of_service_request>
          <current_activity>Final Outcome</current_activity>
          <most_recent_action>CDOT Street Cut ... Outcome</most_recent_action>
          <street_address>3510 W NORTH AVE</street_address>
          <zip>60647</zip>
          <x_coordinate>1152732.14127696</x_coordinate>
          <y_coordinate>1910409.38979075</y_coordinate>
          <ward>26</ward>
          <police_district>14</police_district>
          <community_area>23</community_area>
          <latitude>41.91002084292946</latitude>
          <longitude>-87.71435952353961</longitude>
          <location latitude="41.91002084292946"
                           longitude="-87.71435952353961" />
        </row>
      </row>
    </response>


from xml.etree.ElementTree import parse
from collections import Counter


potholes_by_zip = Counter()


doc = parse('potholes.xml')
for pothole in doc.iterfind('row/row'):
    potholes_by_zip[pothole.findtext('zip')] += 1


for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)


from collections import Counter
potholes_by_zip = Counter()


data = parse_and_remove('potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1


for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)


>>> data = iterparse('potholes.xml',('start','end'))
>>> next(data)
('start', <Element 'response' at 0x100771d60>)
>>> next(data)
('start', <Element 'row' at 0x100771e68>)
>>> next(data)
('start', <Element 'row' at 0x100771fc8>)
>>> next(data)
('start', <Element 'creation_date' at 0x100771f18>)
>>> next(data)
('end', <Element 'creation_date' at 0x100771f18>)
>>> next(data)
('start', <Element 'status' at 0x1006a7f18>)
>>> next(data)
('end', <Element 'status' at 0x1006a7f18>)
>>>


elem_stack[-2].remove(elem)


from xml.etree.ElementTree import Element


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)


        elem.append(child)
    return elem


>>> s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
>>> e = dict_to_xml('stock', s)
>>> e
<Element 'stock' at 0x1004b64c8>
>>>


>>> from xml.etree.ElementTree import tostring
>>> tostring(e)
b'<stock><price>490.1</price><shares>100</shares><name>GOOG</name></stock>'
>>>


>>> e.set('_id','1234')
>>> tostring(e)
b'<stock _id="1234"><price>490.1</price><shares>100</shares><name>GOOG</name>
</stock>'
>>>


def dict_to_xml_str(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key,val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)


>>> d = { 'name' : '<spam>' }


>>> # String creation
>>> dict_to_xml_str('item',d)


'<item><name><spam></name></item>'


>>> # Proper XML creation
>>> e = dict_to_xml('item',d)
>>> tostring(e)
b'<item><name>&lt;spam&gt;</name></item>'
>>>


>>> from xml.sax.saxutils import escape, unescape
>>> escape('<spam>')
'&lt;spam&gt;'
>>> unescape(_)
'<spam>'
>>>


<?xml version="1.0"?>
<stop>
    <id>14791</id>
    <nm>Clark &amp; Balmoral</nm>
    <sri>
        <rt>22</rt>
        <d>North Bound</d>
        <dd>North Bound</dd>
    </sri>


    <cr>22</cr>
    <pre>
       <pt>5 MIN</pt>
       <fd>Howard</fd>
       <v>1378</v>
       <rn>22</rn>
   </pre>
   <pre>
       <pt>15 MIN</pt>
       <fd>Howard</fd>
       <v>1867</v>
       <rn>22</rn>
   </pre>
</stop>


>>> from xml.etree.ElementTree import parse, Element
>>> doc = parse('pred.xml')
>>> root = doc.getroot()
>>> root
<Element 'stop' at 0x100770cb0>


>>> # Remove a few elements
>>> root.remove(root.find('sri'))
>>> root.remove(root.find('cr'))


>>> # Insert a new element after <nm>...</nm>
>>> root.getchildren().index(root.find('nm'))
1
>>> e = Element('spam')
>>> e.text = 'This is a test'
>>> root.insert(2, e)


>>> # Write back to a file
>>> doc.write('newpred.xml', xml_declaration=True)
>>>


<?xml version='1.0' encoding='us-ascii'?>
<stop>
    <id>14791</id>
    <nm>Clark &amp; Balmoral</nm>
    <spam>This is a test</spam><pre>
       <pt>5 MIN</pt>
       <fd>Howard</fd>
       <v>1378</v>
       <rn>22</rn>
   </pre>
   <pre>
       <pt>15 MIN</pt>
       <fd>Howard</fd>


       <v>1867</v>
       <rn>22</rn>
   </pre>
</stop>


<?xml version="1.0" encoding="utf-8"?>
<top>
  <author>David Beazley</author>
  <content>
      <html xmlns="http://www.w3.org/1999/xhtml">
          <head>
              <title>Hello World</title>
          </head>
          <body>
              <h1>Hello World!</h1>
          </body>
      </html>
  </content>
</top>


>>> # Some queries that work
>>> doc.findtext('author')
'David Beazley'
>>> doc.find('content')


<Element 'content' at 0x100776ec0>


>>> # A query involving a namespace (doesn't work)
>>> doc.find('content/html')


>>> # Works if fully qualified
>>> doc.find('content/{http://www.w3.org/1999/xhtml}html')
<Element '{http://www.w3.org/1999/xhtml}html' at 0x1007767e0>


>>> # Doesn't work
>>> doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title')


>>> # Fully qualified
>>> doc.findtext('content/{http://www.w3.org/1999/xhtml}html/'
...  '{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title')
'Hello World'
>>>


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'
    def __call__(self, path):
        return path.format_map(self.namespaces)


>>> ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
>>> doc.find(ns('content/{html}html'))
<Element '{http://www.w3.org/1999/xhtml}html' at 0x1007767e0>
>>> doc.findtext(ns('content/{html}html/{html}head/{html}title'))
'Hello World'
>>>


>>> from xml.etree.ElementTree import iterparse
>>> for evt, elem in iterparse('ns2.xml', ('end', 'start-ns', 'end-ns')):
...     print(evt, elem)
...
end <Element 'author' at 0x10110de10>
start-ns ('', 'http://www.w3.org/1999/xhtml')
end <Element '{http://www.w3.org/1999/xhtml}title' at 0x1011131b0>
end <Element '{http://www.w3.org/1999/xhtml}head' at 0x1011130a8>
end <Element '{http://www.w3.org/1999/xhtml}h1' at 0x101113310>
end <Element '{http://www.w3.org/1999/xhtml}body' at 0x101113260>
end <Element '{http://www.w3.org/1999/xhtml}html' at 0x10110df70>
end-ns None
end <Element 'content' at 0x10110de68>
end <Element 'top' at 0x10110dd60>
>>> elem      # This is the topmost element
<Element 'top' at 0x10110dd60>
>>>


stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]


>>> import sqlite3
>>> db = sqlite3.connect('database.db')
>>>


>>> c = db.cursor()
>>> c.execute('create table portfolio (symbol text, shares integer, price real)')
<sqlite3.Cursor object at 0x10067a730>
>>> db.commit()
>>>


>>> c.executemany('insert into portfolio values (?,?,?)', stocks)
<sqlite3.Cursor object at 0x10067a730>
>>> db.commit()
>>>


>>> for row in db.execute('select * from portfolio'):
...     print(row)
...
('GOOG', 100, 490.1)
('AAPL', 50, 545.75)
('FB', 150, 7.45)
('HPQ', 75, 33.2)
>>>


>>> min_price = 100
>>> for row in db.execute('select * from portfolio where price >= ?',
                         (min_price,)):
...     print(row)
...
('GOOG', 100, 490.1)
('AAPL', 50, 545.75)
>>>


>>> # Initial byte string
>>> s = b'hello'


>>> # Encode as hex
>>> import binascii
>>> h = binascii.b2a_hex(s)
>>> h
b'68656c6c6f'


>>> # Decode back to bytes
>>> binascii.a2b_hex(h)
b'hello'
>>>


>>> import base64
>>> h = base64.b16encode(s)
>>> h
b'68656C6C6F'
>>> base64.b16decode(h)
b'hello'
>>>


>>> h = base64.b16encode(s)
>>> print(h)
b'68656C6C6F'
>>> print(h.decode('ascii'))
68656C6C6F
>>>


>>> # Some byte data
>>> s = b'hello'
>>> import base64


>>> # Encode as Base64
>>> a = base64.b64encode(s)
>>> a
b'aGVsbG8='


>>> # Decode from Base64
>>> base64.b64decode(a)
b'hello'
>>>


>>> a = base64.b64encode(s).decode('ascii')
>>> a
'aGVsbG8='
>>>


from struct import Struct


def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


# Example
if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]


    with open('data.b', 'wb') as f:
         write_records(records, '<idd', f)


from struct import Struct


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


# Example
if __name__ == '__main__':
    with open('data.b','rb') as f:
        for rec in read_records('<idd', f):
            # Process rec
            ...


from struct import Struct


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


# Example
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()


    for rec in unpack_records('<idd', data):
        # Process rec
        ...


# Little endian 32-bit integer, two double precision floats
record_struct = Struct('<idd')


>>> from struct import Struct
>>> record_struct = Struct('<idd')
>>> record_struct.size
20
>>> record_struct.pack(1, 2.0, 3.0)
b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'
>>> record_struct.unpack(_)
(1, 2.0, 3.0)
>>>


>>> import struct
>>> struct.pack('<idd', 1, 2.0, 3.0)
b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'
>>> struct.unpack('<idd', _)
(1, 2.0, 3.0)
>>>


>>> f = open('data.b', 'rb')
>>> chunks = iter(lambda: f.read(20), b'')
>>> chunks
<callable_iterator object at 0x10069e6d0>
>>> for chk in chunks:
...     print(chk)
...
b'\x01\x00\x00\x00ffffff\x02@\x00\x00\x00\x00\x00\x00\x12@'
b'\x06\x00\x00\x00333333\x1f@\x00\x00\x00\x00\x00\x00"@'
b'\x0c\x00\x00\x00\xcd\xcc\xcc\xcc\xcc\xcc*@\x9a\x99\x99\x99\x99YL@'
>>>


def read_records(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)
    return records


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack(data[offset:offset + record_struct.size])
            for offset in range(0, len(data), record_struct.size))


from collections import namedtuple


Record = namedtuple('Record', ['kind','x','y'])


with open('data.p', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))


for r in records:
    print(r.kind, r.x, r.y)


>>> import numpy as np
>>> f = open('data.b', 'rb')
>>> records = np.fromfile(f, dtype='<i,<d,<d')
>>> records
array([(1, 2.3, 4.5), (6, 7.8, 9.0), (12, 13.4, 56.7)],
      dtype=[('f0', '<i4'), ('f1', '<f8'), ('f2', '<f8')])
>>> records[0]
(1, 2.3, 4.5)
>>> records[1]
(6, 7.8, 9.0)
>>>


polys = [
          [ (1.0, 2.5), (3.5, 4.0), (2.5, 1.5) ],
          [ (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0) ],
          [ (3.4, 6.3), (1.2, 0.5), (4.6, 9.2) ],
        ]


Type
int
double
double
double
double
int


Description
File code (0x1234, little endian)
Minimum x (little endian)
Minimum y (little endian)
Maximum x (little endian)
Maximum y (little endian)
Number of polygons (little endian)


Type
int
Points


Description
Record length including length (N bytes)
Pairs of (X,Y) coords as doubles


import struct
import itertools


def write_polys(filename, polys):
    # Determine bounding box
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)


    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi',
                            0x1234,
                            min_x, min_y,
                            max_x, max_y,
                            len(polys)))


        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size+4))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))


# Call it with our polygon data
write_polys('polys.bin', polys)


import struct


def read_polys(filename):
    with open(filename, 'rb') as f:
        # Read the header
        header = f.read(40)
        file_code, min_x, min_y, max_x, max_y, num_polys =


import struct


class StructField:
    '''
    Descriptor representing a simple structure field
    '''
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r =  struct.unpack_from(self.format,
                                    instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num_polys = StructField('<i', 36)


>>> f = open('polys.bin', 'rb')
>>> phead = PolyHeader(f.read(40))
>>> phead.file_code == 0x1234
True
>>> phead.min_x
0.5
>>> phead.min_y
0.5


>>> phead.max_x
7.0
>>> phead.max_y
9.2
>>> phead.num_polys
3
>>>


class StructureMeta(type):
    '''
    Metaclass that automatically creates StructField descriptors
    '''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<','>','!','@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata


    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
       ('<i', 'file_code'),
       ('d', 'min_x'),
       ('d', 'min_y'),


       ('d', 'max_x'),
       ('d', 'max_y'),
       ('i', 'num_polys')
    ]


>>> f = open('polys.bin', 'rb')
>>> phead = PolyHeader.from_file(f)
>>> phead.file_code == 0x1234
True
>>> phead.min_x
0.5
>>> phead.min_y
0.5
>>> phead.max_x
7.0
>>> phead.max_y
9.2
>>> phead.num_polys
3
>>>


class NestedStruct:
    '''
    Descriptor representing a nested structure
    '''
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:
                               self.offset+self.struct_type.struct_size]
            result = self.struct_type(data)
            # Save resulting structure back on instance to avoid
            # further recomputation of this step
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    '''
    Metaclass that automatically creates StructField descriptors


    '''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname,
                        NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<','>','!','@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Point(Structure):
    _fields_ = [
          ('<d', 'x'),
          ('d', 'y')
    ]


class PolyHeader(Structure):
    _fields_ = [
          ('<i', 'file_code'),
          (Point, 'min'),         # nested struct
          (Point, 'max'),         # nested struct
          ('i', 'num_polys')
    ]


>>> f = open('polys.bin', 'rb')
>>> phead = PolyHeader.from_file(f)
>>> phead.file_code == 0x1234
True
>>> phead.min       # Nested structure
<__main__.Point object at 0x1006a48d0>
>>> phead.min.x


0.5
>>> phead.min.y
0.5
>>> phead.max.x
7.0
>>> phead.max.y
9.2
>>> phead.num_polys
3
>>>


class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        sz, = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)


    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off:off+size]
                yield code(data)


>>> f = open('polys.bin', 'rb')
>>> phead = PolyHeader.from_file(f)
>>> phead.num_polys
3
>>> polydata = [ SizedRecord.from_file(f, '<i')
...              for n in range(phead.num_polys) ]
>>> polydata
[<__main__.SizedRecord object at 0x1006a4d50>,
 <__main__.SizedRecord object at 0x1006a4f50>,
 <__main__.SizedRecord object at 0x10070da90>]
>>>


>>> for n, poly in enumerate(polydata):
...     print('Polygon', n)
...     for p in poly.iter_as('<dd'):
...             print(p)
...
Polygon 0
(1.0, 2.5)
(3.5, 4.0)
(2.5, 1.5)
Polygon 1
(7.0, 1.2)
(5.1, 3.0)
(0.5, 7.5)
(0.8, 9.0)
Polygon 2
(3.4, 6.3)
(1.2, 0.5)
(4.6, 9.2)
>>>


>>> for n, poly in enumerate(polydata):
...     print('Polygon', n)
...     for p in poly.iter_as(Point):
...             print(p.x, p.y)
...
Polygon 0
1.0 2.5
3.5 4.0
2.5 1.5
Polygon 1
7.0 1.2
5.1 3.0
0.5 7.5
0.8 9.0
Polygon 2


3.4 6.3
1.2 0.5
4.6 9.2
>>>


class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
        ]


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),
        (Point, 'max'),
        ('i', 'num_polys')
    ]


def read_polys(filename):
    polys = []
    with open(filename, 'rb') as f:
        phead = PolyHeader.from_file(f)
        for n in range(phead.num_polys):
            rec = SizedRecord.from_file(f, '<i')
            poly = [ (p.x, p.y)
                      for p in rec.iter_as(Point) ]
            polys.append(poly)
    return polys


class ShapeFile(Structure):
    _fields_ = [ ('>i', 'file_code'),    # Big endian
                 ('20s', 'unused'),
                 ('i', 'file_length'),
                 ('<i', 'version'),      # Little endian
                 ('i', 'shape_type'),
                 ('d', 'min_x'),
                 ('d', 'min_y'),
                 ('d', 'max_x'),
                 ('d', 'max_y'),
                 ('d', 'min_z'),
                 ('d', 'max_z'),
                 ('d', 'min_m'),
                 ('d', 'max_m') ]


>>> import pandas


>>> # Read a CSV file, skipping last line
>>> rats = pandas.read_csv('rats.csv', skip_footer=1)
>>> rats
<class 'pandas.core.frame.DataFrame'>
Int64Index: 74055 entries, 0 to 74054
Data columns:
Creation Date                      74055  non-null values
Status                             74055  non-null values
Completion Date                    72154  non-null values
Service Request Number             74055  non-null values
Type of Service Request            74055  non-null values
Number of Premises Baited          65804  non-null values
Number of Premises with Garbage    65600  non-null values
Number of Premises with Rats       65752  non-null values
Current Activity                   66041  non-null values
Most Recent Action                 66023  non-null values
Street Address                     74055  non-null values
ZIP Code                           73584  non-null values
X Coordinate                       74043  non-null values
Y Coordinate                       74043  non-null values
Ward                               74044  non-null values
Police District                    74044  non-null values
Community Area                     74044  non-null values
Latitude                           74043  non-null values
Longitude                          74043  non-null values
Location                           74043  non-null values
dtypes: float64(11), object(9)


>>> # Investigate range of values for a certain field
>>> rats['Current Activity'].unique()
array([nan, Dispatch Crew, Request Sanitation Inspector], dtype=object)


>>> # Filter the data
>>> crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
>>> len(crew_dispatched)
65676
>>>


>>> # Find 10 most rat-infested ZIP codes in Chicago
>>> crew_dispatched['ZIP Code'].value_counts()[:10]
60647    3837
60618    3530
60614    3284
60629    3251
60636    2801
60657    2465
60641    2238
60609    2206
60651    2152
60632    2071
>>>


>>> # Group by completion date
>>> dates = crew_dispatched.groupby('Completion Date')
<pandas.core.groupby.DataFrameGroupBy object at 0x10d0a2a10>
>>> len(dates)
472
>>>


>>> # Determine counts on each day
>>> date_counts = dates.size()
>>> date_counts[0:10]
Completion Date
01/03/2011           4
01/03/2012         125
01/04/2011          54
01/04/2012          38
01/05/2011          78
01/05/2012         100
01/06/2011         100
01/06/2012          58
01/07/2011           1
01/09/2012          12
>>>


>>> # Sort the counts
>>> date_counts.sort()
>>> date_counts[-10:]
Completion Date
10/12/2012         313
10/21/2011         314
09/20/2011         316
10/26/2011         319
02/22/2011         325


10/26/2012         333
03/17/2011         336
10/13/2011         378
10/14/2011         391
10/07/2011         457
>>>
```