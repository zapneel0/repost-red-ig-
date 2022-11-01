import praw
import pandas as pd
from RedDownloader import RedDownloader
from pyshorteners import Shortener
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image,ImageDraw,ImageFont
import textwrap as tr
import numpy as np
import cv2
import math
from pilmoji import Pilmoji

reddit_read_only = praw.Reddit(client_id="zgYK-1hEaf57ovim2Y2prQ",                  # your client id
                               client_secret="Dwc43xxKkW66-SCMSr0wHbIVd4zwLw",   # your client secret
                               user_agent="scraper")                                        # your user agent

subreddit = reddit_read_only.subreddit("funny")

sh = Shortener()
s = Service("chromedriver.exe")

## Display the name of the Subreddit
print("Display Name:", subreddit.display_name)
 
## Display the title of the Subreddit
print("Title:", subreddit.title)
 
## Display the description of the Subreddit
print("Description:", subreddit.description)

posts = subreddit.top(time_filter='day' , limit =10)
# Scraping the top posts of the current month
 
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }
'''
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(service=s , options=chrome_options)

driver.get("https://www.instagram.com/accounts/login/")
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('thvibezon')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Meow12345678')
driver.find_element(By.XPATH, '//*[@id="login"]').click()
'''
def post(media):
    driver.find_element(By.XPATH, '//*[contains(@aria-label, "New post")]').click()
    actions = ActionChains(driver)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(1)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(1)
    #enter media


def breaktext(txt):
    output = " "
    lines = tr.wrap(txt, width=40)
    for line in lines:             #
        output = output + line + "\n "
    return output[:-2]           #(40-len(line))*" "+ 


        
def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)
    print("#################"+post.title)
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
    
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
     
    # The score of a post
    posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    posts_dict["Post URL"].append(post.url)
    

    if (post.url).endswith((".png",".jpg",".jpeg")):
        file = open("image.png", "wb")
        file.write(requests.get(post.url).content)
        file.close()

        h,w= cv2.imread("image.png").shape[:2]

        #################################
        fontname = "C:/Users/91943/Desktop/repost/InstagramSans-Bold.ttf"  
        inputtext = post.title    
        colorText = "black"
        colorOutline = "white"
        colorBackground = "white"

        image_1 = cv2.imread("image.png")
        height_1, width_1 = image_1.shape[:2]
        fontsize = int((height_1 + width_1)/40)

        text = breaktext(inputtext)

        font = ImageFont.truetype(fontname, fontsize)
        width, height = getSize(text, font)
        img = Image.new('RGB', (width+4, height+4), colorBackground)
        d = ImageDraw.Draw(img)
        p=Pilmoji(img)
        d.text((2, height/2), text, fill=colorText, anchor="lm", font=font)
        d.rectangle((0, 0, width+3, height+3), outline=None)
        img.save("title.png")    

        image_1 = cv2.imread("image.png")
        image_2 = cv2.imread("title.png")

        height_1, width_1 = image_1.shape[:2]
        height_2, width_2 = image_2.shape[:2]

        if width_1 > width_2:
            img = add_margin(img, 0, (width_1)-(width_2), 0, 0, "white")
            img.save("title.png")

        image_2 = cv2.imread("title.png")

        # Resizing image_2 to match the width of image_1
        new_width_2 = width_1
        new_height_2 = new_width_2 * height_2 // width_2
        image_2 = cv2.resize(image_2, (new_width_2, height_2))

        combined_image = np.vstack((image_2, image_1))

        cv2.imwrite("combined_image.png", combined_image)
        i = Image.open("combined_image.png")
        #i.show("combined_image.jpg")
        #i.save()
        #.close()




        old_size = i.size
        if max(old_size) == old_size[1]:
            change="side"
            if (old_size[1]/5)*4 < old_size[0]:
                new_size = (old_size[1],old_size[1])#1:1
                ratio="1:1"
            else:
                new_size = ((old_size[1]/5)*4,old_size[1])#4:5
                ratio="4:5"
            new_size = (old_size[1],old_size[1])###############
        else:
            change="top"
            if old_size[1] > (old_size[0]/16)*9:
                new_size = (old_size[0],old_size[0])#1:1
                ratio="1:1"
            else:
                new_size = (old_size[0],(old_size[0]/16)*9)#16:9
                ratio="16:9"
            new_size = (old_size[0],old_size[0])###############

        new_size = (math.ceil(new_size[0]),math.ceil(new_size[1]))
        """        
        while type(new_size[1]) != "int" or type(new_size[0]) != "int":
            if ratio == "1:1":
                new_size = (math.ceil(new_size[0]),math.ceil(new_size[1]))
            if ratio == "4:5":
                new_size = (math.ceil(new_size[0]),math.ceil(new_size[1]))
                if math.ceil(new_size[0])/math.ceil(new_size[1]) != 4/5:
                    new_size = ((math.ceil(new_size[1])/5)*4,math.ceil(new_size[1]))
            if ratio == "16:9":
                new_size = (math.ceil(new_size[0]),math.ceil(new_size[1]))
                if math.ceil(new_size[0])/math.ceil(new_size[1]) != 16/9:
                    new_size = (math.ceil(new_size[0]),(math.ceil(new_size[0])/16)*9)

        """
        new_im = Image.new("RGB", new_size, "Black")   ## luckily, this is already black!
        box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
        new_im.paste(i, box)

        new_im.show()
        new_im.save("post.png")
        time.sleep(10)
        #new_im.close()

        #post("post.png")
    
#################################
'''
    if (post.url).endswith((".gif")):
        file = open(post.id + ".gif", "wb")
        file.write(requests.get(post.url).content)
        file.close()    
    else:
        file = RedDownloader.Download(url = sh.tinyurl.expand(post.url)  , output=post.id , quality = 720) 
'''
'''
    #add post title to white border
    file = media
    post(media)
'''
