### 读写csv数据

```python
from urllib import urlretrieve
urlretrieve()
cat  **.csv | less

import csv

csv.reader()
csv.writer()

open()  # 'rb' 二进制打开

# 迭代器
reader.next()

#
writer.writerow()
writer.writerow(reader.next())

#
wf.flush()

```

```python
import csv

with open() as rf:
    reader = csv.reader(rf)
    with open() as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headres)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
            writer.writerow(row)
```