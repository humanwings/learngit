from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
 
username = 'wujian'
password = 'Goken002'
url = 'https://intra.liandisys.com.cn/ioffice/logon.jsp'
 
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
 
try:
    result = opener.open(url)
    html = result.read().decode('GB2312')
    print(html)
except URLError as e:
    print(e)