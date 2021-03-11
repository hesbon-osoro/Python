#Getting Current Time
import time
print("%s"%'getting current time'.title())
print("time.localtime():",time.localtime())
print("%s"%'\ngetting formatted time'.title())
print("time.asctime(time.localtime(time.time())):",time.asctime(time.localtime(time.time())))

print("%s"%'\ngetting calendar for a month'.title())
import  calendar
print("calendar.month(2020,6)")
print(calendar.month(2020,6))

