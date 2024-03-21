import uuid
import Person


class Student:

    def __init__(self, name):
        super(Person).__init__()
        self.student_id = "Student_" + str(uuid.uuid4())
        self.student_name = name


    def get_student_name(self):
        super()


    def get_student_id(self):
        return self.student_id

    def update_name(self, new_name):
        self.student_name = new_name




