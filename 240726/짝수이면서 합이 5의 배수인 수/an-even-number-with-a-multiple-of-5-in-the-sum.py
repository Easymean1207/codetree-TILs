# n: 10 ~ 99
def is_magic_number(n):
    digit_sum = sum([int(i) for i in str(n)])
    
    return n % 2 == 0 and digit_sum % 5 == 0

def print_yes_no(condition):
    print('Yes') if condition else print('No')

n = int(input())

print_yes_no(is_magic_number(n))