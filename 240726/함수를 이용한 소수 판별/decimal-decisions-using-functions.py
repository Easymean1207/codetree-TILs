import math

# 에라토스테네스의 체
def eratosthenes(n):
    # 모든 수를 일단 True로 가정
    sieve = [True for _ in range(n+1)]
    # 0, 1 제외
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        # i가 소수인 경우
        if sieve[i] == True:
            j = 2
            # i의 배수들을 모두 지움
            while i * j <= n:
                sieve[i * j] = False
                j+=1
    
    return sieve


def sumOfPrimes(a,b):
    sieve = eratosthenes(b)

    # 범위에 해당하는 값만을 더하여 return
    return sum(i for i in range(a, b+1) if sieve[i])
         

a,b = tuple(map(int, input().split()))
print(sumOfPrimes(a,b))