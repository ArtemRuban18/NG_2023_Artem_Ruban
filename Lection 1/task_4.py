import math
def calculate(a,b,operator):
    match operator:
        case '+':
            res = a+b
        case '-':
            res = a-b
        case '*':
            res = a*b
        case '/':
            res = a/b
        case '**':
            res = pow(a,b)
    return res
        
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = str(input("Enter operation: "))
result = calculate(a,b,operator)
print(f"{a} {operator} {b} = {result}")
        