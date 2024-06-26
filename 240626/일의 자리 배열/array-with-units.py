a, b = map(int, input().split())

fibonacci = [a, b]
n = 10

for i in range(2,n):
    next_value = fibonacci[i-2] + fibonacci[i-1]
    next_value = next_value % 10
    fibonacci.append(next_value)
    
print(*fibonacci)