from input import input_info_student, input_info_course, input_mark, get_ordinal_number
from output import display_mark_sheet

student_list = input_info_student()
print("---------------------------------------------------")
print("The number of students is:", len(student_list))
for student in student_list:
    print("ID:", student.get_id())
    print("Name:", student.get_name())
    print("DOB:", student.get_dob())
print("---------------------------------------------------")

course_list = input_info_course()
print("---------------------------------------------------")
print("The number of courses is:", len(course_list))
for course in course_list:
    print("ID:", course.get_id())
    print("Name:", course.get_name())
    print("Credit:", course.get_credit())
print("---------------------------------------------------")

gpa_list = input_mark(course_list, student_list)

combined_list = list(zip(student_list, gpa_list))
sorted_list = sorted(combined_list, key=lambda x: x[1], reverse=True)

display_mark_sheet(sorted_list)

import zipfile as zp

with zp.ZipFile("student.data", "w") as zip_file:

    zip_file.write("/home/nick/app/labwork/pp2024/pw5/input.py")

    zip_file.write("/home/nick/app/labwork/pp2024/pw5/output.py")

    zip_file.close()

print("Files compressed into 'student.data' successfully.")