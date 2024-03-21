import uuid
import Person


class Instructor(Person):

    def __init__(self):
        super(Person)
        self.instructor_id = "Instructor_" + str(uuid.uuid4())
