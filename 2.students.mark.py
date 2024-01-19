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
    def __init__(self, course_id, course_name):
        super().__init__(course_id, course_name)

    @staticmethod
    def input_info_course():
        num = int(input("Enter number of courses: "))
        course_list = []
        for i in range(1, num + 1):
            course_id = int(input("Course ID: "))
            course_name = input("Name: ")
            course = Course(course_id, course_name)
            course_list.append(course)
        return course_list

def input_mark(course_list, student_list):
    course_id = int(input("Select your course: "))
    selected_course = None
    for course in course_list:
        if course.get_id() == course_id:
            selected_course = course
            break

    print("ID:", selected_course.get_id())
    print("Name:", selected_course.get_name())
    for student in student_list:
        student_mark = float(input(f"Enter the marks for student {student.get_id()}: "))
        student.set_mark(student_mark)
        print(f"Mark for student {student.get_id()}: {student.get_mark()}")


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
print("---------------------------------------------------")
input_mark(course_list, student_list)
print("---------------------------------------------------")
print("__STUDENTS MARK__")
for i, student in enumerate(student_list, 1):
    print(f"{i}. ID: {student.get_id()}, Name: {student.get_name()}, Mark: {student.get_mark()}")