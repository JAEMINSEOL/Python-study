class ThailandPackage:
    def detail(self):
        print('[태국 패키지 3박 5일] 방콕 신혼 여행 70만원')
        # __name__: str
        
if __name__ == '__main__':
    print('Thailand module 직접 실행')
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print('Thailand 외부에서 모듈 호출')