import time
import random
from selenium import webdriver

class gCrawler:

    def __init__(self):
        pass

    def top_10_sites(self, vocab_list, target_url='https://www.google.com/'):

        driver = webdriver.Chrome("C:\WORK\GitHub\Scraping\chromedriver.exe") #Need to download chromdriver.exe
       #OR
       #driver = webdriver.Chrome() #Need to specify chromedriver.exe's location in PATH

        search_string = '"' + f'" "'.join(vocab_list) + '"' #Turn input words into a search string
        wait = random.random() #Set wait time to avoid frequent access to search engine
        wait_times = 1
        driver.get(target_url) #Access the target url
        time.sleep(wait * wait_times)

        search_box = driver.find_element_by_name("q") #Enter serach string in search box
        search_box.send_keys(search_string)
        time.sleep(wait * wait_times)

        search_box.submit() #Submit (equivalent to pressing "Enter")
        time.sleep(wait * wait_times)

        raw_sen = ""
        for element in driver.find_elements_by_class_name("aCOpRe"):
            raw_sen += element.text






        # driver.quit() #Quit Chrome

        return raw_sen