class RequireInfo:
    def __init__(self, release_code, line_color, right_timing):
        self.release_code = release_code
        self.line_color = line_color
        self.right_timing = right_timing


release_code, color, timing = tuple(input().split())
color = color.capitalize()
timing = int(timing)

info1 = RequireInfo(release_code, color, timing)

print(f"code : {info1.release_code}")
print(f"color : {info1.line_color}")
print(f"second : {info1.right_timing}")