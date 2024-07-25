def makeSquare(n):
    cnt = 1
    for _ in range(n):
        for i in range(n):
            print(cnt, end = ' ')
            cnt = (cnt+1) % 10
        print()

n = int(input())

makeSquare(n)