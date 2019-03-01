from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


URL_1001TRACKLISTS_LIST_YEAR_HEAD = 'https://www.1001tracklists.com/year/'
URL_1001TRACKLISTS_LIST_YEAR_MID  = '/index'
URL_1001TRACKLISTS_LIST_YEAR_TAIL = '.html'

def getCurrentListYearURL():
    CurrentUrl = URL_1001TRACKLISTS_LIST_YEAR_HEAD + URL_1001TRACKLISTS_LIST_YEAR_TAIL
    return CurrentUrl

def CollectFromListYearBS4(year):
    lengthoflist = {'2018' : 1099, '2017' : 961}
    BaseURL = 'https://www.1001tracklists.com/year/' + str(year) + '/index.html'
    print("Base URL was generated.", BaseURL)
    MAX_INDEX = lengthoflist[str(year)]
    '''
    req = requests.get('https://www.1001tracklists.com/tracklist/2cms9wl9/charlotte-de-witte-new-years-day-awakenings-gashouder-amsterdam-netherlands-2018-01-01.html')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    '''
    return MAX_INDEX

def CollectFromListYearSelenium(year):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('chromedriver', chrome_options=options)

    BaseURL = 'https://www.1001tracklists.com/year/' + str(year) + '/index.html'
    print("Base URL was generated.", BaseURL)
    XPATH_MAX_INDEX = '//*[@id="middleTbl"]/tbody/tr/td/ul/li[13]/a'
    MAX_INDEX = 0

    driver.get(BaseURL)
    driver.implicitly_wait(10)
    MAX_INDEX = int(driver.find_element_by_xpath(XPATH_MAX_INDEX).text)

    SELECTOR_PLAYLIST = 'article > div:nth-child(1) > div > div.tlLink > a'
    playlists = driver.find_elements_by_css_selector(SELECTOR_PLAYLIST)

    for index in range(1, MAX_INDEX + 1):
        CurrentURL = URL_1001TRACKLISTS_LIST_YEAR_HEAD + str(year) + URL_1001TRACKLISTS_LIST_YEAR_MID + str(index) + URL_1001TRACKLISTS_LIST_YEAR_TAIL
        print(CurrentURL)

    for playlist in playlists:
        print(playlist.text, '|', playlist.get_attribute('href'))



    return MAX_INDEX