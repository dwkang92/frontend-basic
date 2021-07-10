import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

# 중구에 관련된 모든 정보들을 출력한다
# print(rjson['RealtimeCityAir']['row'][0])

gus = rjson['RealtimeCityAir']['row']

# gu와 gus는 임의의 변수라 생각하자.
# 구의 이름과 미세먼지수치를 출력하는 내용.
for gu in gus:
	print(gu['MSRSTE_NM'], gu['IDEX_MVL'])

# IDEX_MVL값이 60 미만인 구만 찍어주기.
for gu in gus:
	if gu['IDEX_MVL'] < 60:
		print (gu['MSRSTE_NM'], gu['IDEX_MVL'])