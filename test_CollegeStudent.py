import unittest
from CollegeStudent import *
import datetime
from AliveStatus import AliveStatus

class TestCollegeStudent(unittest.TestCase):
    def test_get_college(self):
        # given
        new_stu = CollegeStudent("Chris", "McCall", "Lincoln University")
        expected_coll = "Lincoln University"
        # when
        actual_coll = new_stu.get_college()
        # then

        self.assertEquals(expected_coll, actual_coll)

    def test_get_id(self):
        # given
        new_stu = CollegeStudent("Chris", "McCall", "Lincoln University")
        new_stu.set_student_id()
        #when
        expected_id = new_stu.get_student_id()
        actual_id = new_stu.get_student_id()
        #then
        self.assertEquals(expected_id, actual_id)

    def test_get_diff_ids(self):
        # given
        new_stu = CollegeStudent("Chris", None, None)
        new_stu2 = CollegeStudent("Nate", None, None)
        new_stu.set_student_id()
        new_stu2.set_student_id()
        #when
        chris_id = new_stu.get_student_id()
        nate_id = new_stu2.get_student_id()
        #then
        self.assertNotEquals(chris_id, nate_id)

    def test_update_student_name(self):
        # given
        new_stu1 = CollegeStudent("Chirs", "McCall", "Lincoln University")
        expected_fname = "Chris"
        # when
        new_stu1.update_first_name("Chris")
        actual_fname = new_stu1.get_first_name()
        # then
        self.assertEquals(expected_fname, actual_fname)

    def test_update_student_name(self):
        # given
        new_stu1 = CollegeStudent("Chris", "macal", "Lincoln University")
        expected_fname = "McCall"
        # when
        new_stu1.update_last_name("McCall")
        actual_fname = new_stu1.get_last_name()
        # then
        self.assertEquals(expected_fname, actual_fname)

    def test_update_dob(self):
        # given
        new_stu = CollegeStudent("Chris", "McCall", "Lincoln University")
        expected_dob = datetime.date(1994, 5, 24)
        # when
        new_stu.update_dob(1994, 5, 24)
        actual_dob = new_stu.datetime
        # then
        self.assertEquals(expected_dob, actual_dob)

    def test_update_status(self):
        # given
        new_stu = CollegeStudent("Chris", "McCall", "Lincoln University")
        expected_status = AliveStatus.Alive.name
        # when
        new_stu.update_status(AliveStatus.Alive)
        actual_status = new_stu.AliveStatus.name
        # then
        self.assertEquals(expected_status, actual_status)





