import requests
from bs4 import BeautifulSoup
import time
import csv

fp = open('kugoutop500.csv', 'w+', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('rank', 'singer', 'song', 'time'))
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 '
                  'Safari/537.36'
    }
def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ranks = soup.select('div.pc_temp_songlist > ul > li > span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')           #此处由于这个标签和上一个 标签是在同一个标签下，所以可以只要后面部分路径
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().split('-')[0],
            'song': title.get_text().split('-')[1],
            'time': time.get_text().strip()
        }
        print(data)
        writer.writerow((data['rank'], data['singer'], data['song'], data['time']))

if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1, 24)]
    for url in urls:
        get_info(url)
    time.sleep(2)
    fp.close()