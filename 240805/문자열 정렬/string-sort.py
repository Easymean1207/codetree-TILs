def stringSort(input_str):
    sorted_str = sorted(input_str)
    sorted_str = ''.join(sorted_str)
    
    return sorted_str


string = input()

print(stringSort(string))