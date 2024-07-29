def isContinuousSub(main, target):
    main, target = str(main), str(target)

    if main.find(target) != -1:
        return True
    else:
        return False

n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = isContinuousSub(A,B)

print('Yes' if result == True else 'No')