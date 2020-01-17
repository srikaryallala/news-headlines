# Reuters Top Headlines Webscraper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Start Webdriver
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def getReutersNewsHeadlines():
    # Website URL and class name initialization
    URL = "https://www.reuters.com/"
    headlineClassName = "story-title"

    # Navigate to Reuters' front page
    driver.get(URL)

    # Find and print headlines
    headlines = driver.find_elements_by_class_name(headlineClassName)
    for headline in headlines:
        print(headline.text + '\n')

if __name__ == '__main__':
    getReutersNewsHeadlines()