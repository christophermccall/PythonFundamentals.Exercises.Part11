import uuid
from Person import *


class Student(Person):

    def __init__(self, name):
        super(Person).__init__()
        self.student_id = "Student_"
        self.student_name = name

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, ):
        self.student_id = self.student_id + str(uuid.uuid4())


