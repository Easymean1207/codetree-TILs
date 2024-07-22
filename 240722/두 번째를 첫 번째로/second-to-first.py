string = input()

# 두 번째 문자 -> 첫 번째 문자
first = string[0]
second = string[1]

for i, char in enumerate(string):
    if char == second:
        string = string.replace(char, first)

print(string)