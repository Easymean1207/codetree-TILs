# 2로 나누어떨어지는 확인하는 함수
def divideBy2(n):
    if n % 2 == 0:
        return True

# 일의 자리가 5인지 확인하는 함수
def checkLastDigit(n):
    n = str(n)
    if n[-1] == '5':
        return True

# 3으로 나누어지지만 9로는 나누어지지 않는 지 확인하는 함수
def divideBy3Not9(n):
    if n % 3 == 0 and n % 9 !=0:
        return True

# 해당 수가 온전수인지 확인하는 함수
def checkOnjeonsu(n):
    if divideBy2(n) or checkLastDigit(n) or divideBy3Not9(n):
        return False
    else:
        return True

# 범위 내의 온전수를 찾아내는 함수
def findOnjeonsu(a, b):
    cnt = 0

    for num in range(a, b+1):
        if checkOnjeonsu(num):
            cnt += 1
    
    return cnt

a, b = map(int, input().split())

result = findOnjeonsu(a, b)
print(result)