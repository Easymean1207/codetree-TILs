# 숫자 내에 3, 6, 9가 들어있는 지 확인하는 함수
def threeSixNine(n):
    num = str(n)
    if '3' in num or '6' in num or '9' in num:
        return True
    

# 숫자가 3의 배수인지 판별하는 함수
def multipleOfThree(n):
    digit_sum = sum([int(i) for i in str(n)])
    if digit_sum % 3 == 0:
        return True

def checkAllConditions(a, b):
    cnt = 0

    for num in range(a, b+1):
        if threeSixNine(num) or multipleOfThree(num):
            cnt+=1
            
    return cnt


a, b = tuple(map(int, input().split()))

print(checkAllConditions(a, b))