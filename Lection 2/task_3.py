end_num = int(input("Enter a last number: "))
for num in range(1,end_num+1):
    dividers = [str(divider) for divider in range(1,num +1) if num % divider == 0]
    dividers_string = ", ".join(dividers)
    print(f"{num}     |     {dividers_string}")

def simple_num(n):
    if n < 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True
n = int(input("Enter a number: "))
if simple_num(n):
    print(f'{n} - natural number')
else:
    print(f'{n} - not natural number')
