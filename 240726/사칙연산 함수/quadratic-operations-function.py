def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        a // b
    except ZeroDivisionError as e:
        return e

    return a / b

def chooseOperation(a, b , operator = ''):
    result = 0

    if operator == '+':
        result = plus(a,b)
    elif operator == '-':
        result = minus(a,b)
    elif operator == '*':
        result = multiply(a,b)
    elif operator == '/':
        result = divide(a,b)
    else:
        return False
    
    return result


a, o ,c = input().split()
a, c = int(a), int(c)
result = chooseOperation(a,c,o)

print(f'{a} {o} {c} = {result}')