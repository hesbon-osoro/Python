#The Time Module
import time

#time.altzone
'''The offset of the local DST timezone, in seconds west of UTC, if one is defined.
This is negative if the local DST timezone is east of UTC (as in Western Europe,
including the UK). Use this if the daylight is nonzero.'''
print("time.altzone:",time.altzone)

#time.asctime([tupletime])
'''Accepts a time-tuple and returns a readable 24-character string such as 
'Tue Dec 11 18:07:14 2008'.'''
print("time.asctime(time.localtime()):",time.asctime(time.localtime()))

#time.clock( )
#deprecated use
#time.process_time() or
#time.perf_counter()
'''Returns the current CPU time as a floating-point number of seconds. 
To measure computational costs of different approaches, the value of 
time.clock is more useful than that of time.time().'''
print("\ntime.clock() -deprecated, instead use\ntime.process_time() or time.perf_counter()")
print("view source code :)")
def procedure():
    time.sleep(.5)
#measure process time
#t0 = time.clock() #deprecated in Python 3.3 use time.perf_counter or time.process_time
t0 = time.process_time()
procedure()
print(time.process_time()-t0,"seconds process time {time.process_time()}")
print(time.perf_counter()-t0,"seconds process time {time.perf_counter()}")

#measure wall time
t0 = time.time()
procedure()
print(time.time()-t0,"seconds wall time")


#time.ctime([secs])
'''Like asctime(localtime(secs)) and without arguments is like asctime( )'''
print("time.ctime():",time.ctime())
print("time.ctime(0):",time.ctime(0))
print("time.ctime(36000000):",time.ctime(36000000))

#time.gmtime([secs])
'''Accepts an instant expressed in seconds since the epoch and returns a 
time-tuple t with the UTC time. Note : t.tm_isdst is always 0'''
print("time.gmtime():",time.gmtime())
print("time.gmtime(0):",time.gmtime(0))
print("time.gmtime(10240000):",time.gmtime(10240000))

#time.localtime([secs])
'''Accepts an instant expressed in seconds since the epoch and returns a 
time-tuple t with the local time (t.tm_isdst is 0 or 1, depending on 
whether DST applies to instant secs by local rules).'''
print("time.localtime():",time.localtime())
print("time.localtime(0):",time.localtime(0))
print("time.localtime(900000000):",time.localtime(900000000))


#time.mktime(tupletime)
'''Accepts an instant expressed as a time-tuple in local time and returns a 
floating- point value with the instant expressed in seconds since the epoch.'''
t = (2020,6,11,10,25,0,2,0,0)
print("t:",t)
print("time.mktime(t):",time.mktime(t))
print("time.asctime(time.localtime(time.mktime(t))):",time.asctime(time.localtime(time.mktime(t))))

#time.sleep(secs)
'''Suspends the calling thread for secs seconds.'''
print("Before sleep time.ctime():",time.ctime())
time.sleep(.5)
print("time.sleep(.5)")
print("After sleep time.ctime():",time.ctime())

#time.strftime(fmt[,tupletime])
'''Accepts an instant expressed as a time-tuple in local time and returns a string 
representing the instant as specified by string fmt.'''
print("\n***Directive***")
print("* %a - abbreviated weekday name ")
print("* %A - full weekday name ")
print("* %b - abbreviated month name ")
print("* %B - full month name ")
print("* %c - preferred date and time representation ")
print("* %C - century number (the year divided by 100, range 00 to 99) ")
print("* %d - day of the month (01 to 31) ")
print("* %D - same as %m/%d/%y")
print("* %e - day of the month (1 to 31) ")
print("* %g - like %G, but without the century")
print("* %G - 4-digit year corresponding to the ISO week number (see %V). ")
print("* %h - same as %b ")
print("* %H - hour, using a 24-hour clock (00 to 23)")
print("* %I - hour, using a 12-hour clock (01 to 12) ")
print("* %j - day of the year (001 to 366) ")
print("* %m - month (01 to 12) ")
print("* %M - minute")
print("* %n - newline character")
print("* %p - either am or pm according to the given time value ")
print("* %r - time in a.m. and p.m. notation ")
print("* %R - time in 24 hour notation")
print("* %S - second ")
print("* %t - tab character ")
print("* %T - current time, equal to %H:%M:%S")
print("* %u - weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1 ")
print("* %U - week number of the current year, starting with the first Sunday as the first day of the first week")
print("* %V - The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week")
print("* %W - week number of the current year, starting with the first Monday as the first day of the first week")
print("* %w - day of the week as a decimal, Sunday=0 ")
print("* %x - preferred date representation without the time")
print("* %X - preferred time representation without the date ")
print("* %y - year without a century (range 00 to 99) ")
print("* %Y - year including the century")
print("* %Z or %z - time zone or name or abbreviation ")
print("* %% - a literal % character")

print()
mk = time.asctime(time.localtime(time.mktime(t)))
print("t:",t)
print("mk = time.asctime(time.localtime(time.mktime(t)))")
print("mk:",mk)
print("time.strftime('%y'),time.ctime():",time.strftime("%y"),time.ctime())
print("time.strftime('%Y'),time.ctime():",time.strftime("%Y"),time.ctime())
print("time.strftime('%r'),time.asctime():",time.strftime("%r"),time.asctime())
print("time.strftime('%R'),time.process_time():",time.strftime("%R"),time.process_time())
print("time.strftime('%j'),time.process_time():",time.strftime("%j"),time.process_time())
print("time.strftime('%B'),time.process_time():",time.strftime("%B"),time.process_time())
print("time.strftime('%x'),time.process_time():",time.strftime("%x"),time.process_time())
print("time.strftime('%X),time.process_time():",time.strftime("%X"),time.process_time())
print("time.strftime('%z'),time.process_time():",time.strftime("%z"),time.process_time())
print("time.strftime('%Z'),time.process_time():",time.strftime("%Z"),time.process_time())
#time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
'''Parses str according to format string fmt and returns the instant in 
time-tuple format.'''
print()
print("time.strptime('12 6 2020','%d %m %Y'):",time.strptime('12 6 2020','%d %m %Y'))

#time.time( )
'''Returns the current time instant, a floating-point number of seconds since 
the epoch.'''
print("time.asctime(time.localtime(time.time())):",time.asctime(time.localtime(time.time())))

#time.tzset()
'''Resets the time conversion rules used by the library routines. 
The environment variable TZ specifies how this is done.'''
print("\nview source code :)")
"""
import os
os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print("time.strftime('%X %x %Z'):",time.strftime('%X %x %Z'))

os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print("time.strftime('%X %x %Z'):",time.strftime('%X %x %Z'))
"""
print()


#Two important attributes available with time module
#time.timezone
'''Attribute time.timezone is the offset in seconds of the local time zone 
(without DST) from UTC (>0 in the Americas; <=0 in most of Europe, Asia, Africa). '''

print("time.timezone:",time.timezone)
#time.tzname
'''Attribute time.tzname is a pair of locale-dependent strings, which are the 
names of the local time zone without and with DST, respectively. '''

print("time.tzname:",time.tzname)