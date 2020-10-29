from bs4 import BeautifulSoup
import requests
from splinter import Browser

import pandas as pd

import time

def scraper():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    firstItem=soup.find("div",class_="list_text")

    title=firstItem.find("div",class_="content_title").text
    teaser=firstItem.find("div",class_="article_teaser_body").text

    toReturn={"article title":title,"article teaser":teaser}

    browser.quit()

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image=soup.find("a",class_="button fancybox")["data-fancybox-href"]
    image=f"https://www.jpl.nasa.gov/{image}"

    toReturn["featured image"]=image

    browser.quit()

    table = pd.read_html("https://space-facts.com/mars/")[0]

    toReturn["Mars Facts"]=table.to_html('table.html')

    return toReturn