def changeToAbs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    
    for elem in arr:
        print(elem, end = ' ')
    # print(*arr)


N = int(input())
arr = list(map(int, input().split()))

changeToAbs(arr)