import requests
import numpy as np
import re
from bs4 import BeautifulSoup



def get_article():
  """ Content Creator.
  Returns content of fist article at diken.com.tr/kategori/dunya/"""
  content = ''
  url = 'https://www.diken.com.tr/kategori/dunya/'
  r = requests.get(url)
  if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html5lib')
    articles = soup.find_all('article')
    article_link = articles[0].find('a', {'class':'entry-image-link'})['href']
    article_r = requests.get(article_link)
    article_soup = BeautifulSoup(article_r.content, 'html5lib')
    article_content = article_soup.find('div', {'class':'entry-content'}).find_all('p')
    for i in article_content:
      content = content + i.get_text(strip=True) + ' '
      content = re.sub("[\(\[].*?[\)\]]", "", content)
    return content