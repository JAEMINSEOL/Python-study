# Quiz. 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1. http:// 부분은 제외하고 naver.com 만 남기기
# 규칙2. 처음만나는 점 이후의 부분은 제외하고 naver만 남기기
# 규칙3. 남은 글자 중 처음 세자리 + 글자 수 + 글자 내 e의 수 + !로 구성하기

# 예) 생성된 비밀번호: nav51!

site = 'http://google.com'
r1 = site.replace("http://","")
r2 = r1[:r1.find('.')]
pw= r2[:3]+str(len(r2))+str(r2.count('e')) +'!'

print(f'{site} 의 생성된 비밀번호 : {pw}')