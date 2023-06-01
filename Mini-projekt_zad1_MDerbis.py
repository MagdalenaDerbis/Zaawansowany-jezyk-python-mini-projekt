class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f'{self.hour}, {self.minute}'

    def is_24h_format(self):
        if isinstance(self.hour, int) and self.hour <= 24 and isinstance(self.minute, int) and self.minute <= 60:
            return True
        else:
            return False

    def __add__(self, other):
        actual_minute = 0
        actual_hour = 0
        if self.minute + other.minute >= 60:
            actual_minute = (self.minute+other.minute) - 60
            actual_hour+=1
        else:
            actual_minute = self.minute + other.minute

        if self.hour + other.hour >= 24:
            actual_hour += (self.hour+other.hour) - 24
        else:
            actual_hour += self.hour + other.hour

        return actual_hour, actual_minute

    def __gt__(self, other):
        return self.hour > other.hour


time1 = Time(12, 32)
time2 = Time(6, 23)
time3 = Time(16, 56)
time4 = Time(25, 20)
time5 = Time(13, 73)

print(time1.is_24h_format())
print(time2.is_24h_format())
print(time3.is_24h_format())
print(time4.is_24h_format())
print(time5.is_24h_format())

new_time1 = time1 + time3
print(new_time1)
new_time2 = time3 + time1
print(new_time2)
new_time3 = time2 + time1
print(new_time3)
new_time4 = time2 + time3
print(new_time4)

print(time1 > time2)
print(time2 > time3)
print(time3 > time1)