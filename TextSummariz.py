import bs4 as bs
import urllib.request
import re

scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scraped_data.read()
# print(article)
parsed_article = bs.BeautifulSoup(article,'lxml')
# print(parsed_article)
paragraphs = parsed_article.find_all('p')
# print(paragraphs)
article_text = ""

for p in paragraphs:
    article_text += p.text
print(article_text)