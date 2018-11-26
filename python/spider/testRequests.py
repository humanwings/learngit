import requests
import json

# r = requests.get(url='http://www.itwhy.org')    # 最基本的GET请求
# print(type(r))
# print(r.status_code)    # 获取返回状态
# print(r.cookies)

# params = {
#     "name":"jack",
#     "age":20
# }

# print(params)

# print(json.dumps(params, indent=4))

# print("-----------------------GET 方式-----------------------")
# r = requests.get('http://httpbin.org/get', params = params)
# print(r.status_code)    # 获取返回状态
# content = json.dumps(json.loads(r.text),indent=4)
# print(content)

# print("-----------------------POST 方式-----------------------")
# r = requests.post('http://httpbin.org/post', data = params)
# print(r.status_code)    # 获取返回状态
# content = json.dumps(json.loads(r.text),indent=4)
# print(content)

# print("-----------------------session 测试-----------------------")
# r = requests.get('http://httpbin.org/cookies/set/number/123456789')
# content = json.dumps(json.loads(r.text),indent=4)
# print(content)
# r = requests.get('http://httpbin.org/cookies')
# content = json.dumps(json.loads(r.text),indent=4)
# print(content)

# s = requests.Session()
# r = s.get('http://httpbin.org/cookies/set/number/123456781')
# content = json.dumps(json.loads(r.text),indent=4)
# print(content)
# r = s.get('http://httpbin.org/cookies')
# content = json.dumps(json.loads(r.text),indent=4)
# print(content)

# r = requests.put('http://httpbin.org/put')
# print(r.status_code)    # 获取返回状态

# r = requests.delete('http://httpbin.org/delete')
# print(r.status_code)    # 获取返回状态

# r = requests.head('http://httpbin.org/get')
# print(r.status_code)    # 获取返回状态

# r = requests.options('http://httpbin.org/get')
# print(r.status_code)    # 获取返回状态

# r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
# print(r.url)
# print(r.text)

# print("-----------------------不验证证明书-----------------------")
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)

# print("-----------------------HTTP Basic Auth-----------------------")
response = requests.get('https://intra.liandisys.com.cn/ioffice/logon.jsp',auth=('wujian', 'Goken002'))
print(response.status_code)

