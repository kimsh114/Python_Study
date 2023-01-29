### -------------표준 입출력----------------
# print('python', 'java') # 단순히 이렇게 쓰면 파이썬 띄고 자바 이렇게 나온다.
# print('python','java',sep= ' vs ') # sep를 사용하면 파이썬과 자바 사이에 무엇이 들어갈 것인지 정의 해줄 수 있다.
# print('python', 'java', sep = ',', end='? ') # 이 end를 쓰면 이 뒤의 명령문도 한줄에 실행할 수 있다.
# print('무엇이 더 재미있을까요?')

# import sys
# print('python', 'java', file= sys.stdout) # stdout => 표준 출력으로 문장이 찍힘
# print('python', 'java', file= sys.stderr) # stderr => 표준 에러로 문장이 찍힘 # 우리가 필요하면 따로 에러 처리를 해줌

## 시험성적
# scores = {'수학':0, '영어': 50, '코딩': 100}
# for subject, score in scores.items(): # 딕셔너리에서 .items() 를 사용하면은 키와 벨류의 쌍으로 나옴
#     print(subject.ljust(8),str(score).rjust(4), sep=':') # .ljust(8) => 8칸을 확보하고 왼쪽으로 정렬을 해라, rjust(4) => 4칸을 확보하고 오른쪽 정렬을 해라

## 은행 대기순번표( 001,002,003)
# for num in range(1,21):
#     print('대기번호'.ljust(5),  str(num).zfill(3),sep= ':') # .zfill(3) => 3개만큼의 크기를 차지하고 값을 채워 넣는데 값이 없는 빈공간에는 0으로 채워달라


### ----------------다양한 출력 포멧-----------------
## 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print('{0: >10}'.format(500)) # : 다음 공백 하나가 빈 자리는 빈 공간으로 두는 것, 그 다음 '>'이 오른쪽 정렬을 의미함, 그 다음 10이 10자리를 확보

## 양수일 때는 +로 표시, 음수일 때는 -로 표시하는 예제
# print('{0: >+10}'.format(500))
# print('{0: >+10}'.format(-500)) # '>' 옆 '+'는 음수이면 -로 표시되고 양수 이면 +로 표시가 됨.

## 왼쪽 정렬을 하고 빈칸을 밑줄로 채움
# print('{0:_<+10}'.format(500))

## 큰 숫자가 왔을 때 3자리 마다 콤마를 찍는 예제
# print('{0:,}'.format(10000000))

## 3자리마다 콤마를 찍어주는데 +-부호도 찍기
# print('{0:+,}'.format(1000000)) # 콤마 앞에 플러스를 적어주면 된다.

## 3자리마다 콤마를 찍어주는데 부호도 붙여주고 자리수까지 확보하기 + 빈자리는 ^로 채우기
# print('{0:^<+30,}'.format(1000000)) # 기억해야 할 것은 콜론 다음은 채우기 기능이라는거

## 소수점을 출력하는 방법
# print('{0:f}'.format(5/3))

## 소수점을 특정 자리 수까지만 표시하는 방법(소수점 세 번째 자리에서 반올림을 해서 나온다.)
# print('{0:.2f}'.format(5/3))



###---------------파일 입출력-----------------
# 파일을 만들 수 있다.
# score_file = open('score.txt','w', encoding='utf8') # 첫 번째는 파일의 이름, 두 번째는 쓰기 위한 용도, 세 번째는 인코딩
# print('수학 : 0', file=score_file)
# print('영어 : 0', file=score_file)
# score_file.close() # 파일을 열어줬으면 항상 닫아줘야 한다.



# score_file = open('score.txt','a', encoding='utf8') # a는 이미 있는 파일에 추가해서 적고 싶은 것이다.
# score_file.write('과학: 80')
# score_file.write('\n국어: 100')
# score_file.close()

## 파일의 내용을 읽어오는 방법

# score_file = open('score.txt', 'r', encoding= 'utf8') # r은 파일을 읽어오는 것이다.
# print(score_file.read()) #  score_file.read는 파일의 내용을 전부 다 읽는 것이다.
# score_file.close()

# score_file = open('score.txt', 'r', encoding= 'utf8') # 이번에는 파일 내용 전부를 읽어오는 것이 아닌 한 줄 한 줄 필요한 것만 읽어오는 것
# print(score_file.readline(),end='') # 한 줄을 읽고 커서는 다음 줄로 이동 , end='' => 줄바꿈을 안하기 위함.
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

## 파일이 몇 줄인지 모를 경우 처리하는 방법
# score_file = open('score.txt', 'r', encoding= 'utf8')

# while True: # 무한루프를 이용하는 방법
#     line = score_file.readline() # 라인을 한 줄씩 읽어 내려감.(무한루프로)
#     if not line:# 만약 라인이 없으면은 break
#         break
#     print(line, end= '') # 라인이 있으면 그냥 출력함.
# score_file.close()



#
# lines = score_file.readlines() # readlines를 하면 모든 파일의 내용을 리스트 형태로 저장을 한다.
#
# for line in lines:
#     print(line, end='')
#     # 스코어 파일의 자료를 리스트 형태로 넣고, 리스트에서 한 줄씩 출력이 되게끔한다.
# score_file.close()


### ---------------pickle---------------------------
## pickle은 프로그램 상에서 사용하고 있는 데이터를 파일의 형태로 저장을 해주는 것이다.
# import pickle
#
# profile_file = open('profile.pickle', 'wb') # 피클을 쓰기 위해서는 항상 바이너리 타입을 정의를 해야한다. wb는 write binary이다.
# # 피클은 따로 인코딩을 설정해줄 필요는 없다.
# profile = {'name': 'kim', 'age': '28', 'hobby':['baseball', 'balling', 'coding']}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장하는 과정
# profile_file.close()

## pickle을 이용해서 불러오기
# profile_file = open('profile.pickle.txt', 'rb')
# profile = pickle.load(profile_file) # 파일에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

### -------------with------------------
## with를 쓰면 조금 더 편하게 위의 작업을 할 수 있다.

# import pickle
# with open('profile.pickle','rb') as profile_file: # profile.pickle 파일을 열어서 profile_file이라는 변수로 저장을 함.
#     print(pickle.load(profile_file))  # 위의 파일 내용을 pickle.load로 불러옴.
#     # with문은 close를 할 필요가 없다.

#
# with open('study.txt','w', encoding='utf8') as study_file: # with문을 활용해 파일을 적는 법
#     study_file.write('파이썬을 열심히 공부하고 있어요')

# with open('study.txt', 'r', encoding='utf8') as study_file:
#     print(study_file.read()) # 모든 내용을 읽어옴.



###--------------퀴즈----------------
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x주차 주간보고 -
# 부서:
# 이름:
# 업무 요악:

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시요

# 조건: 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.


for i in range(1,51):
    with open(str(i)+'주차.txt', 'w', encoding='utf8') as report_file:
        report_file.write("- {0}주차 주간보고 -\n부서:\n이름:\n업무 요약:".format(i))



