#Thomson Reuters Top Headline Webscraper

import requests
from bs4 import BeautifulSoup

URL = 'https://www.reuters.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

def getReutersNewsHeadlines():
    results = soup.find(id='hp-top-news-top')
    titles = results.find_all('h3', class_='story-title')
    topTitle = soup.find(id='topStory').find('h2',class_='story-title')

    print(topTitle.text.strip(), end='\n'*2)
    for title in titles:
        print(title.text.strip(), end='\n'*2)

if __name__ == '__main__':
    getReutersNewsHeadlines()