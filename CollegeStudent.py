from Student import *


class CollegeStudent (Student):

    def __init__(self, fname, lname, school):
        super().__init__(self)
        self.set_student_id()
        self.first_name = fname
        self.last_name = lname
        self.college = school


    def get_college(self):
        return self.college

    def set_college(self, school_name):
        self.college = school_name
