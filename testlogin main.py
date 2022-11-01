from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import autoit
import random

s = Service("chromedriver.exe")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(service=s , options=chrome_options)

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('thvibezon')
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('Meow12345678')
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(4)
####
hashtaglist=[
"#ReelsInstagram",
"#VideoOfTheDay",
"#ReelsIndia",
"#ReelSteady",
"#disney",
"#ForYouPage",
"#InstagramReels",
"#bhfyp",
"#instareels",
"#reelsinsta",
"#fyp",
"#ReelsOfInstagram",
"#TikTokIndia",
"#HolaReels",
"#reels",
"#ReelsBrasil",
"#k",
"#ReelsVideo",
"#instareel",
"#music",
"#instafood",
"#FoodBlogger",
"#lunch",
"#PicOfTheDay",
"#instadaily",
"#FoodPhotography",
"#PhotoOfTheDay",
"#food",
"#healthy",
"#foodie",
"#FoodLover",
"#bhfyp",
"#instagood",
"#tasty",
"#delicious",
"#foodstagram",
"#homemade",
"#cooking",
"#FoodPorn",
"#love",
"#foodgasm",
"#foodies",
"#HealthyFood",
"#dinner",
"#yummy",
"#restaurant",
"#TravelPhotography",
"#PicOfTheDay",
"#NaturePhotography",
"#TravelBlogger",
"#beautiful",
"#landscape",
"#adventure",
"#explore",
"#instatravel",
"#photo",
"#trip",
"#summer",
"#travelgram",
"#photography",
"#art",
"#travel",
"#wanderlust",
"#nature",
"#instagood",
"#PhotoOfTheDay",
"#CatLover",
"#of",
"#DogLovers",
"#cute",
"#cats",
"#dogstagram",
"#puppy",
"#catstagram",
"#dogs",
"#animal",
"#animals",
"#DogLife",
"#cachorro",
"#instagram",
"#DogOfTheDay",
"#love",
"#pets",
"#petstagram",
"#PetLovers",
"#DogsOfInstagram",
"#dog",
"#doglover",
"#instagood",
"#instapet",
"#PetsOfInstagram",
"#CatsOfInstagram",
"#pet",
"#cat",
"#instadog",
"#instadaily",
"#LikesForLikes",
"#instagram",
"#fashion",
"#me",
"#FollowMe",
"#love",
"#photography",
"#LikeForLike",
"#like",
"#followers",
"#likes",
"#LikeForLikes",
"#FollowForFollow",
"#myself",
"#f",
"#instalike",
"#comment",
"#beautiful",
"#LikeForFollow",
"#instagood",
"#l",
"#FollowBack",
"#smile",
"#PhotoOfTheDay",
"#FollowForFollowBack",
"#follow",
"#bhfyp",
"#PicOfTheDay",
"#love",
"#instagood",
"#photooftheday",
"#fashion",
"#beautiful",
"#happy",
"#cute",
"#tbt",
"#like4like",
"#followme",
"#picoftheday",
"#follow",
"#me",
"#selfie",
"#summer",
"#art",
"#instadaily",
"#friends",
"#repost",
"#nature",
"#fun",
"#style",
"#smile",
"#food",
"#instalike",
"#likeforlike",
"#family",
"#travel",
"#fitness",
"#euro2020",
"#tagsforlikes",
"#follow4follow",
"#nofilter",
"#life",
"#beauty",
"#amazing",
"#instamood",
"#igers",
"#instagram",
"#photo",
"#music",
"#photography",
"#makeup",
"#dog",
"#beach",
"#sunset",
"#model",
"#foodporn",
"#motivation",
"#followforfollow",
"#sky",
"#lifestyle",
"#design",
"#gym",
"#f4f",
"#toofunny",
"#cat",
"#handmade",
"#hair",
"#vscocam",
"#bestoftheday",
"#vsco",
"#funny",
"#dogsofinstagram",
"#drawing",
"#artist",
"#f4fl",
"#flowers",
"#baby",
"#wedding",
"#girls",
"#instapic",
"#pretty",
"#photographer",
"#instafood",
"#party",
"#inspiration",
"#lol",
"#cool",
"#workout",
"#likeforfollow",
"#swag",
"#fit",
"#healthy",
"#yummy",
"#blackandwhite",
"#foodie",
"#moda",
"#home",
"#christmas",
"#black",
"#memes",
"#winter",
"#pink",
"#sea",
"#landscape",
"#blue",
"#london",
"#holiday"
]

hashtags=""
for i in range(9):
    hashtags = hashtags + " " + random.choice(hashtaglist)

def post():
    driver.find_element(By.XPATH, '//*[contains(@aria-label, "New post")]').click()
    actions = ActionChains(driver)
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(1)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(1)
    autoit.control_set_text("Open", "Edit1", "C:\\Users\\91943\\Desktop\\repost\\post.png")
    time.sleep(1)
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(1)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(1)
    #press ratio button
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
    time.sleep(1)
    caption_field = driver.find_element(By.TAG_NAME, "textarea")
    time.sleep(1)
    caption_field.send_keys("""
follow @"""+pagename+""" for more!
.
.
.
.
"""+hashtags)
