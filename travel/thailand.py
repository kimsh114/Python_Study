class ThailandPackage:
    def detail(self):
        print('[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원')



if __name__ == "__main__":
# 이것은 이 모듈에서만 직접 실행이 될 뿐 다른 모듈에서 이 모듈을 import 할 경우에는 실행이 되지 않음. // 그러므로 이 모듈의 실행여부를 테스트하기 좋음.

    print('이 문장은 thailand 모듈을 직접 실행할 때만 실행됩니다.')
    trip_to = ThailandPackage()
    trip_to.detail()
else: # 다른 곳에서 이 모듈을 사용할 때는 이 문장이 생성
    print('thailand 외부에서 모듈 호출')