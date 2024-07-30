def hasMoreThanTwo(string):
    cnt = 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            cnt +=1

    if cnt >= 2:
        return True
    else:
        return False

A = input()

result = hasMoreThanTwo(A)

print("Yes") if result else print("No")