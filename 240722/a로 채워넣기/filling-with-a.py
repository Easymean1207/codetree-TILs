s = input()

arr = list(s)

arr[1] = 'a'
arr[-2] = 'a'

s = ''.join(arr)
print(s)