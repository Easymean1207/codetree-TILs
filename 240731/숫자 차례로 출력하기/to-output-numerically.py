def recursive(n):
    if n == 0:
        return
    
    recursive(n-1)
    print(n, end = ' ')


def recursiveReverse(n):
    if n == 0:
        return
    
    print(n, end = ' ')
    recursiveReverse(n-1)

n = int(input())

recursive(n)
print()
recursiveReverse(n)