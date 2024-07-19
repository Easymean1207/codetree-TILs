string_A = input()
string_B = input()

concated_1 = string_A + string_B
concated_2 = string_B + string_A

print('true') if concated_1 == concated_2 else print('false')