class Clock:
    def __init__(self, hour, minute):
        mins = (hour * 60) + minute
        self.hour = (mins // 60) % 24
        self.minute = mins % 60

    def __repr__(self):
        return str(self.hour).zfill(2) + ":" + str(self.minute).zfill(2)

    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        else:
            return False 

    def __add__(self, minutes):
        mins = self.minute + minutes + (self.hour * 60)
        self.hour = (mins // 60) % 24
        self.minute = mins % 60
        return self

    def __sub__(self, minutes):
        mins = self.minute - minutes + (self.hour * 60)
        self.hour = (mins // 60) % 24
        self.minute = mins % 60
        return self
