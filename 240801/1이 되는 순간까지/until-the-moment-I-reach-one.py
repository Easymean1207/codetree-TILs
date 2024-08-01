# N이 짝수 -> 2로 나눈 몫
# N이 홀수 -> 3으로 나눈 몫
# 각 재귀가 끝날 때마다 cnt 하나씩 증가

def recursiveDivide(n, cnt):
    if n == 1:
        return cnt
    
    if n % 2 == 0:
        n /=2
    else:
        n //=3

    cnt +=1
    return recursiveDivide(n, cnt)
    

N = int(input())
print(recursiveDivide(N, 0))