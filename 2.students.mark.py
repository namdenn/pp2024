class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.ID = student_id
        self.NAME = student_name
        self.DOB = student_dob
        self.MARK = 0

class Course:
    def __init__(self, course_id, course_name):
        self.ID = course_id
        self.NAME = course_name

def input_number_student():
    number = int(input("Enter number of students: "))
    return number

def input_info_student(num):
    student_list = []
    for i in range(1, num + 1):
        student_id = str(input("Student ID: "))
        student_name = str(input("Name: "))
        student_dob = input("Date of birth (yyyy/mm/dd): ")
        student = Student(student_id, student_name, student_dob)
        student_list.append(student)
    return student_list

def input_number_course():
    number = int(input("Enter number of courses: "))
    return number

def input_info_course(num):
    course_list = []
    for i in range(1, num + 1):
        course_id = int(input("Course ID: "))
        course_name = str(input("Name: "))
        course = Course(course_id, course_name)
        course_list.append(course)
    return course_list

def input_mark(course_list, student_list):
    course_id = int(input("Select your course: "))
    selected_course = None
    for course in course_list:
        if course.ID == course_id:
            selected_course = course
            break

    print("ID:", selected_course.ID)
    print("Name:", selected_course.NAME)
    for student in student_list:
        student_mark = float(input(f"Enter the marks for student {student.ID}: "))
        student.MARK = student_mark
        print(f"Mark for student {student.ID}: {student_mark}")

number_student = input_number_student()
student_list = input_info_student(number_student)
print("---------------------------------------------------")
print("The number of students is:", number_student)
for student in student_list:
    print("ID:", student.ID)
    print("Name:", student.NAME)
    print("DOB:", student.DOB)
print("---------------------------------------------------")
number_course = input_number_course()
course_list = input_info_course(number_course)
print("---------------------------------------------------")
print("The number of courses is:", number_course)
for course in course_list:
    print("ID:", course.ID)
    print("Name:", course.NAME)
print("---------------------------------------------------")
input_mark(course_list, student_list)
print("---------------------------------------------------")
print("__STUDENTS MARK__")
for i, student in enumerate(student_list, 1):
    print(f"{i}. ID: {student.ID}, Name: {student.NAME}, Mark: {student.MARK}")
