import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import Counter
import os

chrome_options = Options()
chrome_options.add_extension('extension_1_2_6.crx')
driver = webdriver.Chrome("C:/Users/evreka/Desktop/chromedriver.exe", chrome_options=chrome_options)

def get_info():
    page1_results = driver.find_elements(By.XPATH, "//div/h3/a")
    for item in page1_results:
        print(item.text)

def search_on_google(param):
    time.sleep(2)
    driver.get("https://www.google.com.tr/advanced_search?q="+param+"&dcr=0&hl=tr")
    time.sleep(2)
    ## dil ##
    driver.find_element_by_xpath("//div[@class='goog-select _oB goog-inline-block goog-flat-menu-button'][@id='lr_button']").click()
    driver.find_element_by_css_selector("[value='lang_tr']").click()
    time.sleep(2)
    ## bölge ##
    driver.find_element_by_xpath("//div[@class='goog-select _oB goog-inline-block goog-flat-menu-button'][@id='cr_button']").click()
    driver.find_element_by_css_selector("[value='countryTR']").click()
    time.sleep(2)
    ## date ##
    driver.find_element_by_xpath("//div[@class='goog-select _oB goog-inline-block goog-flat-menu-button'][@id='as_qdr_button']").click()
    driver.find_element_by_css_selector("[value='y']").click() #d = dat w =week  m=mounth y=year all=any time
    time.sleep(2)
    ##input##
    driver.find_element_by_xpath("//input[@class='jfk-button jfk-button-action _JQ']").click()
    time.sleep(2)
    ##haberlere git ##
    driver.find_element_by_link_text("Haberler").click()

    ##get info ##
    page1_results = driver.find_elements(By.XPATH, "//div/h3/a")
    for item in page1_results:
        print(item.text)

    page_count=driver.find_elements_by_tag_name("td")
    liste_count=[]
    for el in page_count:
        liste_count.append(el.text)
    print(len(liste_count))
    try:
        for i in range(len(liste_count)):
            z=(i+3)
            print(z)
            tty=driver.find_element_by_xpath('//*[@id="nav"]/tbody/tr/td['+str(z)+']/a').get_attribute("href")
            driver.get(tty)
            get_info()
            print(tty)
    except:
        pass


search_on_google("evreka")

