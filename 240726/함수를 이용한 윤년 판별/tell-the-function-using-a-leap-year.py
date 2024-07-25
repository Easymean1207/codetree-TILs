# 윤년(leap year)인지 아닌 지 판별하는 함수
def isLeapYear(year):
    if year % 4 != 0:
        return False
    
    if year % 100 == 0 and year % 400 != 0:
        return False
    
    return True

input_year = int(input())

print('true') if isLeapYear(input_year) else print('false')