s1, s2 = input().split()

arr1 = list(s1)
arr2 = list(s2)

arr2[0] = arr1[0]
arr2[1] = arr1[1]

s2 = ''.join(arr2)
print(s2)