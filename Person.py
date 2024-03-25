import datetime


class Person:
    import AliveStatus

    def __init__(self):
        self.AliveStatus = None
        self.first_name = ''
        self.last_name = ''
        self.datetime = datetime.date(1900, 1, 1)

    def update_first_name(self, fname):
        self.first_name = fname

    def update_last_name(self, lname):
        self.last_name = lname

    def update_dob(self, year, month, day):
        self.datetime = datetime.date(year, month, day)

    def update_status(self, status):
        self.AliveStatus = status

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
