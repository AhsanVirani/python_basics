# Beautiful soup parser
# Created by Ahsan Muhammad

from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# match = soup.find('div', class_='footer')
# print(match)

# # parsing the 1st article heading 
# article = soup.find('div', class_='article')
#print(article)


# # Grabbing article headline an summary
# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)

## Find all the articles here now
# article = soup.find_all('div', class_='article')
#print(article)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    
    print()
