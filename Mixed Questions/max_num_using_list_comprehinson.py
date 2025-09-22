numbers = [10, 25, 7, 88, 42]

max_num = [num for num in numbers if all(num >= other for other in numbers)][0]
print(max_num)