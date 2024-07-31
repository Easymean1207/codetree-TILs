def recursiveStar(n):
    if n == 0:
        return
    
    print('* '*n)
    recursiveStar(n-1)
    print('* '*n)

n = int(input())

recursiveStar(n)