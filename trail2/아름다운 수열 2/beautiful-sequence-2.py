N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
beautifulCount = 0

for i in range(N-M+1): # 시작점
    current = []
    
    for j in range(i, i+M): # 길이가 M인 수열
        current.append(A[j])
    
    if(sorted(current) == sorted(B)):
        beautifulCount+=1

print(beautifulCount)