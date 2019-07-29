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
        counter = 0
        hourNum = 0
        t1 = ""
        t2 = ""
        dt1 = 0
        dt2 = 0
        list1 = []
        days = 0
        calorieList = []

        for row in csv_f:
            hrTime.append(row[0])
            hrValue.append(row[1])
            
        for i in range(len(hrTime)):
            list1.append(hrTime[i])
                         
        for ele in range(0, len(hrTime)):
            timeValue[list1[ele]] = hrValue[ele]

        ###print timeValue['12T20:35:48']

        for t in range(0, len(list1)):
            t1 = list1[counter]
            t2 = list1[t]

            dt1 = datetime.datetime.strptime(t1,'%Y-%m-%dT%H:%M:%SZ')
            dt2 = datetime.datetime.strptime(t2,'%Y-%m-%dT%H:%M:%SZ')

            

            if (int(dt2.timestamp() - dt1.timestamp()) <= 60):
                with open("minute" + str(hourNum) + ".csv", 'a', newline = "") as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([timeValue[t2]])
                                        
            else:
                counter = t
                hourNum += 1

        for m in range(hourNum):
            filename = "minute" + str(m) + ".csv"
            self.averageHeartRate(calorieList, age, gender, weight, filename, m)

    def averageHeartRate(self, calorieList, age, gender, weight, filename, m):
        sum1 = 0
        length_csv_list = []
        average = 0
        length_csv = 0

        f = open(filename)
        csv_f = csv.reader(f)
        
        for row in csv_f:
            length_csv_list.append(row[0])

        length_csv = len(length_csv_list)

        for i in range(length_csv):
            sum1+=int(length_csv_list[i])

        average = float(sum1)/length_csv
        calorieList.append(average)

        sum1 = 0
        del length_csv_list[0:length_csv]

        self.caloriesBurned(calorieList, age, gender, weight, m, length_csv)

    def caloriesBurned(self, calorieList, age, gender, weight, m, length_csv):
        caloriesBurnedList = []
        hours = []
        length_csv2 = []
        max_HR = 220 - int(age)
        caloriesBurned = 0

        min_HR = max_HR * 0.64
        for i in range(len(calorieList)):
            if (calorieList[i] < min_HR):
                caloriesBurned = 83
                caloriesBurnedList.append(caloriesBurned)
                hours.append(m)
                length_csv2.append(length_csv)
            else:
                
                heartRate = 0.6309 * calorieList[i]
                weightCal = 0.1988 * float(weight)
                caloriesBurned = ((-55.0969 + heartRate + weightCal + (0.2017 * float(age)))*60/4.184)
                caloriesBurnedList.append(caloriesBurned)
                hours.append(m)
                length_csv2.append(length_csv)
          
        if (path.exists("caloriesBurned.csv")):
            with open("caloriesBurned.csv", "a", newline = "") as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([hours[i], caloriesBurnedList[i], length_csv2[i]])

        else:
            with open("caloriesBurned.csv", "w", newline = "") as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([hours[i], caloriesBurnedList[i], length_csv2[i]])

        del calorieList[0:len(calorieList)]
            
                
        
             
age = (input("Please enter your age: "))
gender = (input("Please enter your gender: "))
weight = (input("Please enter your weight: "))
test_list2 = HeartRate(age, gender, weight, filename ='AlexHR1sec.csv')
