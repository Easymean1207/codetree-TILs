A = input()
B = input()

cnt = 0

for _ in range(len(A)):
    # right-shift 1번
    A = A[-1] + A[0:-1]
    cnt+=1

    # 해당 shift에서 일치하는 경우
    if A == B:
        break
    
    # 모든 shift 경우에서 일치하지 않는 경우
    if cnt == len(A):
        cnt = -1
        
print(cnt)