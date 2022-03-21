class ClockTime:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # SetHours Function
    def setHours(self, hours):
        self.hours = hours

    # SetMinutes Function
    def setMinutes(self, minutes):
        self.minutes = minutes

    # SetSeconds Function
    def setSeconds(self, seconds):
        self.seconds = seconds

    # SetTime Function
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # ShowTime Function
    def showTime(self):
        print("Formatted Time:" + self.hours + ":" +
              self.minutes + ":" + self.seconds)


hours = input("Enter Hours: ")
minutes = input("Enter Minutes: ")
seconds = input("Enter Seconds: ")
formattedTime = ClockTime(hours, minutes, seconds)
formattedTime.showTime()
