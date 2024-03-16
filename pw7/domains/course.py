from .super_class import Super_class

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
