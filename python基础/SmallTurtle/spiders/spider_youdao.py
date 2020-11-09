import urllib.request
import urllib.parse
import json

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
fanyi = "我好帅"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58"
}

data = {
    "i": fanyi,
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16043223044352",
    "sign": "65234980dec8e3166abae7d62f3b9a90",
    "lts": "1604322304435",
    "bv": "152ab8d037e123e288bdd3fea870d639",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
}
data = urllib.parse.urlencode(data).encode("utf-8")

response = urllib.request.urlopen(url, data)

html = response.read().decode("utf-8")

target = json.loads(html)
print(target['translateResult'][0][0]['tgt'])
