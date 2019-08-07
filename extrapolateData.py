"""
put this code in a folder with the original alexHR1Sec data file and the files with data broken down into intervals of continuous data
example of what the folder should look like:

files in folder:

AlexHR1sec.csv
extrapolateData.py (this code)
hour0
hour1
hour2
hour3
...
hour24823
"""

import datetime
from time import time
import os
from os import path
import csv

class HeartRate:
    def __init__(self, filename):

        file1Date = ''
        file1Value = ''
        file2Date = ''
        file2Value = ''
        dt1 = 0
        dt2 = 0

        dataFiles = next(os.walk('.'))[2]
        del dataFiles[0]
        del dataFiles[0]
        print(str(dataFiles))
    

        for i in range(0, len(dataFiles) - 1):

            with open('hour' + str(i) + '.csv', 'r') as f1:
                for row in (list(csv.reader(f1))):
                    file1Date = row[0]
                    file1Value = row[1]
                    #the times should be formatted like '2018-11-04T11:19:40Z'

            with open('hour' + str(i+1) + '.csv', 'r') as f2:
                for row in (reversed(list(csv.reader(f2)))):
                    file2Date = row[0]
                    file2Value = row[1]
   
            dt1 = datetime.datetime.strptime(file1Date,'%Y-%m-%dT%H:%M:%SZ')
            dt2 = datetime.datetime.strptime(file2Date,'%Y-%m-%dT%H:%M:%SZ')

            #assuming time is plotted on x-axis and hr on y-axis

            slope = float((int(file2Value) - int(file1Value)) / (dt2.timestamp()- dt1.timestamp()))

            for m in range(0, int(dt2.timestamp() - dt1.timestamp())):
                print(str(round(int(file1Value) + float(slope)*int(m))))
                with open('extrapolate' + '_' + str(i) + '_' + str(i+1) + '.csv', 'a', newline = '') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([str(round(int(file1Value) + float(slope)*int(m)))])

test_list2 = HeartRate(filename ='AlexHR1sec.csv')
