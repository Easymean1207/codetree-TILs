# 수열 A(n개의 원소)
# m개의 숫자쌍 a1, a2

n, m = tuple(map(int, input().split()))
A = list(map(int, input().split()))

pairs = [
    list(map(int, input().split()))
    for _ in range(m)
]

def adda1Toa2():
    for pair in pairs:
        output = 0
        
        for i in range(pair[0], pair[1]+1):
            output += A[i-1]
        
        print(output)

adda1Toa2()