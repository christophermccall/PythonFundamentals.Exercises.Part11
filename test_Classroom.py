from unittest import TestCase
from Classroom import *


class TestClassroom(TestCase):
    def test_add_instructor(self):
        new_class = Classroom()
        # given
        new_class.add_instructor("Prof. Green")
        new_class.add_instructor("Prof. H. Wade Johnson")
        expected_instructors = ["Prof. Green", "Prof. H. Wade Johnson"]
        # when
        actual_instructors = new_class.print_instructors()
        # then
        self.assertEqual(expected_instructors, actual_instructors)

    def test_remove_instructor(self):
        new_class = Classroom()
        # given
        new_class.add_instructor("Prof. Green")
        new_class.add_instructor("Prof. H. Wade Johnson")
        new_class.remove_instructor("Prof. Green")
        expected_instructor = ["Prof. H. Wade Johnson"]
        # when
        actual_instructor = new_class.print_instructors()
        # then
        self.assertEqual(expected_instructor, actual_instructor)

    def test_add_student(self):
        new_class = Classroom()
        # given
        new_class.add_student("Greg McCall")
        new_class.add_student("Chris McCall")
        expected_students = ["Greg McCall", "Chris McCall"]
        # when
        actual_students = new_class.print_students()
        # then
        self.assertEqual(expected_students, actual_students)

    def test_remove_student(self):
        new_class = Classroom()
        # given
        new_class = Classroom()
        # given
        new_class.add_student("Greg McCall")
        new_class.add_student("Chris McCall")
        new_class.remove_student("Greg McCall")
        expected_student = ["Chris McCall"]
        # when
        actual_student = new_class.print_students()
        # then
        self.assertEqual(expected_student, actual_student)

        # should I still test if they're being tested repeatedly in the tests above?


    # def test_print_instructors(self):
    #     self.fail()
    #
    # def test_print_students(self):
    #     self.fail()
