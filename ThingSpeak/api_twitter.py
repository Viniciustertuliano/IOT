#!/usr/bin/env python

import time, os, urllib
from urllib.request import urlopen

MAX_TEMP = 38
MIN_T = 60

BASE_URL ='https://api.thingspeak.com/apps/thingtweet/1/statuses/update/'
KEY = 'PS1GTQU45X6TUWJB'

def notification(temp):
    status = 'Raspberry Pi getting hot. CPU temp=' + temp
    data = urllib.urlencode({'api_key' : KEY, 'status': status})
    response = urlopen(url=BASE_URL, data=data)
    print(response.read())

def cpu_temp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = dev.read()[5:-3]
    print(cpu_temp)
    return cpu_temp

while True:
    temp = cpu_temp()
    print(type(temp))
    print("CPU Temp (C): " + str(temp))
    if temp > MAX_TEMP:
        print("CPU TOO HOT!")
        notification(temp)
        print("No more notifications for: " + str(MIN_T) + "mins")
    time.sleep(MIN_T * 60)
    time.sleep(1)
