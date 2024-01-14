import requests

url = 'http://jsscszx.jscsedu.cn'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
           'Connection':'keep-alive'}
r = requests.get(url,headers = headers)
Cookie = r.headers['Set-Cookie'].split(';')[0]
headers['Cookie'] = Cookie
Rsuccess = requests.get(url,headers = headers)
print(Rsuccess.text)
