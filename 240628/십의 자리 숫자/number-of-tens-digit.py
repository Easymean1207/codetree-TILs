nums = list(map(int,input().split()))
cnt = [0 for _ in range(9)]

for num in nums:
    if num == 0:
        break
    if num >= 10:
        tens_digit = num // 10
        cnt[tens_digit-1] += 1

for i in range(len(cnt)):
    print(f'{i+1} - {cnt[i]}')