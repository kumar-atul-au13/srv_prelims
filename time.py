class Tim:
    def __init__(self, hr, min):
        if str(hr).isdigit() and (0 <= hr <= 12):
            self.hr = hr
        else:
            self.hr = None
            print("Invalid hr")

        if str(min).isdigit() and (0 <= min <= 60):
            self.min = min
        else:
            self.min = None
            print("Invalid min")

    def addTime(time1, time2):
        if not (time1 and time1.hr and time1.min):
            return
        if not (time2 and time2.hr and time2.min):
            return
        total_min = (time1.min + time2.min)
        min = total_min % 60
        hr = time1.hr + time2.hr + total_min // 60
        print("added hr is ", hr, " added min is ", min)
        return

    def display_time(self):
        if self.hr and self.min:
            print("hr is ", self.hr, "min is ", self.min)

    def total_minutes(self):
        if self.hr and self.min:
            print(" total min is ", self.hr * 60 + self.min)


time1 = Tim(12, 45)
time1.display_time()
time1.total_minutes()

time2 = Tim(4, 6)
time2.display_time()
time2.total_minutes()

Tim.addTime(time1,time2)
