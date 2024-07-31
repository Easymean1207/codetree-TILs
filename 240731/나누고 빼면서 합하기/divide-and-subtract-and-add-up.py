# 수열 A (n개의 원소)
# 숫자 m

def magicFunction(sequence, m):
    output = sequence[m-1]

    for i in range(len(sequence)):
        while m > 1:
            if m%2 == 1:
                m -=1
            else:
                m //=2
            output += sequence[m-1]

    return output

n, m = tuple(map(int, input().split()))
A = list(map(int, input().split()))

print(magicFunction(A,m))