# Huffington Post Top Headline Webscraper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Start Webdriver
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def getHuffPostHeadlines():
    
    headlines = []
    
    # Website URL and class name initialization
    URL = "https://www.huffpost.com/news/politics"
    headlineClassName = "card__headline__text"

    # Navigate to Huffington Post's Politics Page
    driver.get(URL)

    # Find and return headlines
    HPheadlines = driver.find_elements_by_class_name(headlineClassName)
    for i in range(len(HPheadlines)):
        headline = HPheadlines[i]
        if (not headline.text.isupper()) and (not (i >= 8 and i <= 13)):
            headlines.append(headline.text)
    return headlines

if __name__ == '__main__':
    print(getHuffPostHeadlines())