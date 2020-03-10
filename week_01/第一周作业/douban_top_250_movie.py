import requests
from bs4 import BeautifulSoup as bs
import csv
import time
import math
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
# requet a webpage and parse it with beatifulsoup
def get_info(url, header):
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        bs_info = bs(response.text, 'html.parser')
        return bs_info
    else:
        print('Hello, kite. %s requests error' % (url,))

# save csv
def write_csv(movies_list):
    with open('movies.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for movie in movies_list:
            writer.writerow(movie)
def read_csv():
    with open('movies.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        return sum(1 for row in reader)

line_nums = read_csv()
page_size = 25
start_page_number = math.floor(line_nums / page_size)
start_index = line_nums - round(start_page_number * page_size, 0)
url = 'https://movie.douban.com/top250'
# https://movie.douban.com/top250?start=25
page_urls = ['{0}?start={1}'.format(url, 25 * i) for i in range(start_page_number, 10)]
# main
for i in range(len(page_urls)): 
    page_url = page_urls[i]
    bs_info = get_info(page_url, header)
    div_movies = bs_info.find_all('div', attrs={'class': 'item'})
    movies_list = []
    for j in range(len(div_movies)):
        if i == 0 and j < start_index:
            continue
        movie = div_movies[j]
        # get movie name, rating and amount of rating
        name = movie.find_all('span', attrs={'class': 'title'})[0].get_text()
        rating = movie.find_all('span', attrs={'class': 'rating_num'})[0].get_text()
        rating_amount = movie.find_all('div', attrs={'class': 'star'})[0].find_all('span')[3].get_text()

        # get movie link
        movie_link = movie.find_all('a')[0].get('href')
        time.sleep(5)
        print('Hello, kite, processing %s' % (name,))
        movie_detail_info = get_info(movie_link, header)

        temp = [name, rating, rating_amount, movie_link]

        # get comment
        hot_comments = movie_detail_info.find(id = 'hot-comments')
        for comment in hot_comments.find_all('div', attrs={'class': 'comment-item'}):
            comment_texts = comment.find_all('span', attrs={'class': 'short'})
            if len(comment_texts) > 0:
                temp.append(comment_texts[0].get_text())

        movies_list.append(temp)
    write_csv(movies_list)