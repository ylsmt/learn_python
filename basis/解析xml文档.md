### 解析xml文档

```python
<?xml version='1.0'>
<data>
    <country name=''>
        <year>2008</year>
        ...
    </country>
    ...
    
</data>    
    
```

```python
from xml.etree.ElementTree import parse

f = open('demo.xml')
et = parse(f)
root = et.getroot()  # 根节点

root.tag   # data
root.attrib  # {}
root.text
rooot.text.strip()

for child in root:
    print(child.get('name')) # get 属性

root.find('country')
root.findall('country')
root.iterfind('country')

for e in  root.iterfind('country'):
    print(e.get('name')

# iter 只能找 直接子元素  次级元素

# 可以用 root.iter()

list(root.iter())

root.iter('rank') # 标签是rank的子节点

# 高级查找  support XPath syntax
# * 匹配

root.findall('country/*') # 
# . 当前
# // 任意层次子元素

root.findall('rank') # []
root.findall('.//rank') # ...

# .. 父对象

foot.findall('.//rank..')

#  某一属性
root.findall('country[@name]')

root.findall('country[@name="xx"]')

# 某tag

root.findall('country[rank="5"]')

# 指定位置
root.findall('country[1]')

root.findall('country[last()]')
root.findall('country[last()-1]')

```
