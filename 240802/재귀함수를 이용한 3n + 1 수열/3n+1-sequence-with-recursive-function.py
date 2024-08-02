def recursive3n1(n, cnt),:
    if n == 1:
        return 

    if n %2 == 0:
        n /=2
    else:
        n = 3*n + 1

    cnt +=1

    return recursive3n1(n, cnt)

n = int(input())

print(recursive3n1(n, 0))