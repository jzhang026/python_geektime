import requests
from bs4 import BeautifulSoup as bs
import csv
import time

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url = 'https://movie.douban.com/top250'

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
    with open('movies.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for movie in movies_list:
            writer.writerow(movie)

# main
bs_info = get_info(url, header)
div_movies = bs_info.find_all('div', attrs={'class': 'item'})
movies_list = []
for movie in div_movies:
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