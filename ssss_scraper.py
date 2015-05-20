import requests
import urllib
from bs4 import BeautifulSoup

# scrape most recent comic
page = requests.get("http://sssscomic.com/comic.php").content
 
soup = BeautifulSoup(page)
 
comicImageBlock = soup.find("div",{"id":"wrapper2"})
 
comicImageTag = comicImageBlock.find("img")
 
comicURL = "https://sssscomic.com/" + comicImageTag['src']
 
print comicURL
 
urllib.urlretrieve(comicURL, "C:/Users/alant/Downloads/ssss.jpg")

# scrape historical comics
def scrapeold(start, end):
    if start > end:
        print "input a valid range"
    else:
        for i in range(start, end):
            page = requests.get("http://sssscomic.com/comic.php" +
                                "?page=%s") % (str(i))

            soup = BeautifulSoup(page)

            comicImageBlock = soup.find("div",{"id":"wrapper2"})

            comicImageTag = comicImageBlock.find("img")

            comicURL = "https://sssscomic.com/" + comicImageTag['src']

            urllib.urlretrieve(comicURL, "C:/Users/alant/Downloads/ssss%s.jpg") % (str(i))
