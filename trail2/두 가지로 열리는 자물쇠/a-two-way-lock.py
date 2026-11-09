N = int(input())
a1, b1, c1 = map(int, input().split()) # 첫번째 조합
a2, b2, c2 = map(int, input().split()) # 두번째 조합

# Please write your code here.
first = [a1, b1, c1]
second = [a2, b2, c2]

count = 0

def isUnlock(x, y, z):
    # 첫 번째 조합과의 거리 계산
    firstX = min(abs(x - first[0]), N - abs(x - first[0]))
    firstY = min(abs(y - first[1]), N - abs(y - first[1]))
    firstZ = min(abs(z - first[2]), N - abs(z - first[2]))

    # 두 번째 조합과의 거리 계산
    secondX = min(abs(x - second[0]), N - abs(x - second[0]))
    secondY = min(abs(y - second[1]), N - abs(y - second[1]))
    secondZ = min(abs(z - second[2]), N - abs(z - second[2]))

    # 첫 번째 또는 두 번째 조합 중 하나와
    # 세 자리 모두 거리가 2 이하면 열림
    if (firstX <= 2 and firstY <= 2 and firstZ <= 2) or (secondX <= 2 and secondY <= 2 and secondZ <= 2):
        return True


for x in range(1, N+1):
    for y in range(1, N+1):
        for z in range(1, N+1):
            if isUnlock(x, y, z) == True:
                count+=1

print(count)