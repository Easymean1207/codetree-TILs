str1 = input()
str2 = input()
str3 = input()

longest = max(len(str1),len(str2),len(str3))
shortest = min(len(str1),len(str2),len(str3))
print(longest-shortest)