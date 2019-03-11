from bs4 import BeautifulSoup
from numpy import size
import urllib.request
import os

baseDir = "PVP Data/Heroes/"

html_doc = urllib.request.urlopen('https://grandchase.fandom.com/wiki/Grand_Chase_Dimensional_Chaser')
#print(html_doc.read(100).decode('utf-8'))
soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())

for link in soup.find_all('a'):
    baseURL = 'https://grandchase.fandom.com'
    linkClass = link.get('class')
    linkClassSize = size(linkClass)
    if (linkClassSize == 3):
        hrefLink = link.get('href')
        linkTitle = link.get('title') #Create subdirectories  under PVP Data/Heroes/>>this is the hero name      
        #print('Title:' , linkTitle) 
        if (linkClass[1] == 'image-thumbnail'):
            dirName = linkTitle.partition("/")
            #print(dirName[0])
            charURL = baseURL + hrefLink
            #print(dirName[0], ': ', charURL)

            #Processing Individual Possible Character URL
            char_html = urllib.request.urlopen(charURL) #Open Character URL
            char_soup = BeautifulSoup(char_html, 'html.parser') #Parse URL to soup Object
            char_icons = 0
            iconsURLS = []
            fileNames = []
            for link in char_soup.find_all('a'):
                #linkClass = link.get('class')
                #print('Class: ', linkClass)
                linkTitle = link.get('title')

                if (linkTitle):                                     
                    
                    if "IconHero" in linkTitle:
                        char_icons += 1
                        
                        iconFileName = link.img.get("data-image-name")  
                        print('Title: ', iconFileName) #This is the file name                        
                        #print('Title: ', linkTitle) #This is the file name
                        img_tag = link.img
                        #print(img_tag)
                        imgSRC = img_tag.get('src')
                        #print("::::::::", imgSRC)
                        fileNames.append(iconFileName)
                        iconsURLS.append(imgSRC)

            
            if (char_icons > 0 ):
                #print ("Dir name: ", linkTitle)
                print ("Downloadable icons for ", dirName[0],  " are:")
                directory = baseDir + dirName[0]             
                
                if not os.path.exists(directory):
                    os.makedirs(directory)
                else:
                    print("Dir already exists")            
                
                for i in range(len(fileNames)):
                    fileName = fileNames[i]
                    #print(fileName)
                    full_file_name = directory + '/' + fileName
                    #print(full_file_name)
                    image_url = iconsURLS[i]
                    print(image_url)
                    urllib.request.urlretrieve(image_url,full_file_name)
