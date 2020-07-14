#!/usr/bin/env python
import requests
import time
import pyfiglet
from fake_useragent import UserAgent
from pprint import pprint
from bs4 import BeautifulSoup
from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Fake User Agent
ua  = UserAgent()
#print(ua.random)

#Headers
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,app$",
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
    "Dnt": "1", 
    "Referer": "https://www.google.com/",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": str(ua.random), 
  }

#Fake-Browser
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.binary_location = '/usr/bin/google-chrome-stable'


#Banner
custom_fig = Figlet(font='cybermedium')
print(custom_fig.renderText('Shagohod'))
message = 'Your random header'
#print(message + ua.random)

#Site Input
URL = input("What site would you like to scrape?[http://www.example.com]")
html_text = requests.get(URL, headers=headers)
soup = BeautifulSoup(html_text.content, 'html.parser')

#Print
print (vars(soup))

