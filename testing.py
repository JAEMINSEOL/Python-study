# 자연수만 입력하세요!
import math

str='1'
while True:
    try: 
    
        str=(input('자연수만 입력하세요:'))
        if str=='그만':
            break
        str=float(str)
        if str<=0:
           print( "양수로 입력하세요!")
        elif str!=math.floor(str):
            print("정수로 입력하세요!")
        else:
            print("감사합니다!")
    except:
        print("숫자를 입력하세요!")
    else:
        print("숫자로 입력해주셨군요!")
    finally:
        print("다음 사이클을 시작합니다\n\n")
        
print("알겠습니다. 종료합니다.")
