import datetime
from time import time
import os
from os import path
import csv

class HeartRate:
    def __init__(self, age, gender, weight, filename):

        #too many variables to count
        f = open(filename)
        csv_f = csv.reader(f)
        next(csv_f)
        hrTime = []
        hrValue = []
        timeValue = {}
        counter = 0
        counter2 = 0
        hourNum = 0
        t1 = ""
        t2 = ""
        dt1 = 0
        dt2 = 0
        list1 = []
        days = 0
        timelist = []
        calorieList = []
        hourNum2 = 0
        hrList = []
        max_HR = 220 - int(age)
        goodHRList = []
        finalHRList = []
        z = 0
        t_temp = 0
        HRdict = {}
        interval = 0
        tempValue = 0
        tempList = []
        dt4 = 0
        count2 = 1
        finalDict = {}
        p = 0
        count3600 = 0
        goodTime = []

        #get the time and heartrate from the file
        for row in csv_f:
            hrTime.append(row[0])
            hrValue.append(row[1])

        while z < len(hrValue):
            if ((float(hrValue[z]) < 70) and (float(hrValue[z]) > max_HR)):
                del hrValue[z:z+1:]
                del hrTime[z:z+1:]
                z+=1
            else:
                z+=1
        z = 0

        #append the times into list1
        for i in range(len(hrTime)):
            list1.append(hrTime[i])

        #make a dictionary called timeValue, pretty much a dictionary form of the Alex file.
        for ele in range(0, len(hrTime)):
            timeValue[list1[ele]] = hrValue[ele]

        
        #adding things to list
        
        for t in range(0, len(list1)):
            #t1: the time at the beginning, stays "still. t2 increments each time
            t1 = list1[counter]
            t2 = list1[t]
            
            #time before t2
            temp = list1[t-1]

            #datetime form of the times
            dt1 = datetime.datetime.strptime(t1,'%Y-%m-%dT%H:%M:%SZ')
            dt2 = datetime.datetime.strptime(t2,'%Y-%m-%dT%H:%M:%SZ')
            int_dt2 = int(dt2.timestamp())
            dt6 = str(datetime.datetime.fromtimestamp(int_dt2))
            
            dttemp = datetime.datetime.strptime(temp, '%Y-%m-%dT%H:%M:%SZ')
            
            #if t-1 is greater than zero (making sure index does not go out of range)
            if (t-1 >= 0):
                #if the time gap does not exceed 3600 and the gap is no more than two seconds, append heartrates to "goodHRList"
                if (int(dt2.timestamp() - dt1.timestamp()) <= 3600) and (int(dt2.timestamp()-dttemp.timestamp()) < 2):
                    goodHRList.append(timeValue[t2])
                    goodTime.append(dt2)
                   

                #if the gap is larger than 2 seconds
                elif ((int(dt2.timestamp()-dttemp.timestamp()) > 2)):
                   
                    int_ttemp = int(dttemp.timestamp())
                        
                        

                    #taking the two values of the HRs on the "gap"
                    HRdict[t2] = timeValue[t2]
                    HRdict[temp] = timeValue[temp]

                    #calculate the interval to increment
                    interval = (float(HRdict[t2]) - float(HRdict[temp]))/(float(dt2.timestamp() - dttemp.timestamp()))

                    #appending to tempList by adding the interval from the previous value.
                    for g in range(int(dt2.timestamp()-dttemp.timestamp())):
                        
                        #if the temp list is empty, grab the value from the goodHRList
                        temp2 = goodHRList[-1]
                        tempValue = (float(temp2) + (interval))
                        goodHRList.append(tempValue)

                        
                        dttemp2 = str(datetime.datetime.fromtimestamp(int_ttemp))
                        goodTime.append(dttemp2)
                        int_ttemp += 1

                        #if the temp list isn't empty, grab the previous value.
                        
                        """temp2 = finalDict[dt7]
                        tempValue = (float(temp2) + (interval))
                        dt6 = int_dt2 + count2
                        dt7 = str(datetime.datetime.fromtimestamp(dt6))
                        finalDict[dt7] = tempValue"""
                    
                    #count2 = 1   
                    #stick finalHRlist into goodHRlist

                    #clean out bad heartrates
                    """while z < (len(goodHRList)):
                        if ((float(goodHRList[z]) < 70) and (float(goodHRList[z]) > max_HR)):
                            del finalHRList[z:z+1:]
                            z+=1
                        else:
                            z+=1
                    z = 0

                    #cleans out more bad heartrates
                    while p < (len(tempList)):
                        if ((float(tempList[p]) < 70) and (float(goodHRList[p]) > max_HR)):
                            del tempList[p:p+1:]
                            p+=1
                        else:
                            p+=1
                    p = 0"""

                    #write in files - maybe i can put it in a dictionary
                    

                    """for a in range(len(tempList)):
                        dt4 = ((int(dt3.timestamp()) + count2))
                        dt5 = str(datetime.datetime.fromtimestamp(dt4))
                        finalDict[dt5] = tempList[a]
                        count2+=1"""
                        
                    #t_temp+=count2
                    counter = t
                    count2 = 1
                    
                    
                else:
                    goodHRList.append(timeValue[t2])

                
        print (len(goodHRList))
        print (len(goodTime))
        for y in range(0, len(goodTime)):
            t3 = goodTime[y]
            finalDict[t3] = goodHRList[y]
            
                    

        for key in finalDict:
            
            if (count3600 < 3599):
                
                with open("hour" + str(hourNum) + ".csv", 'a', newline = "") as csvfile:
                    filewriter = csv.writer(csvfile, delimiter = ',', quotechar = "|", quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([key, finalDict[key]])
                count3600+=1
            else:
                
                hourNum+=1
                with open("hour" + str(hourNum) + ".csv", 'a', newline = "") as csvfile:
                    filewriter = csv.writer(csvfile, delimiter = ',', quotechar = "|", quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([key, finalDict[key]])
                count3600 = 0 
                                    

        """for k in range(0, hourNum):
            g = open("hour" + str(k) + ".csv")
            csv_g = csv.reader(g)

            for row in csv_g:
                timelist.append(row[0])
                hrList.append(row[1])

            for l in range(len(timelist)):
                if l == 0:
                    continue
                t3 = timelist[l]
                t4 = timelist[l-1]
            
                if (float(t3)-float(t4) == 1):
                    with open("hour2_" + str(hourNum2) + ".csv", 'a', newline = "") as csvfile:
                        filewriter = csv.writer(csvfile, delimiter = ',', quotechar = "|", quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow([str(hrList[l])])
                else:
                    hourNum2 += 1
                    with open("hour" + str(hourNum2) + ".csv", 'a', newline = "") as csvfile:
                        filewriter = csv.writer(csvfile, delimiter = ',', quotechar = "|", quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow([hrList[l]])
            hourNum2+=1
            del timelist[0::]
            del hrList[0::]"""

                
        for m in range(hourNum):
            filename = "hour" + str(m) + ".csv"
            self.averageHeartRate(calorieList, age, gender, weight, filename, m)

    def averageHeartRate(self, calorieList, age, gender, weight, filename, m):
        
        sum1 = 0
        length_csv_list = []
        average = 0
        length_csv = 0

        f = open(filename)
        csv_f = csv.reader(f)
        
        for row in csv_f:
            length_csv_list.append(row[1])

        length_csv = len(length_csv_list)

        for i in range(length_csv):
            sum1+=float(length_csv_list[i])

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



