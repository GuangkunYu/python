import urllib.request
response = urllib.request.urlopen("http://www.fishc.com")
html = response.read().decode("utf8")
print(html)
