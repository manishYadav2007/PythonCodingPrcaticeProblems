

# first apprich to solve this question 

# student_name = input("Enter the student name: ").split()
# student_id = input("Enter the student id: ").split()

# student_info = list(zip(student_name, student_id))
# print(student_info)

# student_info.sort()
# print(student_info)


# for name, student in student_info:
#     print(name,student)


# second approch 

student_name = input("Enter the student name: ").split()

student_id = input("Enter the student id: ").split()


student_info  = []

for info in range(len(student_name)):
    pair = [student_name[info], student_id[info]]
    student_info.append(pair)
    
print(student_info)

for name, id_value in student_info:
    print(name, id_value)


