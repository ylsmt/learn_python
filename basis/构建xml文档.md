### 构建xml 文档

```python
# 构建elementtree  write


from xml.etree.EleementTree import Element, ElementTree

e = Element('Data')
e.tag   # 'Data'

e.set('name', 'abc')

tostring(e) 　# <Data name="abc" />

e.text = 123
tostring(e)　　# <Data name="abc">123</Data>

e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
e2.append(e3)

e.text = None
e.append(e2)


et = ElementTree(e)

et.write('demo.xml')
```

```python
def csvToxml(fname):
    with open(fname, 'rb')  as f: 
        reader = csv.reder(f)
        headers = reader.next()
        
        root = Element('Data')
        for row in reader:
            eRow = Elemnet('Row')
            root.append(eRow)
            
            for tag, text in zip(headers, row):
            e = Element(tag)
            e.text = text
            eRow.append(e)
    
    return ElementTree(root)

et = csvToxml('xx.csv')
et.write('xx.xml')

################################### 格式美化
def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level
    
pretty(root)
```
