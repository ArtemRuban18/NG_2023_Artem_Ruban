lst = input("enter ")
lst = lst.split()
numbers = 0
for element in lst:
    try:   #Спроба перетворити елемент масиву на число
        float(element)
        numbers +=1
    except ValueError: #Помилка при перетворенні
        pass
print(f"Quantity of numbers in massive: {numbers}")
    