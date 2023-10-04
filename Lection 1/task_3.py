# F - Fahrenheit
# C - Celsius
temp = str(input("What units do you want the temperature in (F/C) ?: "))
if temp == 'F' or temp == 'f':
    temp_in_cels = float(input("Enter the temperature in Fahrenheit : "))
    print(f"{temp_in_cels} F = {(temp_in_cels*5/9)-32:.1f} C")
if temp == 'C' or temp == 'c':
    temp_in_fahr = float(input("Enter the temperature in Celsius : "))
    print(f"{temp_in_fahr} C = {(temp_in_fahr*9/5) + 32:.1f} F ")
else:
    print("Error. Enter 'F' or 'C'! ")