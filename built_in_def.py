### 내장함수는 파이썬 내부에 내장되어 있는 함수이기때문에 import할 필요가 없다

# input => 사용자 입력을 받는 함수
#dir => 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시하는 것
# 등등

### -------------------외장함수------------------------
## import 를 해야하는 함수들
## time 함수

# import time
# print(time.strftime('%y-%m-%d %H:%M:%S'))

import datetime
# print('오늘 날짜는, ', datetime.date.today())

## timedelta : 두 날짜 사이의 간격을 알려줌

today = datetime.date.today()
td = datetime.timedelta(days=100)
print('우리가 만난지 100일은', today + td)