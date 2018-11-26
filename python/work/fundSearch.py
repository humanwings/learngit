import urllib.request
import urllib.error
import http.cookiejar

from datetime import datetime

url = "http://jingzhi.funds.hexun.com/database/jzzs.aspx?fundcode=001878"
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
# user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Mobile Safari/537.36"
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

    content = rp.read().decode('GBK')
    print("content len: ",len(content))
    print(content)
  
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


