word = input()
arr = list(word)

while len(arr) > 1:
    idx = int(input())
    if idx >= len(arr):
        idx = -1
    arr.pop(idx)
    print(''.join(arr))