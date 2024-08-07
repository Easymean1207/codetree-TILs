class RequireInfo:
    def __init__(self, release_code, line_color, right_timing):
        self.release_code = release_code
        self.line_color = line_color
        self.right_timing = right_timing


given_code, given_color, given_timing = tuple(input().split())
given_color = given_color.capitalize()
given_timing = int(given_timing)

info1 = RequireInfo(given_code, given_color, given_timing)

print(f"code : {info1.release_code}")
print(f"color : {info1.line_color}")
print(f"second : {info1.right_timing}")