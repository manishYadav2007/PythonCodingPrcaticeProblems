






string  = list(input("Enter the string: "))


letters_only  = "".join(char for char in string if char.isalpha()).lower()

if letters_only == letters_only[::-1]:
    print(1)
else:
    print(0)
    
    
    

    
    
    






