class Confidential:
    def __init__(self, secret_code, meeting_location, meeting_time):
        self.secret_code = secret_code
        self.meeting_location = meeting_location
        self.meeting_time = meeting_time


code, location, time = input().split()

command1 = Confidential(code, location, time)
print(f"secret code : {command1.secret_code}")
print(f"meeting point : {command1.meeting_location}")
print(f"time : {command1.meeting_time}")