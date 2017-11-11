### 降低大量实例内存开销

> __slots__ 属性

```python
class Player(object):
    """docstring for Player"""
    def __init__(self, uid, name ,status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level
        

class Player2(object):
    """docstring for Player"""
    # __slots__
    __slots__ = ('uid', 'name', 'stat', 'level')
    def __init__(self, uid, name ,status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

p1 = Player('0001','Bob')
p2 = Player2('0002','Jim')

# 查看减少的属性
a = set(dir(p1)) - set(dir(p2))
print(len(a))
print(set.difference(set(dir(p1)), set(dir(p2))))

# 查看内存使用
import sys
print(sys.getsizeof(p1.__dict__))


# 动态绑定属性
print(p1.__dict__)
p1.x = 123
print(p1.__dict__)
p1.__dict__['y'] = 99
print(p1.y)
# 删除
del p1.__dict__['y']

```