import os
import time
import praw
import wget
import shutil

from PIL import Image
from pathlib import Path
from instabot import Bot

def create_client(ID, SECRET, AGENT):
    client = praw.Reddit(
        client_id=ID,
        client_secret=SECRET,
        user_agent=AGENT,
    )
    return client

def is_image(post):
    try:
        return post.post_hint == "image"
    except AttributeError:
        return False


def get_url(client, SUBNAME, limit):
    top_memes = client.subreddit(SUBNAME).top("hour", limit=limit)
    image_urls = list()

    for post in top_memes:
        if is_image(post):
            image_urls.append(post.url)
    
    return image_urls

def scrape(SUBNAME, ID, SECRET, AGENT, LIMIT=10):
    client = create_client(ID=ID, SECRET=SECRET, AGENT=AGENT)
    urls = get_url(client=client, SUBNAME=SUBNAME, limit=LIMIT)
    return urls

def download(URL):
    os.makedirs("./temp", exist_ok=True)
    TEMPPATH = "./temp"
    try:
        f = open("banlist.txt","a")
        f.close()
    except:
        f = open("banlist.txt","w")
        f.close()

    for i in URL:
        end = i[-3:]

        if end == "gif":
            continue

        blist = open("banlist.txt")

        if i not in blist.read():
            print(i)
            blist.close()

            with open("banlist.txt", "a") as blist:
                blist.write(i + "\n")
                wget.download(i, TEMPPATH)

        else:
            continue

def square(min_size=256, fill_color=(255, 255, 255, 0)):
    os.makedirs("./upload", exist_ok=True)
    name = 0
    for file in os.scandir("./temp"):
        name += 1
        IMG = Image.open(file.path)
        x, y = IMG.size
        size = max(min_size, x, y)
        new_IMAGE = Image.new('RGB', (size, size), fill_color)
        new_IMAGE.paste(IMG, (int((size - x) / 2), int((size - y) / 2)))
        new_IMAGE.save(f"./upload/{str(name)}.jpg", quality = 95)
    shutil.rmtree("./temp")

def upload(USER, PASS, CAPTION="", DELAY=5):
    try: 
        os.remove(f"config/{USER}_uuid_and_cookie.json")
        bot = Bot()
        bot.login(username=USER, password=PASS)
    except:
        bot = Bot()
        bot.login(username=USER, password=PASS)

    images = "./upload/"

    for image in os.listdir(images):
        bot.upload_photo(images + image, caption=CAPTION)
        time.sleep(DELAY)

    shutil.rmtree("./upload")

def Auto(USER, PASS, SUBNAME, ID, SECRET, AGENT, LIMIT=10, DELAY=5, CAPTION=""):
    links = scrape(SUBNAME=SUBNAME, ID=ID, SECRET=SECRET, AGENT=AGENT, LIMIT=LIMIT)
    download(URL=links)
    square()
    upload(USER=USER, PASS=PASS, CAPTION=CAPTION, DELAY=DELAY)