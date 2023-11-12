import math
def calculator():
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    match input("Avaliable operations : +, -, *, /, **, root. Choose one of them: "):
        case '+':
            res = first_num + second_num
            return f"{first_num} + {second_num} = {res}"
        case '-':
            res = first_num - second_num
            return f"{first_num} - {second_num} = {res}"
        case '*':
            res = first_num * second_num
            return f"{first_num} * {second_num} = {res}"
        case '/':
            if second_num == 0:
                print("Cannot be divided by 0!")
            else:
                res = first_num / second_num
                return f"{first_num} / {second_num} = {res}"
        case '**':
            res = pow(first_num,second_num)
            return f"{first_num} ^{second_num} = {res}"
        case 'root':
            res = pow(first_num,1/second_num)
            return f"{first_num} - {second_num} = {res}"

result = calculator()
print(result)
        