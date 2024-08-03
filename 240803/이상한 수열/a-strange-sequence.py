def weirdSequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    # F(n) = F(n//3) +f(n-1)
    return weirdSequence(n//3) + weirdSequence(n-1)

N = int(input())

print(weirdSequence(N))