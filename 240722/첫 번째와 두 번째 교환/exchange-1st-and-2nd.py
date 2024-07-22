s = input()

arr = list(s)

char1 = arr[0]
char2 = arr[1]

for i,elem in enumerate(arr):
    if elem == char1:
        arr[i] = char2
    elif elem == char2:
        arr[i] = char1

print(''.join(arr))