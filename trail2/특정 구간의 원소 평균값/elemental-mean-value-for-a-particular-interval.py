n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
count = 0

for i in range(len(arr)): # 시작점
    for j in range(i, n): # 끝점
        total = 0
        for k in range(i, j+1): # 범위
            total += arr[k]

        average = total / (j-i+1)
        
        if average in arr[i:j+1]:
            count+=1

print(count)

