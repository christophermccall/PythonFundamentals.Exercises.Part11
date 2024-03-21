import Student
import Instructor


class ZipCodeStudent:
    def __init__(self):
        self.students = {}
        self.instructors = {}

    def add_instructor(self, instructor):
        self. instructors = self.instructors.update(instructor)

    def remove_instructor(self, instructor):
        self.instructors = self.instructors.pop(instructor)

    def add_student(self, student):
        self.instructors = self.students.update(student)

    def remove_student(self, student):
        self.instructors = self.students.pop(student)

    def print_instructors(self):
        return self.instructors

    def print_students(self):
        return self.students
