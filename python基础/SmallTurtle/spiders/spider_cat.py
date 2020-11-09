import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
image = response.read()

with open("spiders\\imgs\\cat_200_300.jpg", "wb") as f:
    f.write(image)
