string  = input("Enter the string: ");

len_of_str = len(string)

for i in range(1, len_of_str + 1):
    index = int(input("Enter the indexes: "))
    
    if 0 <= index < len_of_str:
        print(string[index])