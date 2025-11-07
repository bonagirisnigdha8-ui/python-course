import random

import time


def getRandomdate(starDate, endDate):
    print("Printing random date between",starDate,"and",endDate)
    randomGenerator = random.random()
    dateformat = '%m/%d/%y'
    starttime = time.mktime(time.strptime(starDate, dateformat))
    endtime = time.mktime(time.strptime(endDate, dateformat))
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomTime))
    return randomdate


print("Random date = ",getRandomdate("1/1/2020","12/12/2024"))