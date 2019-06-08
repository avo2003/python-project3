from bs4 import BeautifulSoup
import urllib2 
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
}

num= 1
url = "https://www.packtpub.com/all-products/all-books"
for i in range(4):
    req = urllib2.Request(url, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, features="html.parser")
    num+= 1
    url = "https://www.packtpub.com/all-products/all-books?page=" + str(num)
    bb = soup.find_all(class_="primary-content")
    for s in range(len(bb)):
        book = bb[s]
        img= book.find(class_="photo image")
        print(img)
        img = book.find(class_ = "photo image")
        imq = urllib2.Request(img['src'], headers=hdr)
        imp = urllib2.urlopen(imq)
        imf = open(str(num)+img["alt"] + ".png", "w")
        imf.write(imp.read())
        imf.close()
        num +=1

