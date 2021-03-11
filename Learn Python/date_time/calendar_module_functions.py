#The Calendar Module
import calendar
import time
#calendar.calendar(year,w=2,l=1,c=6)
'''Returns a multiline string with a calendar for year year formatted into three 
columns separated by c spaces. w is the width in characters of each date; 
each line has length 21*w+18+2*c. l is the number of lines for each week.'''
print("calendar.calendar(2020,2,1,6)")
#print(calendar.calendar(2020))
print(calendar.calendar(2020,2,1,6))

#calendar.firstweekday( )
'''Returns the current setting for the weekday that starts each week. 
By default, when calendar is first imported, this is 0, meaning Monday.'''

print("calendar.firstweekday():",calendar.firstweekday())

#calendar.isleap(year)
'''Returns True if year is a leap year; otherwise, False.'''
print("calendar.isleap(2019):",calendar.isleap(2019))
print("calendar.isleap(2020):",calendar.isleap(2020))

#calendar.leapdays(y1,y2)
'''Returns the total number of leap days in the years within range(y1,y2).'''
print("calendar.leapdays(2000,2020):",calendar.leapdays(2000,2020))

#calendar.month(year,month,w=2,l=1)
'''Returns a multiline string with a calendar for month month of year year, 
one line per week plus two header lines. w is the width in characters of each date; 
each line has length 7*w+6. l is the number of lines for each week.'''

#print(calendar.month(2020,6))
print("\ncalendar.month(2020,6)\n",calendar.month(2020,6))
#calendar.monthcalendar(year,month)
'''Returns a list of lists of ints. Each sublist denotes a week. Days outside 
month month of year year are set to 0; days within the month are set to their 
day-of- month, 1 and up.'''

print("calendar.monthcalendar(2020,6):",calendar.monthcalendar(2020,6))

#calendar.monthrange(year,month)
'''Returns two integers. The first one is the code of the weekday for the first day of 
the month month in year year; the second one is the number of days in the month. 
Weekday codes are 0 (Monday) to 6 (Sunday); month numbers are 1 to 12.'''

print("calendar.monthrange(2020,2):",calendar.monthrange(2020,2))
print("calendar.monthcalendar(2020,2):",calendar.monthcalendar(2020,2))

#calendar.prcal(year,w=2,l=1,c=6)
'''Like print calendar.calendar(year,w,l,c).'''

print("calendar.prcal(2020)")
print(calendar.prcal(2020,2,1,6))
#print(calendar.prcal(2020))
#calendar.prmonth(year,month,w=2,l=1)
'''Like print calendar.month(year,month,w,l).'''

print("calendar.prmonth(2020,6,2,1)")
print(calendar.prmonth(2020,6,2,1))

#calendar.setfirstweekday(weekday)
'''Sets the first day of each week to weekday code weekday. Weekday codes are 0 (Monday) 
to 6 (Sunday).'''
calendar.setfirstweekday(6) #Sunday becomes the first week day
print(calendar.month(2020,6))

#calendar.timegm(tupletime)
'''The inverse of time.gmtime: accepts a time instant in time-tuple form and returns the 
same instant as a floating-point number of seconds since the epoch.'''
print("calendar.timegm((2020,8,2,13,45,1,0,0)):",calendar.timegm((2020,8,2,13,45,1,0,0)),"seconds since epoch (1970 1 1)")
print("calendar.timegm((2019,2,2,13,45,1,0,0)):",calendar.timegm((2019,2,2,13,45,1,0,0)),"seconds since epoch (1970 1 1)")
#calendar.weekday(year,month,day)
'''Returns the weekday code for the given date. Weekday codes are 0 (Monday) to 6 (Sunday);
 month numbers are 1 (January) to 12 (December).'''

print("calendar.weekday(2020,6,12):",calendar.weekday(2020,6,12))
print("calendar.weekday(2019,6,12):",calendar.weekday(2019,6,12))



#Link to other online modules to play with date & time in python
#link =  'The datetime Module', 'The pytz Module',  'The dateutil Module'
print("\n*Other Modules & Functions*")
print("http://docs.python.org/library/datetime.html#module-datetime")
print("http://www.twinsun.com/tz/tz-link.html")
print("http://labix.org/python-dateutil")
