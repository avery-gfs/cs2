def checkEqual(a, b):
    print(a, "==", b, a == b)

# A class representing a time with some number of hours and minutes

class Time:
    def __init__(self, hours, minutes):
        # Add code to add hours and minutes fields to Time
        # Make sure to adjust hours and minutes
        # when minutes >= 60

        while minutes >= 60:
            minutes -= 60
            hours += 1

        self.hours = hours
        self.minutes = minutes

    def __repr__(self):
        # Add code to print out a Time in "hours:minutes" format
        if self.minutes < 10:
            return f"{self.hours}:0{self.minutes}"

        return f"{self.hours}:{self.minutes}"

    def addHours(self, hours):
        # Add code to make a new Time object with additional hours
        return Time(self.hours + hours, self.minutes)

    def addMinutes(self, minutes):
        # Add code to make a new Time object with additional minutes
        return Time(self.hours, self.minutes + minutes)

print(Time(10, 15).hours == 10)
print(Time(10, 15).minutes == 15)
print(str(Time(10, 15)) == "10:15")
print(str(Time(10, 5)) == "10:05")
print(str(Time(12, 0)) == "12:00")
print(str(Time(1, 0)) == "1:00")
print(Time(1, 15).addHours(4).hours == 5)
print(Time(1, 15).addMinutes(5).minutes == 20)
print(Time(1, 15).addMinutes(5).hours == 1)
print(Time(1, 15).addMinutes(65).minutes == 20)
print(Time(1, 15).addMinutes(65).hours == 2)
print(Time(1, 15).addMinutes(45).minutes == 0)
print(Time(1, 15).addMinutes(45).hours == 2)
