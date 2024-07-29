''' 
    날짜가 존재하면 계절을 반환, 
    존재하지 않으면 -1을 반환 
'''
def isDateExist(year, month, day):
    day_31 = [1,3,5,7,8,10,12]
    day_30 = [4,6,9,11]

    # 유효하지 않는 달 제외
    if month < 1 or month > 12:
        return -1

    # 30일까지 있는 달에 속함
    if month in day_31 and day <= 31:
        return decideSeason(month)

    # 30일까지 있는 달에 속함
    elif month in day_30 and day <= 30:
        return decideSeason(month)

    # 2월 케이스
    elif month == 2:
        # 윤년과는 관계없는 경우
        if day <= 28:
            return decideSeason(month)
        # 윤년 경우 처리(2월 29일인데 윤년)
        elif day == 29 and isLeapYear(year):
            return decideSeason(month)
        else:
            return -1

    else:
        return -1

''' 
    계절 결정 함수
    계절에 따라 다른 정수 값(1,2,3,4,-1) 반환
'''
def decideSeason(month):
    # 계절이 봄인 경우
    if month >= 3 and month <= 5:
        return 1
    
    # 계절이 여름인 경우
    elif month >= 6 and month <= 8:
        return 2
    
    # 계절이 가을인 경우
    elif month >= 9 and month <= 11:
        return 3

    # 계절이 겨울인 경우
    elif month == 12 or month == 1 or month == 2:
        return 4

    else:
        return -1


'''
    윤년 판별 함수 
'''
def isLeapYear(year):
    if year % 4 == 0 and year % 100 !=0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False 


Y,M,D = tuple(map(int, input().split()))

result = isDateExist(Y, M, D)

if result == 1:
    print('Spring')
elif result == 2:
    print('Summer')
elif result == 3:
    print('Fall')
elif result == 4:
    print('Winter')
else:
    print('-1')