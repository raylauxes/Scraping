import pandas as pd
import random
import time
from selenium import webdriver

class gCrawler:

    def __init__(self, vocab_list, target_url='https://www.google.com/'):
        self.vocab_list = vocab_list
        self.target_url = target_url

        driver = webdriver.Chrome("C:\WORK\GitHub\Scraping\chromedriver.exe") #Need to download chromdriver.exe
       #OR
       #driver = webdriver.Chrome() #Need to specify chromedriver.exe's location in PATH

        search_string = '"' + f'" "'.join(self.vocab_list) + '"' #Turn input words into a search string
        wait = random.random() #Set wait time to avoid frequent access to search engine
        wait_times = 1
        driver.get(self.target_url) #Access the target url
        time.sleep(wait * wait_times)

        search_box = driver.find_element_by_name("q") #Enter serach string in search box
        search_box.send_keys(search_string)
        time.sleep(wait * wait_times)

        search_box.submit() #Submit (equivalent to pressing "Enter")
        time.sleep(wait * wait_times)

        self.raw_sen = []
        for element in driver.find_elements_by_class_name("aCOpRe"):
            self.raw_sen.append(element.text)


    def output(self, relevant_only=False):

        if not relevant_only:
            result = pd.DataFrame(self.raw_sen)

        else:
            raw_text = ""
            for sen in self.raw_sen:
                 raw_text += sen
            result_in_one = "".join(raw_text)
            processed_sen = [sentence + "。" for sentence in result_in_one.split("。")]

            trimmed_sen = []
            for sen in processed_sen:
                if any([substr in sen for substr in self.vocab_list]):
                    trimmed_sen.append(sen)

            result = pd.DataFrame(trimmed_sen)


        result.to_csv(f"search_results_{'_'.join(self.vocab_list)}.csv", encoding="utf-8-sig")


        # driver.quit() #Quit Chrome

        return result
