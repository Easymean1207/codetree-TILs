def binaryToDecimal(binary):
    decimal = 0
    
    for i in range(len(binary)):
        decimal = decimal * 2 + int(binary[i])

    return decimal


given_binary = input()

print(binaryToDecimal(given_binary))