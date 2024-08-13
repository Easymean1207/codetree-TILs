def NumToQuaternary(num):
    if num < 4:
        return str(num)
    else:
        return NumToQuaternary(num // 4) + str(num % 4)


def NumToOcta(num):
    if num < 8:
        return str(num)
    else:
        return NumToOcta(num // 8) + str(num % 8)


N, B = list(map(int, input().split())) 

if B == 4:
    result = NumToQuaternary(N)
elif B == 8:
    result = NumToOcta(N)

print(result)