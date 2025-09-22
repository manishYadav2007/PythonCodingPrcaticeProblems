alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
}



keys_input = input("Enter the keys: ").split()

copy_dict = alphabets.copy()

print(alphabets)
for each_key in keys_input:
    if each_key in copy_dict:
        del copy_dict[each_key]
print(copy_dict)