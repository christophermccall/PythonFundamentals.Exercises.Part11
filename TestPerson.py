import Person
import unittest
import AliveStatus as alive
import datetime



class TestPerson(unittest.TestCase):


    def test_update_first_name(self):
        # given
        new_person = Person.Person()
        expected_fname = "Chris"
        # when
        new_person.update_first_name("Chris")
        actual_fname = new_person.first_name
        # then
        self.assertEquals(expected_fname, actual_fname)

    def test_update_last_name(self):
        # given
        new_person = Person.Person()
        expected_lname = "McCall"
        # when
        new_person.update_last_name("McCall")
        actual_lname = new_person.last_name
        # then
        self.assertEquals(expected_lname, actual_lname)

    def test_update_dob(self):
        # given
        new_person = Person.Person()
        expected_dob = datetime.date(1994, 5, 24)
        # when
        new_person.update_dob(1994, 5, 24)
        actual_dob = new_person.datetime
        # then
        self.assertEquals(expected_dob, actual_dob)

    def test_update_status(self):
        # given
        new_person = Person.Person()
        expected_status = alive.AliveStatus.Alive
        # when
        new_person.update_status(alive.AliveStatus.Alive)
        actual_status = new_person.Alive.AliveStatus
        # then
        self.assertEquals(expected_status, actual_status)