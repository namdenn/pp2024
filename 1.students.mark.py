def input_number_student():
    number = int(input("Enter number of students: "))
    return number

def input_info_student(num):
    student_list = []
    for i in range(1, num + 1):
        student_id = str(input("Student ID: "))
        student_name = str(input("Name: "))
        student_dob = input("Date of birth (yyyy/mm/dd): ")
        student_info = {
            'ID': student_id,
            'NAME': student_name,
            'DOB': student_dob
        }
        student_list.append(student_info)
    return student_list

def input_number_course():
    number = int(input("Enter number of courses: "))
    return number

def input_info_course(num):
    course_list = []
    for i in range(1, num + 1):
        course_id = int(input("Course ID: "))
        course_name = str(input("Name: "))
        course_info = {
            'ID': course_id,
            'NAME': course_name,
        }
        course_list.append(course_info)
    return course_list

def select_course(course_list):
    course_id = int(input("Select your course: "))
    selected_course = None
    for course in course_list:
        if course['ID'] == course_id:
            selected_course = course
            break
    if selected_course:
        print("ID:", selected_course['ID'])
        print("Name:", selected_course['NAME'])
        for student in student_list:
            student_marks = float(input(f"Enter the marks for student {student['ID']}: "))
            student['MARKS'] = student_marks
            print(f"Mark for student {student['ID']}: {student_marks}")
    else:
        print("///Course is not found///")

number_student = input_number_student()
student_list = input_info_student(number_student)
print("---------------------------------------------------")
print("The number of students is:", number_student)
print(student_list)
print("---------------------------------------------------")
number_course = input_number_course()
course = input_info_course(number_course)
print("---------------------------------------------------")
print("The number of courses is:", number_course)
print(course)
print("---------------------------------------------------")
select_course(course)
print("---------------------------------------------------")
print("Updated student list:")
print(student_list)