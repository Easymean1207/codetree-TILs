def find_minimum(n1,n2,n3):
    return min(n1,n2,n3)

a, b, c = tuple(map(int, input().split()))

print(find_minimum(a,b,c))