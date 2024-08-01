def recursiveEvenOdd(n):
    if n == 1 or n == 2:
        return n

    if n %2 == 0:
        return recursiveEvenOdd(n-2) + n
    else:
        return recursiveEvenOdd(n-2) + n
    

N = int(input())

print(recursiveEvenOdd(N))