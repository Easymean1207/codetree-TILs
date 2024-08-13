def decimalToBinary(num):
    binary = []
    
    while True:
        if num < 2:
            binary.append(str(num))
            break
    
        binary.append(str(num%2))
        num //=2

    binary.reverse()
    binary = ''.join(binary)

    return binary

def decimalToBinary2(num):
    if num < 2:
        return str(num)
    else:
        return decimalToBinary2(num // 2) + str(num % 2)

n = int(input())

result = decimalToBinary(n)
# result = decimalToBinary2(n)

print(result)