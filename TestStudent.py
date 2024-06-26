import unittest
from Student import *
import datetime
from AliveStatus import AliveStatus
class TestStudent(unittest.TestCase):

    def test_get_id(self):
        # given
        new_stu = Student("Chris")
        new_stu.set_student_id()
        #when
        expected_id = new_stu.get_student_id()
        actual_id = new_stu.get_student_id()
        #then
        self.assertEqual(expected_id, actual_id)

    def test_get_diff_ids(self):
        # given
        new_stu = Student("Chris")
        new_stu2 = Student("Nate")
        new_stu.set_student_id()
        new_stu2.set_student_id()
        #when
        chris_id = new_stu.get_student_id()
        nate_id = new_stu2.get_student_id()
        #then
        self.assertNotEqual(chris_id, nate_id)

    def test_update_student_name(self):
        # given
        new_stu1 = Student("Chroa")
        expected_fname = "Chris"
        # when
        new_stu1.update_first_name("Chris")
        actual_fname = new_stu1.first_name
        # then
        self.assertEquals(expected_fname, actual_fname)

    def test_update_student_name(self):
        # given
        new_stu1 = Student("Chris")
        expected_fname = "McCall"
        # when
        new_stu1.update_last_name("McCall")
        actual_fname = new_stu1.last_name
        # then
        self.assertEqual(expected_fname, actual_fname)

    def test_update_dob(self):
        # given
        new_stu = Student("Chris")
        expected_dob = datetime.date(1994, 5, 24)
        # when
        new_stu.update_dob(1994, 5, 24)
        actual_dob = new_stu.datetime
        # then
        self.assertEqual(expected_dob, actual_dob)

    def test_update_status(self):
        # given
        new_stu = Student("chris")
        expected_status = AliveStatus.Alive.name
        # when
        new_stu.update_status(AliveStatus.Alive)
        actual_status = new_stu.AliveStatus.name
        # then
        self.assertEqual(expected_status, actual_status)








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
