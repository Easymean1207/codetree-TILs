n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
notCarryMax = -1

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            carry = False

            # 일의 자리 carry 확인
            if arr[i]%10 + arr[j]%10 + arr[k]%10 >= 10:
                carry = True
            
            # 십의 자리 carry 확인
            if arr[i] % 100 // 10 + arr[j]%100 // 10 + arr[k]%100 // 10 >= 10:
                carry = True

            # 백의 자리 carry 확인
            if arr[i]%1000 // 100 + arr[j]%1000 // 100 + arr[k]%1000 // 100 >= 10:
                carry = True

            # 천의 자리 carry 확인
            if arr[i]%10000 // 1000 + arr[j]%10000 // 1000 + arr[k]%10000 // 1000 >= 10:
                carry = True

            # carry가 아니라면 최대 비교후 최대값 갱신
            if carry == False:
                notCarryMax = max(notCarryMax, arr[i]+arr[j]+arr[k])

print(notCarryMax)
    