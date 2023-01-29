## 모듈은 쉽게 필요한 것들끼리 부품처럼 잘 만들어진 파일이라고 보면됨
## 파이썬에서는 함수정의나 클래스 등의 파이썬 문장들을 담고 있는 것들을 모듈이라고 한다.
## 모듈은 내가 쓰려고자 하는 파일과 같은 경로상에 있어야 한다.

###------------import를 이용한 모듈의 활용-----------------
# import theater_module
#
# # 내가 만들어 놓은 모듈을 활용하려면 이런식으로 우선 import를 하고 모듈.함수명/클래스명 이렇게 사용가능
# theater_module.price(3)  # 이 내용은 theater_module에 있는 price 함수를 쓰는 것임. 3명이서 영화를 보러 갔을 때 가격
# theater_module.price_morning(4) # 조조할인
# theater_module.price_soldier(5) # 군인할인



###---------------import에 as 붙이기-------------

# import theater_module as mv #  모듈명이 길 때는 별명을 사용하자
#
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

###---------------from import-------------
# from theater_module import * # theater_module에서 전체 다 사용하겠다는 의미이다.
# price(3)
# price_soldier(4)
# price_soldier(5)

## -----------------from import 인데 내가 필요한 함수만 사용-----------

# from theater_module import price_morning as pm # 하나만 쓰려면 as를 붙여서 별명입력도 가능하다.
# pm(6)