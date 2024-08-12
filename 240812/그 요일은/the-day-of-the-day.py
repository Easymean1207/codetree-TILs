# 2024년 m1월 d1일이 월요일이었다면
# 2024년 m2월 d2일까지 A요일은 몇 번 등장하는 지?
# 2024년은 윤년임
import datetime

def calcaulateCountOfDay(base_date, target_date, target_day):
    day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    day_count = 0
    target_idx = day_of_week.index(target_day)

    # m1월 d1일은 월요일
    base_day = 0

    # 날짜 차이 계산
    differ_day = (target_date - base_date).days

    # 주와 일로 구별
    elapsed_week = differ_day // 7
    elapsed_last = differ_day % 7

    # 마지막 1주에서 이미 target 요일이거나 지난 경우
    if target_idx <= elapsed_last:
        day_count = elapsed_week + 1
    else:
        day_count = elapsed_week
    
    return day_count
    

m1, d1, m2, d2 = list(map(int, input().split()))
A = input()

base_date = datetime.date(2024, m1, d1)
target_date = datetime.date(2024,m2,d2)

count = calcaulateCountOfDay(base_date, target_date,A)
print(count)