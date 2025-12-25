import datetime, time

print("Current date and time:")
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S"))
time_now = time.strftime("%H:%M:%S")
print(time_now)
print(time.ctime())
