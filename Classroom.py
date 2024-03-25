

class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
        old_instructor = self.instructors.pop(self.instructors.index(instructor))


    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        old_student = self.students.pop(self.students.index(student))

    def print_instructors(self):
        print(self.instructors)
        return self.instructors

    def print_students(self):
        print(self.students)
        return self.students
