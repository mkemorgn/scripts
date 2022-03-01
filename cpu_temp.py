#!/usr/bin/env python3

"""
This script finds the average temp of all cores on my pc.  Originally made to display in Polybar
"""
import psutil
import math

raw_temp = psutil.sensors_temperatures().get("coretemp")[1:7]


def Average(temp):
    return sum(temp) / len(temp)


temp = []
for i in raw_temp:
    temp.append(i[1])

average_c = Average(temp)

# Convert the average Celsius to Fahrenheit
average_f = (average_c * 1.8) + 32
print(round(average_f))
