#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    time = s.split(':')

    hours = int(time[0])
    minutes = time[1]
    seconds = time[2][:-2]
    
    if 'PM' in time[2]:
        if hours < 12:
            hours = hours + 12
    elif 'AM' in time[2]:
        if hours == '12':
            hours = '00'
    else:
        hours = time[0]

    return str(hours)+':'+minutes+':'+seconds

s = input().strip()
result = timeConversion(s)
print(result)

