import requests
from bs4 import BeautifulSoup

def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    text= soup.get_text()

    #num = int(input("How many paragraphs?"))
    print(text[1500:1800])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Wikipedia")

