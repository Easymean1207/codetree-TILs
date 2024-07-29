def isDateExist(month, day):
    day_31 = [1,3,5,7,8,10,12]
    day_30 = [4,6,9,11]

    # 31일까지 있는 달 확인
    if month in day_31 and day <= 31:
        return True
    
    # 30일까지 있는 달 확인
    elif month in day and day <= 30:
        return True
    
    # 2월 확인
    elif month == 2 and day <= 28:
        return True

    # 존재하지 않는 날짜 처리
    else:
        return False


M,D = tuple(map(int, input().split()))

result = isDateExist(M, D)

print('Yes') if isDateExist else print('No')