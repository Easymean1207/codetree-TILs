def binaryToDecimal(input_binary):
    decimal = 0

    for i in range(len(input_binary)):
        decimal = decimal * 2 + int(input_binary[i])
    
    return decimal

def decimalToBinary(input_decimal):
    if input_decimal < 2:
        return str(input_decimal)
    else:
        return decimalToBinary(input_decimal // 2) + str(input_decimal % 2)


N = input()
changed_N = decimalToBinary((binaryToDecimal(N) * 17))
print(changed_N)