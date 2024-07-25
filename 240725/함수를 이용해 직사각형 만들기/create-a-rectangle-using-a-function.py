def makeRectangle(length,width):
    for _ in range(length):
        print('1' * width)

n, m = map(int, input().split())

makeRectangle(n, m)