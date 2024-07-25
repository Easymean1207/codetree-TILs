def eraseAlphabet(input_str):
    for char in input_str:
        if char.isalpha():
            input_str = input_str.replace(char,'')
    
    return int(input_str)

str_1 = input()
str_2 = input()

str_1 = eraseAlphabet(str_1)
str_2 = eraseAlphabet(str_2)

print(str_1 + str_2)