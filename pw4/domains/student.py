from .super_class import Super_class

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