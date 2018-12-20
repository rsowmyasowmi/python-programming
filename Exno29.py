time = float(input("Input time in minutes: "))
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
print("d:h:m:s-> %d:%d:%d:%d" % (hour, minutes))

