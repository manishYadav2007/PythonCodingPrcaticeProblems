
class Student:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.grades = []



    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return None  
        
        if self.grades:
            return sum(self.grades) / len(self.grades)
    

    def get_student_info(self):
        average_grade = self.get_average_grade()

        if average_grade is None:
            return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, City: {self.city}, Average Grade: N/A"
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, City: {self.city}, Average Grade: {average_grade}"






def main():
    first_name = 'Alice'
    last_name = 'Johnson'
    age = 22
    city = "Seattle"
    # grades = [] 
    grades = [90, 85, 80] 

    student = Student(first_name, last_name, age, city)

    for grade in grades:
        student.add_grade(grade)

    print(student.get_student_info())

main()
