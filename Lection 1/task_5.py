import math
def square_equation(a,b,c):
    D = b**2 - 4*a*c #Дискримінант

    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
    elif D == 0:
        x1 = -b / 2*a
        x2 = 0
    else:
        print("D can`t be < 0")
    return f"x1 = {x1:.2f}   x2 = {x2:.2f}"
    
    
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if b>=0:
    print(f"Square equation: {a}x^2 + {b}x + {c} = 0")
else:
    print(f"Square equation: {a}x^2 {b}x + {c} = 0")
result = square_equation(a,b,c)
print(result)

