from datetime import datetime
now = datetime.now()
timedel = datetime.timedelta(days=7)
print now
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second


print "1 week ago was it: ", now - datetime.timedelta(weeks=1)
print "100 days ago was: ", now - datetime.timedelta(days=100)
print "1 week from now is it: ",  now + datetime.timedelta(weeks=1)
print "In 1000 days from now is it: ", now + datetime.timedelta(days=1000)

birthday = datetime.datetime(2012,11,04)

print "Birthday in ... ", birthday - now