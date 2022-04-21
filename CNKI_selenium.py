from selenium import webdriver
import pandas as pd
from itertools import zip_longest
import time
import random
import os

def crawler_paper():
    opt=webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches', ['enable-automation']) 
    chrome_driver = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    driver=webdriver.Chrome(executable_path=chrome_driver)
    driver.get('https://www.cnki.net/')
    time.sleep(2)
    search=driver.find_element_by_id('txt_SearchText')
    search.send_keys('大数据')
    submit=driver.find_element_by_class_name('search-btn')
    submit.click()
    time.sleep(3)
    df=[]
    

    for page in range(1,3):
        try:
            elements = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/form/div/table/tbody/tr/td[2]/a')
            for telement in elements:
                df.append(telement.text)
                print(telement.text)
            driver.find_element_by_xpath('//*[@id="PageNext"]').click()
            time.sleep(random.randint(2,5))
        except:
            print('未爬到数据')
            time.sleep(10)
    return df


if __name__=='__main__':
    data=crawler_paper()
