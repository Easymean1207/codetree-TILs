abilities = list(map(int, input().split()))

# Please write your code here.
import sys

minDiff = sys.maxsize

for i in range(len(abilities)):
    for j in range(i+1, len(abilities)):
        for k in range(j+1, len(abilities)):
            sum1 = abilities[i] + abilities[j] + abilities[k]
            sum2 = sum(abilities) - sum1

            minDiff = min(minDiff, abs(sum1 - sum2))

print(minDiff)