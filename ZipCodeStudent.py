import Student
from ZipCodeTrack import *

class ZipCodeStudent(Student):
    def __init__(self,name,track):
        super().__init__(self,name)
        self.java = {}
        self.data ={}
        self.track = ZipCodeTrack.name


    # def get_track(self):
    #     return self.track
    #
    # def choose_track(self,track):
    #     try:
    #         super()
    #         if track is ZipCodeTrack.Data:
    #             self.data = self.data.update():
    #





