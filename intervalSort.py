import datetime
from time import time
import os
from os import path
import csv

class HeartRate:
    def __init__(self, age, gender, weight, filename):

        f = open(filename)
        csv_f = csv.reader(f)
        next(csv_f)
        hrTime = []
        hrValue = []
        timeValue = {}
        timeValue2 = {}
        counter = 0
        splitter = 0
        intervalInput = ""
        interval = 0
        t1 = ""
        t2 = ""
        dt1 = 0
        dt2 = 0
        list1 = []
        hourNum = 0
        calorieList = []

        for row in csv_f:
            hrTime.append(row[0])
            hrValue.append(row[1])
                         
        for ele in range(0, len(hrTime)):
            timeValue[hrTime[ele]] = hrValue[ele]

        for t in range(0, len(hrTime)):
            t1 = hrTime[counter]
            t2 = hrTime[t]

            dt1 = datetime.datetime.strptime(t1,'%Y-%m-%dT%H:%M:%SZ')
            dt2 = datetime.datetime.strptime(t2,'%Y-%m-%dT%H:%M:%SZ')

            if (int(dt2.timestamp() - dt1.timestamp()) <= 3600):
                with open("hour" + str(hourNum) + ".csv", 'a', newline = "") as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([t2,timeValue[t2]])
                    ###filewriter.writerow([t2],[timeValue[t2]])

                    
            else:
                counter = t
                hourNum += 1

        intervalInput = input("Enter the maximum gap of time (sec) between datapoints")  
        interval = int(intervalInput)

        for hours in range(hourNum):
            r = open("hour" + str(hours) + ".csv")
            csv_r = csv.reader(r)
            counter = 0
            splitter = 0
            
            for rows in csv_r:
                hrTime.append(rows[0])
                hrValue.append(rows[1])

            for elem in range(len(hrTime)):
                timeValue2[hrTime[elem]] = hrValue[elem]

            for elems in range(len(hrTime)):
                t1 = hrTime[counter]
                t2 = hrTime[counter + 1]
                counter += 1
                
                dt1 = datetime.datetime.strptime(t1,'%Y-%m-%dT%H:%M:%SZ')
                dt2 = datetime.datetime.strptime(t2,'%Y-%m-%dT%H:%M:%SZ')

                if (int(dt2.timestamp() - dt1.timestamp()) <= interval):
                    with open("hour" + str(hours) + "_" + str(splitter) + ".csv", 'a', newline = "") as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow([timeValue2[hrTime[counter]]])
                else:
                    splitter += 1

            os.remove("hour" + str(hours) + ".csv")
            

age = (input("Please enter your age: "))
gender = (input("Please enter your gender: "))
weight = (input("Please enter your weight: "))
test_list2 = HeartRate(age, gender, weight, filename = 'alexData.csv')

    
