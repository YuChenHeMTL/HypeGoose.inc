import os
from urllib import request as req
from urllib import error
from urllib import parse
import bs4

listcolor = ["red", "yellow", "black", "white", "blue", "brown", "grey", "green"]
listgender = ["women", "men"]


countergender = 0
while range(len(listgender)):
    countercolor = 0
    while range(len(listcolor)):
        d = {color[countercolor]:gender[countergender]}
        countercolor += 1
    countergender += 1
        

for val in d:
    keyword = val[0] + "clothes" + val[1]
    if not os.path.exists(keyword):
        os.mkdir(keyword)

urlKeyword = parse.quote(keyword)
url = 'https://www.google.com/search?hl=jp&q=' + urlKeyword + '&btnG=Google+Search&tbs=0&safe=off&tbm=isch'


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",}
request = req.Request(url=url, headers=headers)
page = req.urlopen(request)

html = page.read().decode('utf-8')
html = bs4.BeautifulSoup(html, "html.parser")
elems = html.select('.rg_meta.notranslate')
counter = 0
for ele in elems:
    ele = ele.contents[0].replace('"','').split(',')
    eledict = dict()
    for e in ele:
        num = e.find(':')
        eledict[e[0:num]] = e[num+1:]
    imageURL = eledict['ou']

    pal = '.jpg'
    if '.jpg' in imageURL:
        pal = '.jpg'
    elif '.JPG' in imageURL:
        pal = '.jpg'
    elif '.png' in imageURL:
        pal = '.png'
    elif '.gif' in imageURL:
        pal = '.gif'
    elif '.jpeg' in imageURL:
        pal = '.jpeg'
    else:
        pal = '.jpg'

    try:
        img = req.urlopen(imageURL)
        localfile = open('./'+keyword+'/'+keyword+str(counter)+pal, 'wb')
        localfile.write(img.read())
        img.close()
        localfile.close()
        counter += 1
    except UnicodeEncodeError:
        continue
    except error.HTTPError:
        continue
    except error.URLError:
        continue


#df = pandas.DataFrame(data=BrandList, index=NameList)
#df.to_csv('StreetSnapMen.csv')
#save in csv form

