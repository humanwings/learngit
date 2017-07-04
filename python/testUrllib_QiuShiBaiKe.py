import urllib.request
import urllib.error
import http.cookiejar
import re
from tool import Tool

from datetime import datetime

#url = "http://fund.eastmoney.com/f10/jjjz_519156.html"
#url = "http://www.licaidashiye.com/tools/dividend_ratio.php"
url = "http://www.qiushibaike.com/hot/page/2/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
headers = { 'User-Agent' : user_agent }
timeout = 10

rq = urllib.request.Request(url,None,headers)

print("url: " ,rq.full_url,"\n")
print("type: " ,rq.type,"\n")
print("host: " ,rq.host,"\n")
print("origin_req_host: " ,rq.origin_req_host,"\n")

for item in rq.header_items():
    print(item[0]," : ",item[1],"\n")

try:
    rp = urllib.request.urlopen(rq,None,timeout)

    #print (rp.read().decode("utf-8"))
    
    content = rp.read().decode('utf-8')
    print("content len: ",len(content))
    #pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
    #                     'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    pattern = re.compile('<div class="article block untagged mb15".*?<h2>(.*?)</h2>.*?<span>(.*?)</span>',re.S)
    
    tool = Tool()
    
    items = re.findall(pattern,content)
    print("items len: ",len(items))
    
    for item in items:
        print(item[0],"\n",tool.replace(item[1]))
        print("\n")

    print("rp.url: " ,rp.geturl(),"\n")
    #print("rp.info: " ,rp.info(),"\n")
    print("rp.code: " ,rp.getcode(),"\n")

except urllib.error.HTTPError as e:
    print("error code: ",e.code)
    print("error reason: ",e.reason)
    print("error headers: ",e.headers)

except urllib.error.URLError as e:
    print("error reason: ",e.reason)


print(datetime.today())


