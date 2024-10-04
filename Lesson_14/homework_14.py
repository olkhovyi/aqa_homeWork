class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    # Method for changing the average score
    def change_average_grade(self, new_grade):
        self.average_grade = new_grade
        print(f"Average score changed to: {self.average_grade}")

    # A method for outputting information about a student
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Average grade: {self.average_grade}")


student = Student("Alex", "Jons", 18, 3.5)
print("Information about the student:")
student.display_info()

# A change in the student's average score
student.change_average_grade(4.8)


print("\nUpdated information about the student:")
student.display_info()
