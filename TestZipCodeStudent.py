import unittest
from ZipCodeStudent import *
from ZipCodeTrack import *
import datetime
from AliveStatus import AliveStatus


class TestStudent(unittest.TestCase):

    def test_set_track(self):
        # given
        new_zip = ZipCodeStudent("chris")
        expected_track = ZipCodeTrack.Data
        # when
        new_zip.set_track(ZipCodeTrack.Data)
        actual_track = new_zip.get_track()
        # then
        self.assertEquals(expected_track, actual_track)


    def test_get_id(self):
        # given
        new_stu = ZipCodeStudent("Chris")
        new_stu.set_student_id()
        #when
        expected_id = new_stu.get_student_id()
        actual_id = new_stu.get_student_id()
        #then
        self.assertEquals(expected_id, actual_id)

    def test_get_diff_ids(self):
        # given
        new_stu = ZipCodeStudent("Chris")
        new_stu2 = ZipCodeStudent("Nate")
        new_stu.set_student_id()
        new_stu2.set_student_id()
        #when
        chris_id = new_stu.get_student_id()
        nate_id = new_stu2.get_student_id()
        #then
        self.assertNotEquals(chris_id, nate_id)

    def test_update_student_name(self):
        # given
        new_stu1 = ZipCodeStudent("Chroa")
        expected_fname = "Chris"
        # when
        new_stu1.update_first_name("Chris")
        actual_fname = new_stu1.first_name
        # then
        self.assertEquals(expected_fname, actual_fname)

    def test_update_student_last_name(self):
        # given
        new_stu1 = ZipCodeStudent("Chris")
        expected_fname = "McCall"
        # when
        new_stu1.update_last_name("McCall")
        actual_fname = new_stu1.last_name
        # then
        self.assertEquals(expected_fname, actual_fname)

    def test_update_dob(self):
        # given
        new_stu = ZipCodeStudent("Chris")
        expected_dob = datetime.date(1994, 5, 24)
        # when
        new_stu.update_dob(1994, 5, 24)
        actual_dob = new_stu.datetime
        # then
        self.assertEquals(expected_dob, actual_dob)

    def test_update_status(self):
        # given
        new_stu = ZipCodeStudent("chris")
        expected_status = AliveStatus.Alive.name
        # when
        new_stu.update_status(AliveStatus.Alive)
        actual_status = new_stu.AliveStatus.name
        # then
        self.assertEquals(expected_status, actual_status)
