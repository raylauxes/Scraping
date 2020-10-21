import time

### from random import random
import random
from selenium import webdriver

def top_10_sites(vocab_list, target_url='https://www.google.com/'):

    driver = webdriver.Chrome("C:\WORK\GitHub\Scraping\chromedriver.exe")
    # OR
    # driver = webdriver.Chrome() #Need to specify chromedriver.exe's location in PATH

    #Turn input words into a search string
    search_string = '"' + f'" "'.join(vocab_list) + '"'

    #Set wait time to avoid frequent access to search engine
    wait = random.random()

    #Access the target url
    driver.get(target_url)

    time.sleep(wait * 1)

    #Enter serach string in search box
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(search_string)

    time.sleep(wait * 1)

    #Submit (equivalent to pressing "Enter")
    search_box.submit()

    time.sleep(wait * 1)

    result = []
    for element in driver.find_elements_by_class_name("aCOpRe"):
        result.append(element.text)
        print(element.text)
        print("-"*100)


    #Quit Chrome
    # driver.quit()

    return result