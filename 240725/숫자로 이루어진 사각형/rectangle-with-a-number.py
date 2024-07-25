def makeSquare(n):
    cnt = 0

    for _ in range(n):
        for i in range(n):
            cnt = 1 if cnt == 9 else (cnt + 1) % 10
            print(cnt, end = ' ')
        print()


n = int(input())
makeSquare(n)