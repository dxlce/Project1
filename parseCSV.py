import os
import csv

test_list1 = []
class HeartRate:
    def __init__(self, filename='filename.csv'):

        f = open(filename)
        csv_f = csv.reader(f)
        next(csv_f)
        heartrate = []

        for row in csv_f:
            heartrate.append(row[1])

        print str(len(heartrate))

        for i in range(0, int(len(heartrate)/3600)+1):
            for ele in range(0, 3600):
                with open("hour" + str(i) + ".csv", 'wb') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(heartrate[ele*i])
          
"""
      self.heartrate = []
      print self.heartrate
"""

test_list2 = HeartRate(filename='alexHR.csv')
