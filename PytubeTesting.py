from pytube import YouTube, Search 
import urllib.request
from PIL import Image

## Pulling a video and it's information via a implicit URL

yt = YouTube(input("enter url:"))
title = yt.title
print (title)

## Using the search module

s = Search(input("What do you want?: "))
print ("There were", len(s.results), "results found") 
print (s.results)
x = input("Did you find what you were looking for?: ")
if x == "no":
    s.get_next_results()
    print ("There were", len(s.results), " additional results found") 
else: 
    print ("thanks for using the thing, goodbye!")

##creating an object with the video ID

yt_id = YouTube.from_id("XubH4QNdUjQ") 

print (yt_id.title) 

##making sure that we can grab an image URL
print (yt_id.thumbnail_url)


##display the image 
urllib.request.urlretrieve(
  'https://i.ytimg.com/vi/XubH4QNdUjQ/sddefault.jpg',
    "sddefault.jpg")
  
img = Image.open("sddefault.jpg")
img.show()


