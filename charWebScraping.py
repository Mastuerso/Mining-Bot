from bs4 import BeautifulSoup
from numpy import size
import urllib.request
html_doc = urllib.request.urlopen('https://grandchase.fandom.com/wiki/Elesis/Grand_Chase_Dimensional_Chaser')
#print(html_doc.read(100).decode('utf-8'))
soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())
for link in soup.find_all('a'):
    #linkClass = link.get('class')
    #print('Class: ', linkClass)
    linkTitle = link.get('title')
    if (linkTitle):      

        #print('Title: ', linkTitle)
        if "IconHero" in linkTitle:

            img_tag = link.img
            #print(img_tag)
            imgSRC = img_tag.get('src')
            print(imgSRC)

            #print('Hero: ', linkTitle)
            heroHref = link.get('href')
            
            baseURL = 'https://grandchase.fandom.com'
            iconURL = baseURL + heroHref
            #print('IconURL: ', iconURL)        
            