## for 반복문
# for waitting_num in range(1,101): #  for i in x: => x를 i에 대입을 하겠다.
#     print('대기번호: {0}'.format(waitting_num))

# starbucks = ['a', 'b', 'c', 'd']
# for i in starbucks:
#     print('{0} 손님 음료 나왔습니다.'.format(i))



# #---------------------------------------------------------
##while 조건 반복문(어떤 조건을 만족할 때 까지 반복하라)
# # 예제 1
# customer = 'a'
# index = 5
# while index >= 1:
#     print('{0} 손님 음료 나왔습니다.{1} 번 남았어요.'.format(customer, index))
#     index -=1
#     if index == 0:
#         print('커피는 폐기처분 되었습니다.')

##----------------------- while 예제 2 : 무한루프-------------------
#
# customer = 'b'
# index = 1
#
# while True: # 이걸 무한루프라고 한다. => 계속해서 반복하는 것이다. // ctrl+ c를 누르면 강제 종료가 된다.
#     print('{0} 손님 음료 나왔습니다. 호출 {1}회'.format(customer, index))
#     index += 1

## ------------------while 예제 3: 원하는 손님이 올 때까지 이름을 부르는 법----------------
# customer = 'a'
# person = 'unknown'
# number = 35
#
# while person != customer : # while 문은 조건을 만족할 때까지 계속 이 안에서 반복함. 그러므로 여기서는 person과 customer가 서로 다르면 계속 반복하는 거임.
## 내가 원하는 손님인 a가 오면 그제서야 이 반복문을 나가는 것임.
#     print('{0} 음료 준비 되었습니다. '.format(customer))
#     person = input ('이름이 어떻게 되세요?')


##---------------------continue/break-----------------
# absent = [2,5] # continue는 예를 들어 2번과 5번이 결석을 했으면, 결석한 학생들은 넘어가고 다른 사람들은 지속적으로 책을 읽게 해주는 역할이다.
# no_book = [7] # 책을 안 가져온 친구 7번
# for student in range(1,10): # 2번과 5번은 결석을 했으니 스킵하고 책을 읽어라 이 말임.
#     if student in absent:
#         continue # continue를 만나면 다음 반복문을 실행함
#     elif student in no_book:
#         print('오늘 수업은 여기까지. {0}번은 교무실로 따라와라.'.format(student))
#         break # 하지만 break를 만나면 뒤에 반복값이 더 있든 없든 관계없이 반복값을 탈출함.
#     print('{0} 책 읽어라'.format(student))


## ------------한 줄로 끝내는 for문 활용법--------------------
## 출석번호가 1,2,3,4 인 학교에서 정책이 바뀌어서 앞에 100을 붙여 101,102,103으로 하기로함.
# student = list(range(1,6))
# students = [i+100 for i in student] # student 리스트에 있는 i들을 하나씩 불러오면서 그 i에 100을 더해라, 한 마디로 for문의 조건을 앞에 써준거임)
# print(students)

## 학생의 이름을 길이로 변환

# student = ['iron man', 'thor','hulks']
# students = [len(i) for i in student]
# print(students)

## 학생이름을 대문자로 바꾸기 (대문자 = upper)
# student = ['iron man', 'thor','hulks']
# students = [i.upper() for i in student]
# print(students)


### ----------------------퀴즈----------
## 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
## 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

## 조건 1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
## 조건 2: 당신은 소요 시간 5분~ 15분 사이의 승객만 매칭해야 합니다.

## ( 출력문 예제)

# [0] 1번째 손님(소요시간:15분) 0 => 선택이 됨.
# [] 2번째 손님 (소요시간: 50분) => 소요시간이 50분이라서 대괄호 안이 비어있음.
# [0] 3번째 손님(소요시간: 5분)
# ...
# [] 50번째 손님(소요시간: 16분)

# 총 탑승 승객: 2분

from random import *

cnt = 0 # 총 탑승 승객 수

for i in range(1,51):
    time = randrange(5, 50) # 5분에서 50분 사이의 소요 시간 정보
    if 5 <= time <= 15: # 5분에서 15분 사이의 손님 매칭이 성공한 경우
        print('[o] {0}번째 손님(소요시간:{1}분)'.format(i,time))
        cnt +=1 # 매칭이 된 경우에는 cnt가 올라감.

    else: # 이 때는 매칭이 실패한 경우임. 그러므로 cnt값이 증가가 안함.
        print('[] {0}번째 손님(소요시간:{1}분)'.format(i, time))

print('총 탑승 승객: {0}분'.format(cnt))








