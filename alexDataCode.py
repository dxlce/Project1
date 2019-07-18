#NOTE: this is in Python 2, not Python 3

"""

CODE CHANGED TO ONLY WORK FOR THE NEW FILES CREATED PER HOUR FROM ALEX'S DATA

"""

test_list1 = []

import os
from os import path
import csv
from operator import mul

def checkFile(filename):
    while (True):
        if (filename == 'q'):
            print "Ok bye"
            exit()
    
        if (".csv" in filename):
            if (path.exists(filename)):
                return filename
                break
            else:
                filename = (raw_input(file_input_prompt))
        elif ("." in filename):
            if (filename.endswith(".")):
                filename = filename + "csv"
                if (path.exists(filename)):
                    return filename
                    break
                else:
                    filename =(raw_input(file_input_prompt))
                
            else:
                filename = (raw_input("File type is invalid, please re-enter file name: "))
            
        else:
            filename = filename + ".csv"
            if (path.exists(filename)):
                return filename
                break
            else:
                filename =(raw_input(file_input_prompt))
    
class HeartRate:
    def __init__(self, workingHR, age, gender, filename):
      weight = 82

      dataFromFile = open(filename).readlines()
      
      heartrate = []
      self.heartrate = heartrate
      self.age = age
      self.gender = gender
      ### Sean:
      ### Now, get the heartrate list from the file.
      #Laura:
      #I have to modify this later so it isn't hard coding
      #get heartrate into a list 
      with open(filename, 'r') as file:
          count = 0
          csv_read = csv.reader((open(filename)))

          for row in csv_read:
                  heartrate.append(row[0])

          heartrate = map(int, heartrate)
          self.averageHeartRate(workingHR, weight, age, gender)
          

    def averageHeartRate(self, workingHR, weight, age, gender):
      ### returns a float to two decimals of the average heart rate during
      ### the effort
      ### how does is compare to the Polar calculated value
      heartrate1 = map(int, self.heartrate)
      validRange = []

      sum1 = 0

      for i in range(len(heartrate1)):
          if (heartrate1[i] >= workingHR): 
              validRange.append(heartrate1[i])

      divide = len(validRange)

      if (divide == 0):
          print "The heartrates given are too low"
      else:
          for i in range(divide):
              sum1 += validRange[i]
      
          average = float(sum1)/divide
          average = round(average, 2)
          self.caloriesBurned(average, weight, age, gender)
          pass

  
    def caloriesBurned(self, average, weight, age, gender):
      ### returns the number of calories burned durring the effort
      ### here is a simple formula:
      ### Male: Calories/min = (-55.0969 + (0.6309 * Heart Rate) + (0.1988 * Weight) + (0.2017 * Age)) / 4.184
      ### Female: Calories/min = (-20.4022 + (0.4472 * Heart Rate) - (0.1263 * Weight) + (0.074 * Age)) / 4.184 
      ### how does is compare to the Polar calculated value
      printAgeGender = 0
      counter = 0
      if (gender.lower() == 'male'):
          heartRate = 0.6309 * average
          weightCal = 0.1988 * (weight)
          caloriesBurned = (-55.0969 + heartRate + weightCal + (0.2017 * float(age)))/5.56472
          print "Formula: " + str(round(caloriesBurned*60, 1))
          
          with open(storeInfo + ".csv", 'ab') as csvfile:
              filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
              if (printAgeGender == 0):
                  counter += 1
                  filewriter.writerow([str(round(caloriesBurned*60, 1)), counter])
                  printAgeGender = 1
              else:
                  filewriter.writerow([str(round(caloriesBurned*60, 1)), counter])

#asks for user age, gender, and filename (they need to put in the filetype (ie. (name).csv))
age = 0
gender = ""
###proceed = "True"
workingHR = 0
file_input_prompt = "File does not exist, please re-enter file name. Type 'q' to exit: "

          
storeInfo = raw_input("Name the file you want to write the calories info inside of: ")

if not path.exists(storeInfo):
    with open(storeInfo + ".csv", 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['cals', 'hour'])

dataFiles = next(os.walk('.'))[2]
del dataFiles[0]
del dataFiles[0]
print dataFiles

age = (raw_input("Please enter your age: "))
workingHR = int(0.64 * (80 - int(age)))
gender = (raw_input("Please enter your gender: "))

for i in range(0, len(dataFiles)-1):
    filename = dataFiles[i]
    calorieCount = HeartRate(workingHR, age, gender, filename)

    ### proceed = raw_input("Enter \"Yes\" to keep filling in the new csv file: ")
