import unittest
import Person
from Student import Student


class TestStudent(unittest.TestCase):

    def test_get_id(self):
        # give
        new_stu = Student("Chris")

        Student.get_student_id(new_stu)
        self.assertEquals(2, 3)






    # def test_update_name(self):
    #     # given
    #     new_stu = Student('')
    #     exp_name = "joe"
    #     #when
    #     new_stu.update_name("joe")
    #     act_name = new_stu.get_student_name()
    #
    #     # then
    #     self.assertEquals(exp_name, act_name)
