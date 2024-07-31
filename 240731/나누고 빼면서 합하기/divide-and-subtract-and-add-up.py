# 수열 A (n개의 원소)
# 숫자 m

def magicFunction(sequence, m):
    output = 0

    for i in range(len(sequence)):
        while m > 1:
            if m%2 == 1:
                m -=1
            else:
                m //=2
            output += sequence[m]
    
    return output

n, m = tuple(map(int, input().split()))
A = list(map(int, input().split()))