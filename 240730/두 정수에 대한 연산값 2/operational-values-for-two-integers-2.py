def magicBox(a, b):
    if a > b:
        a *=2
        b +=10
    else:
        b *=2
        a +=10

    return a, b

a, b = tuple(map(int, input().split()))
# a, b = magicBox(a,b)
# print(a,b)
print(*magicBox(a,b))