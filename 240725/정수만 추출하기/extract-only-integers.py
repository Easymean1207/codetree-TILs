def abstractNum(input_str):
    sub_str = ''

    for char in input_str:
        if char.isdigit():
            sub_str += char
        else:
            break
    
    return int(sub_str) if sub_str else 0
            

string1, string2 = input().split()
result_1, result_2 = abstractNum(string1), abstractNum(string2)
print(result_1 + result_2)