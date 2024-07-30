def swap(a,b):
    a,b = b,a
    return a, b

n, m = tuple(map(int, input().split()))

n, m = swap(n,m)
print(n, m)