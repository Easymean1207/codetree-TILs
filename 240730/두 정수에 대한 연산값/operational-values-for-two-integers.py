def function(a, b):
    if a > b:
        a += 25
        b *= 2
    elif a < b:
        a *= 2
        b += 25

    print(a, b)


a, b = tuple(map(int, input().split()))

function(a, b)