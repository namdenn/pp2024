import math
import numpy as np

class Super_class:
    def __init__(self, id, name):
        self.__ID = id
        self.__NAME = name

    def get_id(self):
        return self.__ID

    def get_name(self):
        return self.__NAME


class Student(Super_class):
    def __init__(self, student_id, student_name, student_dob):
        super().__init__(student_id, student_name)
        self.__DOB = student_dob
        self.__MARK = 0

    def get_dob(self):
        return self.__DOB

    def get_mark(self):
        return self.__MARK

    def set_mark(self, mark):
        self.__MARK = mark
   
    @staticmethod
    def input_info_student():
        num = int(input("Enter number of students: "))
        student_list = []
        for i in range(1, num + 1):
            student_id = input("Student ID: ")
            student_name = input("Name: ")
            student_dob = input("Date of birth (yyyy/mm/dd): ")
            student = Student(student_id, student_name, student_dob)
            student_list.append(student)
        return student_list


class Course(Super_class):
    def __init__(self, course_id, course_name, course_credit):
        super().__init__(course_id, course_name)
        self.__CREDIT = course_credit

    def get_credit(self):
        return self.__CREDIT

    def set_credit(self, credit):
        self.__CREDIT = credit

    @staticmethod
    def input_info_course():
        num = int(input("Enter number of courses: "))
        course_list = []
        for i in range(1, num + 1):
            course_id = input("Course ID: ")
            course_name = input("Name: ")
            course_credit = int(input("Credits: "))
            course = Course(course_id, course_name, course_credit)
            course_list.append(course)
        return course_list

def input_mark(course_list, student_list):
    final_gpa_array = []
    
    for student in student_list:
        credit_array = np.empty((0,))
        mark_array = np.empty((0,))
        
        for course in course_list:
            student_mark = float(input(f"Enter the marks for student {student.get_id()} for course {course.get_name()}: "))
            round_mark = math.floor(student_mark * 10) / 10
            student.set_mark(round_mark)

            credit_array = np.append(credit_array, course.get_credit())
            mark_array = np.append(mark_array, student.get_mark())

        weighted_sum = np.dot(credit_array, mark_array)
        total_credit = np.sum(credit_array)
        final_gpa = weighted_sum/total_credit
        final_gpa_array.append(final_gpa)

    return final_gpa_array

def get_ordinal_number(number):
    last_digit = number % 10
    if last_digit == 1 and number != 11:
        ordinal = f"{number}"
    elif last_digit == 2 and number != 12:
        ordinal = f"{number}"
    elif last_digit == 3 and number != 13:
        ordinal = f"{number}"
    else:
        ordinal = f"{number}"
    return ordinal

def display_mark_sheet(sorted_list):
    print("---------------------------------------------------")
    print("--------------------MARK SHEET---------------------")
    for i, (student, gpa) in enumerate(sorted_list, start=1):
        ordinal = get_ordinal_number(i)
        print(f"{ordinal} | Student: {student.get_name()} | ID: {student.get_id()} | GPA: {gpa}")

student_list = Student.input_info_student()
print("---------------------------------------------------")
print("The number of students is:", len(student_list))
for student in student_list:
    print("ID:", student.get_id())
    print("Name:", student.get_name())
    print("DOB:", student.get_dob())
print("---------------------------------------------------")

course_list = Course.input_info_course()
print("---------------------------------------------------")
print("The number of courses is:", len(course_list))
for course in course_list:
    print("ID:", course.get_id())
    print("Name:", course.get_name())
    print("Credit:", course.get_credit())
print("---------------------------------------------------")

gpa = input_mark(course_list, student_list)
combined_list = list(zip(student_list, gpa))
sorted_list = sorted(combined_list, key=lambda x: x[1], reverse=True) 

display_mark_sheet(sorted_list)
