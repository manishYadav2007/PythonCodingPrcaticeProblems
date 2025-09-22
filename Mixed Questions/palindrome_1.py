string = input("Enter the string: ")
string = string.lower()
reversed_str = string[::-1]

if reversed_str == string:
    print("Palindrome")
else:
    print("Not a Plaindrome")
    