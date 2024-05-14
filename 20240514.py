# \n : 줄바꿈
print('백문이 불여일견 \n백견이 불여일타')

# \', \" : 문장 내 따옴표
print('저는 \'리랩\' 소속입니다.')
print('저도 \"리랩 \" 소속입니다.')
 
# \\ : 문장 내에서 \
print('C\\users')

# \r : 커서를 맨 앞으로 이동
print('Red apple \rPine')

# \b : 1글자 삭제(백스페이스)
print('redd\bapple')

# \t : 탭
print('Red \t Apple')

## quiz
domain = 'http://mysnu.ac.kr'
#규칙 1: http:// 부분은 제외
#규칙 2: 처음 만나는 . 이후 부분은 제외
#규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 갯수 + !
domain_crop = domain.replace('http://',''); domain_crop = domain_crop[:domain_crop.index('.')]
pw =  domain_crop[:3] + str(len(domain_crop)) + str(domain_crop.count('e')) +'!'; print(pw) 

