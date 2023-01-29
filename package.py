# travel 폴더 안의 thailand 모듈에 대한 것들을 사용하는 방법이다.
### -----------import로 다른 파일 안의 모듈을 사용하는 법----------------------

# import travel.thailand # import 뒤의 부분은 모듈이나 패키지만 가능하다. 클래스나 함수는 사용불가 사용하려면 아래처럼 사용.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

###----------------from import를 통해 다른 파일 안의 모듈을 사용하는 법------------------
# from travel.thailand import ThailandPackage # 여기서는 모듈 안의 특정 클래스나 함수도 사용이 가능하다.
#
# trip_to = ThailandPackage()
# trip_to.detail()


###------------------- __all__----------------------------
## travel 파일 안의 __init__ 모듈에서 __all__에 배트남을 집어넣었더니 사용이 가능함.
## 만약 태국 모듈을 사용하고자 해서 당장 여기에 적으면 사용이 불가능 함. __init__ 모듈에 태국도 넣어줘야 함.
# from travel import *
# trip_to = vietnam.vietnamPackage()
# trip_to.detail()