end_num = int(input("Enter a last number: "))
for num in range(1,end_num+1):
    dividers = [str(divider) for divider in range(1,num +1) if num % divider == 0]
    dividers_string = ", ".join(dividers)
    print(f"{num}     |     {dividers_string}")
    

def simple_num(number):
    if number < 0:
        return False
    for divider in range(2,number):
        if number % divider == 0:
            return False
    return True
    
number = int(input("Enter number: "))
result = simple_num(number)
arrayOfSimpleNumber = [number for number in range(2, number) if simple_num(number)]
if result:
    print(f"{number} is simple number")
    print(f"List of simple number: {arrayOfSimpleNumber}")
else:
    print(f"{number} is not simple number")
