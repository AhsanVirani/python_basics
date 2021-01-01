from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
# print(article.prettify())
headline = article.h2.a.text
# print(headline)

summary = article.find('div', class_='entry-content').p.text
# print(summary)

video_src = article.find('iframe', class_='youtube-player')['src']
# print(video_src)

vid_id = video_src.split('/')[4]
vid_id = vid_id.split('?')[0]
# print(vid_id)

yt_link = f'http://youtube.com/watch?v={vid_id}'
# print(yt_link)


#############################
#
# Loop Over all the articles
#
#############################

csv_file = open('real_parser.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        video_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = video_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'http://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    
    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

### Save it to csv ###