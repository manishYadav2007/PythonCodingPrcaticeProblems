students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}




num_of_inputs = int(input("Enter the number of inputs: "))


for each_item in range(num_of_inputs):
    key, value = input("Enter the key value pairs: ").split()
    students_dict[key] = value
print(students_dict)


