string = input()

for char in string:
    if char.isdigit():
        print(char, end = '')
    elif char.isalpha():
        print(char.lower(), end = '')