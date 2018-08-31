from bs4 import BeautifulSoup
import requests
import time
import lxml
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 '
                  'Safari/537.36'
    }

fp = open('test.csv', 'w+', newline='', encoding='utf8')
writer = csv.writer(fp)
writer.writerow(('sex','address','name', 'price', 'img', 'tittle'))


def judgment_sex(class_name):
    if class_name == ['member_girl_ico']:
        return '女'
    else:
        return '男'

def get_links(url):
    wb_data = requests.get(url, headers=headers)
    print(wb_data.status_code)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get("href")
        get_info(href)

def get_info(url):
    wb_date = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_date.text, 'lxml')
    tittles = soup.select('div.pho_info > h4 > em')
    addresses = soup.select('div.pho_info > p > span')
    prices = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#curBigImage')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')
    for tittle, address, price, img, name, sex in zip(tittles, addresses,prices,imgs, names,sexs):
        date = {
            'tittle': tittle.get_text().strip(),
            'address': address.get_text().strip(),
            'price': price.get_text(),
            'img': img.get("src"),
            'name': name.get_text(),
            'sex': judgment_sex(sex.get("class"))
        }
        print(date)
        writer.writerow((date['sex'],date['address'], date['name'], date['price'], date['img'], date['tittle']))




if __name__ == '__main__':
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1, 2)]
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)
        fp.close()


