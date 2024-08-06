def isSame(str1, str2):
    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))

    if sorted_str1 == sorted_str2:
        print('Yes')
    else:
        print('No')

str1 = input()
str2 = input()

isSame(str1, str2)