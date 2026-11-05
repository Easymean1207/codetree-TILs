import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
maxSum = -sys.maxsize

for i in range(n-k+1):
    currentSum = 0
    for j in range(i, i+k):
        currentSum += arr[j]

    maxSum = max(currentSum, maxSum)

print(maxSum)