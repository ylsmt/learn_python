
### 读写json数据

```python
import requests
import json

# 录音
from record import Record
record = Record(channels=1) # 单声道
audioData = record.record(2) # 2 秒

# 获取token
from secret import API_KEY SECRET_KEY
authUrl = ''+ API_KEY + '&client_secret=' + SECRET_KEY

response = requests.get(authUrl)
res = json.loads(response.content)
token = res['access_token']

# 语音识别
cuid = 'xxxxxxxxxx'
srvUrl = '' + '?cuid=' + cuid + '&token=' + token
httpHeader = {
    'Content-type': 'audio/wav; rate = 8000',
}
response = requests.post(srvUrl, headers=httpHeader, data=audioData)
res = json.loads(responsecontent)
text = res['result'][0]

print('\n resuls:')
print(text)

```

```
l = [1, 2, 'abc', {'name': 'Bob', 'age': 13}]
json.dumps(l)

d = {'b': None, 'a':5 , 'c': 'abc'}
json.dumps(d)

# 删除多余空格 默认', ', ': '
json.dumps(l, separators=',',':')

json.dumps(d, sort_keys=True)

# json to obj

l2 = json.loads('[1, 2, 'abc', {'name': 'Bob', 'age': 13}]')

l2[0]
l2[2]

# load  dump  接口是个文件

with open('deom.json, 'wb') as f:
    json.dump(l, f)

```