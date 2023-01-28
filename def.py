## 함수는 박스라고 생각하면은 된다.
# def open_account(): # 함수는 정의만 되는거지 실제로 호출하기 전까지는 실행이 되지 않는다.
#     print('새로운 계좌가 생성되었습니다.')
#
# open_account() #이렇게 호출문을 작성해줘야 그제서야 호출이 됨.

## ------------전달값과 반환값---------------
# def deposit(balance, money): # 전달값은 함수의 소괄호에 넣으면 된다. (이 예제에서는 지금 잔액이 얼마남았고, 입금할 금액(money)이 얼마인지 적어주는 것이다.)
#     print('입금이 완료되었습니다. 현재 잔액은 {0}원 입니다.'.format(balance+money)) #balance+money 이전 잔액에 현재 입금받는 돈을 더해서 출력
#     return balance + money # return은 반환값이다. (원하는 값을 반환함)
#
# def withdraw(balance,money): # 출금하려는 함수
#     if balance >= money: # 잔액이 출금하려는 돈 보다 많이 있으면!!
#         print('출금 완료되었습니다. 현재 잔액은 {0}원 입니다.'.format(balance - money))
#         return balance - money
#     else :
#         print('출금이 완료되지 않았습니다. 현재 잔액은 {0}원입니다.'.format(balance))
#         return balance
#
# def withdraw_night(balance, money): #저녁에 출금할 경우 수수료가 붙도록
#     commission = 100
#     print('수수료는 {0}원이며, 잔액은 {1}원 입니다.'.format(commission,balance-commission-money))
#     return commission, balance - money - commission # 앞의 commission은 수수료가 지금 얼마가 나왔는지, 뒤의 식은 잔액에서 출금한 돈을 빼고 수수료까지 뺀 것을
# #반환값으로 돌려줌
#
#
#
# balance = 0 # 처음 잔액
# balance = deposit(balance, 10000) # 처음 잔액에 10000원을 더한값을 반환함.
# balance = withdraw(balance, 20000) # 20000원은 10000원보다 큰 금액이므로 출금이 불가능함.
# balance = withdraw(balance,5000) # 5000원은 10000원보다 적으므로 출금이 가능함.
# commission, balance = withdraw_night(balance,500)

## ----------- 기본값 설정----------
# 예를 들어 같은 학교, 같은 학년, 같은 반, 같은 수업을 들을 경우 이 때 사용되는게 기본값이라는 것이다.

# def profile(name, age=28, main_lang='python'):
#     #  이름은 서로 다를테니 그냥 두고 , age와 main_lang은 서로 같으니 기본값으로 =을 사용해서 주는 것이다.
#     # 만약에 age와 main_lang에 밑에서 어떤 값을 넣어주면 그 값을 따르지만 값을 넣어주지 않으면 기본값을로 위의 것을 사용
#     print('이름: {0}\t나이:{1}\t주사용 언어:{2}'.format(name,age,main_lang)) # \t는 구분하는 문자
#
# # 위의 profile함수를 호출하면 이름만 넣어주면 나이와 주사용 언어가 똑같이 나옴을 알 수 있다.
# profile('유재석')
# profile('김태호')


## -------------키워드값을 이용한 함수의 호출----------------
# def profile(name, age, main_lang):
#     print(name,age, main_lang)
#
# # 함수를 호출할 때 키워드값을 입력해서 호출하면 순서에 상관없이 호출을 해도 출력시에는 위의 순서대로 나옴
# profile(name='yoo', main_lang='python', age=36)
#
# profile(main_lang='java', age=25, name='kim')

## -------------------------가변 인자를 이용한 함수의 호출------------------------

# def profile(name, age, lang1,lang2, lang3,lan4,lang5):
#     print('이름:{0}\t나이:{1}\t'.format(name,age),end='') #end='' => 이 문장을 출력하고 나서 이어서 밑에 있는 문장도 계속 출력을 한다는 의미이다.
#     print(lang1,lang2,lang3,lan4,lang5)

# profile('유재석',20,'java', 'python','c','c++','c#')
# # 만약 유재석이 이 언어 이외에 또 다른 언어를 아는 경우에는 함수 자체를 바꿔야 하는 상황이 온다. 이럴 때 쓰는 것이 가변인자이다.
# profile('김태호',25,'mysql','kotlin','','','')


