### `__new__` 修改实例化行为

> 场景
> IntTuple([1,-1,'abc',7,['x','y'],3])  ==>  (1,6,3)

```python
class IntTuple(tuple):
    """docstring for IntTuple"""
    def __init__(self, iterable):

        print(self)

        super(IntTuple, self).__init__(iterable)

        self.arg = arg

    def __new__(cls, arg):
        g = (x for x in arg if isinstance(x, int) and x > 0)

        # return 实例
        # 这里 super    cls 是一个子类
        return super(IntTuple, cls).__new__(cls, g) 
t = IntTuple([1,-1,'abc',7,['x','y'],3])
print(t)

```
