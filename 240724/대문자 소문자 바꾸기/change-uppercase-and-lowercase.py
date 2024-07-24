string = input()

for char in string:
    print(char.lower(), end = '') if char.isupper() else print(char.upper(), end = '')