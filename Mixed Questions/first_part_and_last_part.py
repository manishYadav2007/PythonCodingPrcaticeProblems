string = input("Enter the string: ")
sub_string = input("Enter the substring: ")


if string.startswith(sub_string) or string.endswith(sub_string):
    print(True)
else:
    print(False)
