from domains.student import Student
from domains.course import Course

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
    gpa_list = []
    for student in student_list:
        total_mark = 0
        total_credit = 0
        print(f"Enter marks for student {student.get_name()} (ID: {student.get_id()})")
        for course in course_list:
            mark = float(input(f"Course {course.get_name()} (ID: {course.get_id()}) mark: "))
            total_mark += mark
            total_credit += course.get_credit()
        gpa = total_mark / total_credit
        gpa_list.append(gpa)
    return gpa_list

def get_ordinal_number(n):
    if 10 <= n % 100 < 20:
        return str(n) + "th"
    else:
        ordinal = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
        return str(n) + ordinal