# def profile(name, age, *language): # 서로 다른 개수의 값을 넣어줄 때는 가변인자인 *을 사용할 수 있다.
#     print('이름:{0}\t나이:{1}\t'.format(name,age),end='') #end='' => 이 문장을 출력하고 나서 이어서 밑에 있는 문장도 계속 출력을 한다는 의미이다.
#     for lang in language:
#         print(lang, end='')
#     print()
#
# profile('유재석',20,'java', 'python','c','c++','c#', 'js')
# # 만약 유재석이 이 언어 이외에 또 다른 언어를 아는 경우에는 함수 자체를 바꿔야 하는 상황이 온다. 이럴 때 쓰는 것이 가변인자이다.
# profile('김태호',25,'mysql','kotlin','','','')


## -------------------지역변수와 전역변수----------------

# 지역변수: 함수 내에서만 사용하는 변수이다. 함수 호출이 끝나면 사용이 불가능 하다.
# 전역변수: 프로그램 어디서든 부를 수 있는 것을 전역변수라고 한다.

# gun = 10 # 이게 전역변수가 된다.
# def checkpoint(soldiers): # 경계근무
#     gun = gun - soldiers
#     # 함수 안의 gun은 밖에 있는 gun이 아니고 체크포인트 함수 안에 있는 gun이다. 그러므로 빨간줄이 나는 거임.// 이게 바로 지역변수 이다.
#     print('[함수 내에서] 남은 총: {0}'.format(gun))
#
# checkpoint(2)

## 일반적으로 전역변수를 많이 사용하면 코드가 복잡해지므로 가급적이면 함수의 파라미터로 전달 받아서 사용한다.
# gun = 10
# def checkpoint(soldiers): # 경계근무
#     global gun  # 이 문장의 의미는 전역변수 gun을 이 문장에 쓰겠다는 의미이다.
#
#     gun = gun - soldiers
#     # 함수 안의 gun은 밖에 있는 gun이 아니고 체크포인트 함수 안에 있는 gun이다. 그러므로 빨간줄이 나는 거임.// 이게 바로 지역변수 이다.
#     print('[함수 내에서] 남은 총: {0}'.format(gun))
#
# print('전체 총:{0}'.format(gun))
# checkpoint(2)
# print('남은 총:{0}'.format(gun))

## 함수의 파라메터로 전역변수를 전달하는 방법

# gun1 = 10
# def checkpoint_ret(gun,soldiers):
#     gun = gun - soldiers # return이 없는 gun은 함수 내 지역변수임.
#     print('[함수 내에서] 남은 총: {0}'.format(gun))
#     return gun # 이 return을 활용해 함수 내에서 바껴진 gun이라는 변수를 외부에 던질 수 있다.
#
#
# print('전체 총:{0}'.format(gun1))
#
# gun = checkpoint_ret(gun1,2)
# # 여기서 gun은 checkpoint_ret에서 return한 값을 받는 것임. 전역 변수인 gun1을 받아 checkpoint_ret 함수의 gun에 집어 넣어 주는 것임
# print('남은 총:{0}'.format(gun))

## ----------------------함수 퀴즈 ----------------------------

# Q. 표준 체중을 수하는 프로그램을 작성하시오. (표준체중: 각 키에 적당한 체중)
# (성별에 따른 공식)
# 남자: 키(m) * 키(m) * 22
# 여자: 키(m) * 키(m) * 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
# 1-1: 함수명 = std_weight
# 1-2: 전달값: 키(height), 성별(gender)

# 조건 2: 표준 체중을 소수점 둘째자리까지 표시

#  출력 예제: 키 175cm 남자의 표준 체중은 67.38kg입니다.


# def std_weight(height, gender): # 키는 m단위(실수) => cm로 변환시에는 100으로 나눠야함. , gender = '남자', '여자'
#     if gender == '남자':
#         return height * height * 22
#     else:
#         return height * height * 21
#
# height = int(input('키를 입력해주세요:'))
# gender = input('성별을 입력해주세요:')
# weight = round(std_weight(height / 100, gender), 2)
# # 반올림을 하는 함수인 round 함수를 통해 소수점 두 번째 자리까지만 반환
# # 나누기 100을 하는 이유는 cm로 반환해야 하기때문
#
# print('키 {0}cm의 {1}의 표준체중은 {2}kg 입니다.'.format(height,gender,weight))



