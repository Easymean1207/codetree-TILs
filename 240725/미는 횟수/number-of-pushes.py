A = input()
B = input()

cnt = 0

for _ in range(len(A)-1):
    # right-shift 1번
    A = A[-1] + A[0:-1]
    cnt+=1

    if A == B:
        break

print(cnt)