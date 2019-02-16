from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
from Classes.formatting import color
import os

search = input("Who do you want to search for?") #GetTwitterUserID
params = {"q": search} 
#r = requests.get("https://twitter.com/", params= search)
r = requests.get("https://twitter.com/"+search)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol",{"id": "stream-items-id"})
tweets = results.findAll ("li", {"data-item-type": "tweet"})

for tweet in tweets:
    tweet_FullName = tweet.find("strong", "fullname show-popup-with-id u-textTruncate").text
    tweet_Date = tweet.find("small", "time").text
    tweet_text = tweet.find("p", "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    if tweet_text:
        print(color.BOLD, color.BLUE, tweet_FullName, ":" + tweet_Date, color.END)
        print (tweet_text)
    #looking for images

    tweet_image_container =  tweet.find("div", {'class' :"AdaptiveMediaOuterContainer"})

    if(tweet_image_container):
        tweet_image = tweet_image_container.find("img").attrs["src"]
        print(color.BOLD, color.GREEN, tweet_image, color.END)
        '''for photo in tweet_image_container.findAll("img"):
                tweet_image = photo.attrs["src"]
                print(color.color.BOLD, color.color.GREEN, tweet_image, color.color.END)'''
    else:
        print (color.BOLD, color.RED, "No image found", color.END)



'''
htmlFile = open("E:\\Services\\Test\\" + "file2.html", "w+")
htmlFile.write(str(r.text))
htmlFile.close()

htmlFile = "E:\\Services\\Test\\"+search+".html"
with open(htmlFile, 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
'''