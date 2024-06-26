ls = list(map(int, input().split()))
result = 0

for i in range(len(ls)):
    if ls[i] == 0:
        result = ls[i-3] + ls[i-2] + ls[i-1]
        break
        
print(result)