string = input("Enter string:")
vowels = "AEIOUaeiouАОУЕЄЮЯЇІИаоуіїюяєи"
vowels_string = ""
for char in string:
    if char in vowels:
        vowels_string += char
print("Vowels char in string:",vowels_string)
