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

def input_mark(course_list, student_list):
    course_id = int(input("Select your course: "))
    for course in course_list:
        if course['ID'] == course_id:
            selected_course = course
            break

    print("ID:", selected_course['ID'])
    print("Name:", selected_course['NAME'])
    for i in student_list:
        student_mark = float(input(f"Enter the marks for student {i['ID']}: "))
        i['MARK'] = student_mark
        print(f"Mark for student {i['ID']}: {student_mark}")

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
input_mark(course, student_list)
print("---------------------------------------------------")
print("__STUDENTS MARK__")
for i, student_info in enumerate(student_list, 1):
    print(f"{i}. ID: {student_info['ID']}, Name: {student_info['NAME']}, Mark: {student_info['MARK']}  ")
