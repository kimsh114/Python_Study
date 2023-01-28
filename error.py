### 에러가 발생했을 때 그것에 대해서 처리를 해주는 것을 말한다.
# try:
#     print('나누기 전용 계산기 입니다.')
#
#     num1 = int(input('첫 번째 숫자를 입력하세요 :'))
#     num2 = int(input('첫 번째 숫자를 입력하세요 :'))
#     print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
# except ValueError:
#                 print('에러! 잘못된 값을 입력했습니다.')
# # try 내부의 문장을 실행하다가 ValueError가 발생했을 때 밑에 있는 except를 찾아서 그 except의 문장을 실행함.
# except ZeroDivisionError as err:
#     print(err) # ValueError나 ZeroDivisionError와 같이 명확한 에러들은 이렇게 예외처리가 가능하다.

##-----------

# try:
#     print('나누기 전용 계산기 입니다.')
#     nums = []
#
#     nums.append(int(input('첫 번째 숫자를 입력하세요 :')))
#     nums.append(int(input('첫 번째 숫자를 입력하세요 :')))
#     ## nums.append(int(nums[0] / nums[1]))  # 만약 깜빡 잊어버리고 이 부분을 못 썻다고 가정하면 인덱스 에러가 뜸
#     print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))
# except ValueError:
#                 print('에러! 잘못된 값을 입력했습니다.')
# except ZeroDivisionError as err:
#     print(err)
#
# except Exception as err: # 이렇게 쓰면 ValueError 나 ZeroDivisionError가 아닌 오류들에 대해 예외처리가 되고 어떤 에러가 떴는지 알 수 있다.
#     print('알 수 없는 에러가 발생했습니다.')
#     print(err)


###-------------의도적으로 에러 발생시키기---------------------

## 한 자리 숫자에 대해서만 나누기가 가능한 계산기를 만든다고 가정

# try:
#     print('한 자리 숫자 나누기 전용 계산기 입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError # 만약에 num1과 num2가 두 자리수일 경우에는 ValueError를 일으키겠다는 의미이다.
#     print('{0} / {1} = {2}'.format(num1, num2, num1/num2))
# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력해주세요')


###---------사용자 정의 예외처리---------------------

# ValueError나 IndexError 등은 파이썬에서 정의하고 있는 에러들인데, 이러한 에러들 말고 내가 직접 에러를 정해주는 경우도 만들 수 있다.

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg # 우리가 직접 메시지를 적고 싶을 경우
#
#     def __str__(self):
#         return self.msg
#
# try:
#     print('한 자리 숫자 나누기 전용 계산기 입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError('입력값: {0}, {1}'.format(num1, num2)) # BigNumberError를 발생시키는데 어떤 입력값이 잘못되었는지를 알려주고싶을 때
#     print('{0} / {1} = {2}'.format(num1, num2, num1/num2))
# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력해주세요')
# except BigNumberError as err:
#     print('에러가 발생했습니다. 한 자리 숫자만 입력해주세요')
#     print(err)

###----------------finally-------------
## finally는 예외처리 구문에서 정상적으로 작동을 하건 오류가 나건 상관없이 무조건 실행이 되는 구문이다.

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg # 우리가 직접 메시지를 적고 싶을 경우
#
#     def __str__(self):
#         return self.msg
#
# try:
#     print('한 자리 숫자 나누기 전용 계산기 입니다.')
#     num1 = int(input('첫 번째 숫자를 입력하세요: '))
#     num2 = int(input('두 번째 숫자를 입력하세요: '))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError('입력값: {0}, {1}'.format(num1, num2)) # BigNumberError를 발생시키는데 어떤 입력값이 잘못되었는지를 알려주고싶을 때
#     print('{0} / {1} = {2}'.format(num1, num2, num1/num2))
# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력해주세요')
# except BigNumberError as err:
#     print('에러가 발생했습니다. 한 자리 숫자만 입력해주세요')
#     print(err)
#
# finally:
#     print('계산이 완료되었습니다.') # 에러가 나오건 정상적으로 작동하건 관계없이 이 문장이 출력이 됨.


###---------------퀴즈----------------------
# 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작했습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리하기.
#        출력 메시지 : '잘못된 값을 입력했습니다.'
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨양은 10마리로 한정하기
#         치킨 소진 시 사용자 정의 예러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지: '재고가 소진되어 더 이상 주문을 받지 않습니다.'


chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작

class SoldOutError(Exception):
    pass

while True:
        try:
           print('[남은치킨 : {0}]'.format(chicken))
           order = int(input('치킨 몇 마리 주문하시겠습니까?'))
           if order > chicken:
              print('재료가 부족합니다.')

           elif order < 1:
               raise ValueError

           else:
              print('[대기번호 {0}] {1}마리 주문이 완료되었습니다.'.format(waiting, order))
              waiting += 1
              chicken -= order

           if chicken == 0:
                raise SoldOutError

        except ValueError:
            print('잘못된 값을 입력했습니다.')

        except SoldOutError:
            print('재료가 다 소진되어 더이상 주문을 받지 않습니다.')
            break
