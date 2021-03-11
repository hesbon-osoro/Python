#Time Tuple
import time
print("Many of the Python's time functions handle time as a tuple of 9 numbers, as shown below- ")
#timetuple = ['4-digit year' 2016, Month 1 to 12   Day 1 to 31]
field = ('4-digit year','Month','Day','Hour','Minute','Second','Day of Week','Day of year','Daylight savings')
values = (2020,'1 to 12','1 to 31','0 to 23','0 to 59','0 to 61 (60 or 61 are leap-seconds)','0 to 6 (0 is Monday)','1 to 366 (Julian day)','-1, 0, 1, -1 means library determines DST')
attributes = ('tm_year','tm_mon','tm_mday','tm_hour','tm_min','tm_sec','tm_wday','tm_yday','tm_isdst')
print("\n%s\t%s\t%s\n"%('index'.title(),'field'.title().ljust(16,' '),'values'.title()))
#loop to generate a table for time tuple
for i in range(9):
    print("%5d\t%16s\t%s\n"%(i,field[i].ljust(16,' '),values[i]))
print("Example:-")
print("time.localtime():",time.localtime())

print("\nThe above tuple is equivalent to struct_time structure. This structure has the following attributes-")
print("\n%s\t%s\t%s\n"%('index'.title(),'attributes'.title().ljust(16,' '),'values'.title()))
#loop to generate a table for struct_time
for i in range(9):
    print("%5d\t%16s\t%s\n"%(i,attributes[i].ljust(16,' '),values[i]))


