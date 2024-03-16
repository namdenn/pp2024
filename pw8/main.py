from input import input_info_student, input_info_course, input_mark, get_ordinal_number
from output import display_mark_sheet

import pickle
import gzip
import threading
import time

def save_data():
    file_path = 'student.data'

    with gzip.open(file_path, 'wb') as file:
        pickle.dump(student_list, file)

    print("Data saved successfully.")

# Your existing code
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


file_path = 'student.data'  

def save_data():
    global file_path  

    with gzip.open(file_path, 'wb') as file:
        pickle.dump(student_list, file)

    print("Data saved successfully.")

save_thread = threading.Thread(target=save_data)
save_thread.start()

time.sleep(1) 
print("Continuing with the program...")

save_thread.join()

with gzip.open(file_path, 'rb') as file:
    student_list = pickle.load(file)

print(student_list)