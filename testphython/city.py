import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#1 -> 모든 tr 다 가져오기
#print(soup.selct('#old_content > table > tbody > tr'))
movies = soup.select('#old_content > table > tbody > tr')
#2 -> tr 안에서 title 부분만 뽑아내기

for movie in movies :
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None :
        print(movie.select_one('td.ac > img')['alt'],a_tag.text, movie.select_one('td.point').text)
#        print(movie.select_one('td.point').text)