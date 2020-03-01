import requests

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
google = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
url = 'https://book.douban.com/top250'
header = {
    'user-agent': google,
}
# urllib3 是request内部用来解析url的包
response = requests.get(url, headers=header)

# print(response.text)

from bs4 import BeautifulSoup as bs
bs_info = bs(response.text, 'html.parser')
div_pl = bs_info.find_all('div', attrs={'class': 'pl2'})

# 格式化字符串的方法
# 1 print('the value of pi is %5.3f' % Math.pi)
# 2 print('{1} and {0}'.format('egg', 'spam'))
# 3 print()
for tags in div_pl:
    for atag in tags.find_all('a'):
        print(atag.get('href'))
        print(atag.get('title'))