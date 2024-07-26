import math

# 소수인지 판별하는 함수
def isPrime(n):
    # 모든 수를 True라고 가정
    sieve = [True for _ in range(n+1)]
    
    # 0, 1 제외
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        # i가 소수인경우
        if sieve[i] == True:
            j = 2
            # i의 배수들을 모두 지움
            while i * j <= n:
                sieve[i*j] = False
                j+=1
    
    return sieve[n]

# 자리수의 합이 짝수인지 확인하는 함수
def isdigitSumEven(n):
    digit_sum = sum([int(i) for i in str(n)])
    
    if digit_sum %2 == 0:
        return True
    else:
        return False

# 범위 내의 조건을 만족하는 숫자의 개수를 세는 함수
def cntNumbers(a, b):
    cnt = 0

    for num in range(a, b+1):
        if isPrime(num) and isdigitSumEven(num):
            cnt += 1

    return cnt


a, b = tuple(map(int, input().split()))

result = cntNumbers(a, b)
print(result)