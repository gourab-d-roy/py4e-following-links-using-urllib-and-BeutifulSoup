import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count=int(input('counts......'))
pos=int(input('position.....'))
url = input('Enter - ')

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    cnt=0
    for tag in tags:
        cnt=cnt+1

        if (cnt>pos): break
        url=tag.get('href', None)

print(url)
    #url=tags[pos-1].get('href', None)
#print(tags[pos-1].get('href', None))
#print(tags)
