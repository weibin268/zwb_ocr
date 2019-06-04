from urllib import request
import sys
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id= &client_secret= '
requ = request.Request(host)
requ.add_header('Content-Type', 'application/json; charset=UTF-8')
resp = request.urlopen(requ)
content = resp.read()
if (content):
    print(content)