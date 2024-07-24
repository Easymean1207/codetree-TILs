string_A = input()

sum_result = 0

for char in string_A:
    if char.isdigit():
        # print(type(char))
        sum_result += int(char)
    
print(sum_result)