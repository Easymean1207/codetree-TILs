def recursiveFlower(n):
    if n == 0:
        return
    
    print(n, end = ' ')
    recursiveFlower(n-1)
    print(n, end = ' ')

n = int(input())

recursiveFlower(n)