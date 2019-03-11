import urllib.request
full_file_name = 'test.png'
image_url = "https://vignette.wikia.nocookie.net/grandchase/images/9/94/IconHero-Elesis-5.png/revision/latest?cb=20180412130740"
urllib.request.urlretrieve(image_url,full_file_name)