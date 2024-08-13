def changeAToB(src_digit, dest_digit, given_num):
    # src_digit -> 10진수
    middle = aToDecimal(src_digit, given_num)
    
    # 10진수 -> dest_digit
    result = decimalToB(dest_digit,middle)

    return result


# given_num을 10진수로 변환하는 함수
def aToDecimal(src_digit, given_num):
    decimal = 0
    given_num = str(given_num)

    for i in range(len(given_num)):
        decimal = decimal * src_digit + int(given_num[i])

    return decimal

# 10진수로 변환된 given_num을 dest_digit진법으로 변환하는 함수
def decimalToB(dest_digit,given_num):
    if given_num < dest_digit:
        return str(given_num)
    else:
        return decimalToB(dest_digit, given_num // dest_digit) + str(given_num % dest_digit)

a, b = tuple(map(int, input().split()))
n = int(input())

print(changeAToB(a,b,n))