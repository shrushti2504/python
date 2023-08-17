import datetime 
start = datetime.datetime(2019,12,12,11,11,11)
end = datetime.datetime(2020,7,12,5,4,3)
diff=start-end
print(diff)

minutes = divmod(diff.seconds, 60) 
print('Total difference in minutes: ', minutes[0], 'minutes',minutes[1], 'seconds')
