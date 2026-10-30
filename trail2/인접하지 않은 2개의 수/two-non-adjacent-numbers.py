n = int(input())
numbers = list(map(int, input().split()))

maxSum = 0

# Please write your code here.
for i in range(n):
    for j in range(i+2, n):
        maxSum = max(maxSum, numbers[i] + numbers[j])

print(maxSum)