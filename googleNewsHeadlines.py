# Google News Top Headline Webscraper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Start Webdriver
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def getGoogleNewsHeadlines():
    
    headlines = []
    
    # Website URL and class name initialization
    URL = "https://news.google.com/?hl=en-US&gl=US&ceid=US:en"
    articleClassName = "article"

    # Navigate to Google News's Front Page
    driver.get(URL)

    # Find and return headlines
    articles = driver.find_elements_by_tag_name(articleClassName)
    for article in articles:
        if not len((article.text.split('\n')[0]).strip()) == 0:
            headline = (article.text.split('\n')[0]).strip()
            articleTeaser = (article.text.split('\n')[1]).strip()
            newsOrganization = (article.text.split('\n')[2]).strip()
            timePosted = (article.text.split('\n')[3]).strip()
            headlines.append(headline)
    return headlines
            
            
if __name__ == '__main__':
    print(getGoogleNewsHeadlines())
