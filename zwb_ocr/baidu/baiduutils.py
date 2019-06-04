from urllib import request
import sys
import ssl
import json


def get_access_token(id, cecret):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + id+'&client_secret='+cecret
    requ = request.Request(host)
    requ.add_header('Content-Type', 'application/json; charset=UTF-8')
    resp = request.urlopen(requ)
    content = resp.read().decode("utf-8")
    jsonObj = json.loads(content)
    return jsonObj["access_token"]