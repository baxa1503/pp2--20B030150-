import datetime

now = datetime.datetime.now()
without_microseconds = now.replace(microsecond=0)

print("Current datetime with microseconds:", now)
print("Current datetime without microseconds:", without_microseconds)
