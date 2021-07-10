import requests
from bs4 import BeautifulSoup

# 브라우저에서 엔터친 것마냥 효과를 내어준다. 기본적으로 불러오지못하게 막아둔 웹사이트도 있기 때문에. 보안때문에 막아둠.
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 데이터라는 변수에 받아온 데이터를 넣어준다.
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)
# 변수데이터를 text형태로 표시한다.
soup = BeautifulSoup(data.text, 'html.parser')

# 크롤링이 가능한 이유는, 웹의 동작기능과 관련된다.
# requests로 불러온 데이터들을 가져와서, beautiful_soup으로 솎아낸다.
# 즉, 서버로부터 받아온 데이터 (HTML)중에서 내가 원하는 정보를 잘 솎아내는것.

# 1. 위 코드를 입력한 뒤, 제일먼저 확인 해야할 일: print(soup)으로 내가 입력한 코드에 오류는 없는지 확인한다.
# print(soup)

# 2. beutiful_soup의 사용방법은 크게 두가지가 있다. select_one과 select가 있음.
# 불러온 태그내용중에서 text만 뽑아오고 싶을 때: 변수명.text
# 불러온 태그내용중에서 속성만 뽑아오고 싶을 때: 변수명['href']
# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print(title.text)

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    print(tr)

# :nth-child(2)
#old_content > table > tbody > tr:nth-child(3)