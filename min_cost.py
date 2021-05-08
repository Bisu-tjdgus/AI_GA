import math

def csv2list(filename):
    import csv
    data = list()
    f = open(filename, 'r')
    rea = csv.reader(f)
    for row in rea:
        data.append(row)
    f.close
    #str to float
    import numpy as np
    data = list(np.float_(data))
    return data

def distanceTo(self, city):
    xDistance = abs(data[self][0] - data[city][0])
    yDistance = abs(data[self][1] - data[city][1])
    distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
    return distance

def mindistance(self):
    min_d = 99999
    for city in range(0,999):
        temp = distanceTo(self,city)
        if min_d > temp and temp !=0:
            min_d = distanceTo(self, city)
    return min_d

data=csv2list("C:\Pycharm\AI_GA-master\GA_TSP\TSP.csv")
sum = 0
for t in range(0,999):
    sum += mindistance(t)
print(sum)