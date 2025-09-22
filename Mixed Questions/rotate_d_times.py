# list_num = list(map(int, input("Enter the list items: ").split(',')))
# f = int(input("Enter the rotation frequency: "))

# length = len(list_num)

# rotation_frequency = f  % length




# rotation_part = list_num[:rotation_frequency]

# remaining_part = list_num[rotation_frequency:]

# remaining_part.extend(rotation_part)
# print(remaining_part)












array  =   [1, 2, 3, 4, 5]
frequency = 2


rotate_times = frequency % len(array)


first_part = array[:rotate_times]
second_part = array[rotate_times:]

second_part.extend(first_part)
print(second_part)
















































