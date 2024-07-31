def recursiveStar(n):
    if n == 0:
        return
    
    recursiveStar(n-1)
    print('*' * n)


n = int(input())
recursiveStar(n)