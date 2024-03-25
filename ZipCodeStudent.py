
from Student import *


class ZipCodeStudent(Student):
    def __init__(self, name):
        super().__init__(self)
        self.set_student_id()
        self.name = name
        self.trk = None

    def get_track(self):
        return self.trk

    def set_track(self, track):
        self.trk = track






