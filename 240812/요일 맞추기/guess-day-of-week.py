# 2011년 m1월 d1일이 월요일이라고 가정할 때
# 2011년 m1월 d2일이 무슨 요일인가?
import datetime

def calculateDay(base_date, target_date):
    day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    
    # m1월 d1일을 월요일로 설정
    base_day = 0 

    # 두 날짜의 차이를 계산
    differ_day = (target_date - base_date).days
    
    # 날짜 차이를 요일에 대입하기 위한 값
    target_day = (base_day + differ_day) % 7

    return day_of_week[target_day]

m1, d1, m2, d2 = list(map(int, input().split()))

base_date = datetime.date(2011, m1, d1)
target_date = datetime.date(2011, m2, d2)

day_of_target_date = calculateDay(base_date, target_date)
print(day_of_target_date)