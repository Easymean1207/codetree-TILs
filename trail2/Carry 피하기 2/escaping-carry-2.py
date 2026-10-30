n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
notCarryMax = -1

def isCarry(a, b, c):
    while a > 0 or b > 0 or c > 0:
        if a % 10 + b % 10 + c % 10 >= 10:
            return True

        a //= 10
        b //= 10
        c //= 10

    return False

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not isCarry(arr[i], arr[j], arr[k]):
                notCarryMax = max(notCarryMax, arr[i]+arr[j]+arr[k])

print(notCarryMax)
    