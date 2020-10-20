import re
import requests
import time

from bs4 import BeautifulSoup
from random import random
from selenium import webdriver

t

def top_10_sites(vocab_list):
    # driver = webdriver.Chrome() #Need to specify chromedriver.exe's location in PATH
    # OR specify it as an argument like this
    driver = webdriver.Chrome("C:\WORK\GitHub\Scraping\chromedriver.exe")

    just_a_sec = random()

    # vocab_list = ["浅草", "デートスポット", "雑貨"]
    search_string = ""
    for i in vocab_list:
        search_string = search_string + i + '"　"'

    driver.get('https://www.google.com/')
    time.sleep(just_a_sec * 1)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys('"' + search_string + '"')
    time.sleep(just_a_sec * 1)
    search_box.submit()
    time.sleep(just_a_sec * 1)

    # for h1 in driver.find_elements_by_tag_name("h1"):
    #    print(h1.text)

    # i = 0
    url_list = []
    XPATH = '//*[@id="rso"]/div/div/div[" + str(i + 1) + "]/div/div/div[1]/a'
    for a in driver.find_elements_by_xpath(XPATH):
        url_list.append(a.get_attribute('href'))

    for i in url_list:
        print(i)
    # driver.quit()