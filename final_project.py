import random
"""ITF 08 Final Project
#TODO 1 Enter your name and submission date
Name :
Delivery Date :
Eng.Mohanad Alkrunz
"""


# TODO 2 Define Course Class and define constructor with (course_id generated ,course name (user_input) and
# course mark
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1, 1000)
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    # TODO 3 define static variable indicates total student count
    total_students = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using random module)
    # student_name (user input)
    # student_age (user_inout)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(1, 1000)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self, course):
        self.courses_list.append(course)

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    # method to get student_average as a value
    def get_student_average(self):
        total_marks = 0
        num_courses = len(self.courses_list)
        if num_courses == 0:
            return 0
        for course in self.courses_list:
            total_marks += course.course_mark
        return total_marks / len(self.courses_list)

# in Global Scope
# TODO 8 declare empty students list
students_list = []

def exit_program():
    print("Exit")
    save_student_data()
    exit()

def save_student_data():
    with open("student_data.txt", "w") as file:
        for student in students_list:
            student_data = student.get_student_details()
            file.write(str(student_data) + "\n")

def load_student_data():
    try:
        with open("student_data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                student_data = eval(line)
                new_student = Student(student_data['student_name'], student_data['student_age'], student_data['student_number'])
                students_list.append(new_student)
    except FileNotFoundError:
        print("No student data file found")

load_student_data()

while True:
    try:
         # TODO 9 handle Exception for selection input
        selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))

        if selection == 1:
            student_number = input("Enter Student Number")
            student_name = input("Enter Student Name")
            while True:
                try:
                    student_age = int(input("Enter Student Age"))
                    break
                except ValueError:
                    print("Invalid Value")
            # TODO 10 create student object and append it to students list
            new_student = Student(student_name, student_age, student_number)
            students_list.append(new_student)
            print("Student Added Successfully")

        elif selection == 2:
            # TODO 11 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
            student_number = input("Enter Student Number")
            for student in students_list:
                if student.student_number == student_number:
                    students_list.remove(student)
                    print("Student Deleted Successfully")
                    break
            else:
                print("Student Not Found")

        elif selection == 3:
            # TODO 12 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
            student_number = input("Enter Student Number")
            for student in students_list:
                if student.student_number == student_number:
                    print("Student Details:")
                    print(student.get_student_details())
                    break
            else:
                print("Student Not Found")

        elif selection == 4:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    average = student.get_student_average()
                    print(f"Student Average: {average}")
                    if average == 0:
                        print("No courses found for the student.")
                    else:
                        print(f"Student Average: {average}")
                    break
            else:
                print("Student Not Found")
        # TODO 13 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
        elif selection == 5:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name: ")
                    course_mark = int(input("Enter Course Mark: "))
                    new_course = Course(course_name, course_mark)
                    student.enroll_course(new_course)
                    print("Course Added Successfully")
                    break
            else:
                print("Student Not Found")
        # TODO 14 ask user to enter course name and course mark then create coures object then append it to target student courses
        elif selection == 6:
            exit_program()

        else:
            print("Invalid Selection")
        # TODO 15 call a function to exit the program
    except ValueError:
        print("Invalid Input")