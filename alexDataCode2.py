import datetime
import os
import csv

class HeartRate:
    def __init__(self, filename='filename.csv'):

        f = open(filename)
        csv_f = csv.reader(f)
        next(csv_f)
        hrTime = []
        hrValue = []
        timeValue = {}
        counter = 0
        hourNum = 0
        interval = 0
        t1 = ""
        t2 = ""
        dt1 = 0
        dt2 = 0
        list1 = []

        for row in csv_f:
            hrTime.append(row[0])
            hrValue.append(row[1])

        for i in range(len(hrTime)):
            list1.append(hrTime[i])
                         
        for ele in range(0, len(hrTime)):
            timeValue[list1[ele]] = hrValue[ele]

        interval = raw_input("Enter the number of hours you want to group the data in: ")

        ###print timeValue['12T20:35:48']

        for t in range(0, len(list1)):
            t1 = list1[counter]
            t2 = list1[t]

            dt1 = datetime.datetime.strptime(t1,'%Y-%m-%dT%H:%M:%SZ')
            dt2 = datetime.datetime.strptime(t2,'%Y-%m-%dT%H:%M:%SZ')

            if (int(dt2.timestamp() - dt1.timestamp()) <= int(interval*3600)):
                with open("hour" + str(hourNum) + ".csv", 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([timeValue[t2]])
            else:
                counter = t
                hourNum += 1

test_list2 = HeartRate(filename ='alexData.csv')
