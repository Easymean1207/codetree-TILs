def recursiveFibonacci(n):
    if n == 1 or n==2:
        return 1
    
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)


N = int(input())

print(recursiveFibonacci(N))