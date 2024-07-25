n, A = input().split()

n = int(n)
cnt = 0

for _ in range(n):
    input_str = input()

    if A == input_str:
        cnt += 1

print(cnt)