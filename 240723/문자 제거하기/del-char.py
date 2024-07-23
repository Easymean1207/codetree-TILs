word = input()
arr = list(word)

for _ in range(len(arr)-1):
    idx = int(input())
    if idx > len(arr):
        idx = -1
    arr.pop(idx)
    print(''.join(arr))