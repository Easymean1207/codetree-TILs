# 문자열 B의 길이는 항상 2
A = input()
B = input()

# B가 A의 부분 문자열로써 등장하는 횟수
cnt = 0

for i in range(len(A)-1):
    if A[i] == B[0] and A[i+1] == B[1]:
        cnt+=1

print(cnt)