# Convert time in milliseconds
import time

def past(timestamp): #timestamp is a string in the format of HH:MM:SS
    h,m,s = map(int,timestamp.split(':')) #split the string into hours, minutes and seconds
    convert_in_seconds=h*3600 + m*60 + s #convert the hours, minutes and seconds into seconds
    millisecond=convert_in_seconds*1000 #convert the seconds into milliseconds
    return millisecond

timestamp = time.strftime('%H:%M:%S') #get the current time in the format of HH:MM:SS
print(timestamp)
print(past(timestamp)) #print the current time in milliseconds