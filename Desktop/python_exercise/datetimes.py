
from datetime import datetime, timedelta
#timedelta represent diff between two dates and times
from intervals import Interval

start_time_str = input("Enter start time (YYYY-MM-DD HH:MM): ")
end_time_str = input("Enter end time (YYYY-MM-DD HH:MM): ")

start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

# night intervals
night_start = Interval(start_time.replace(hour=0, minute=0, second=0))
night_end = Interval(start_time.replace(hour=5, minute=59, second=59))

adjusted_time_difference = timedelta()

while start_time < end_time:
    if start_time < night_start:
        if end_time < night_start:
            adjusted_time_difference += end_time - start_time
            break
        else:
            adjusted_time_difference += night_start - start_time
    elif start_time > night_end:
        adjusted_time_difference += end_time - start_time
        break
    start_time = night_end
    night_start += timedelta(days=1)
    night_end += timedelta(days=1)

print("Adjusted time difference:", adjusted_time_difference)


