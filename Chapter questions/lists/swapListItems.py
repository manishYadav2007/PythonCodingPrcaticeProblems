list_items = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]





index1 = int(input("Enter the index one: "))
index2 = int(input("Enter the index one: "))


temp = list_items[index1]
list_items[index1] = list_items[index2]
list_items[index2] =temp 

print(list_items)



