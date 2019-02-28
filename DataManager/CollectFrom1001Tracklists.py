from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


URL_1001TRACKLISTS_LIST_YEAR_HEAD = 'https://www.1001tracklists.com/year/2019/index'
URL_1001TRACKLISTS_LIST_YEAR_TAIL = '.html'

def getCurrentListYearURL():
    CurrentUrl = URL_1001TRACKLISTS_LIST_YEAR_HEAD + URL_1001TRACKLISTS_LIST_YEAR_TAIL
    return CurrentUrl

def CollectFromListYearSelenium(year):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('chromedriver', chrome_options=options)

    BaseURL = 'https://www.1001tracklists.com/year/' + str(year) + '/index.html'
    print("Base URL was generated.", BaseURL)
    XPATH_MAX_INDEX = '//*[@id="middleTbl"]/tbody/tr/td/ul/li[13]/a'
    MAX_INDEX = 0

    driver.get(BaseURL)
    driver.implicitly_wait(3)
    MAX_INDEX = driver.find_element_by_xpath(XPATH_MAX_INDEX)
    print(MAX_INDEX, MAX_INDEX.text)
    return int(MAX_INDEX.text)