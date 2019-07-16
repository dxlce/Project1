#NOTE: this is in Python 2, not Python 3
#modified code so it can verify if the file exists or not
test_list1 = []

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
      weight = 0
      ### Sean:
      ### csv.reader() is a  better solution, but I'll do this quickly
      ### Feel free to fix / improve.
              
      dataFromFile = open(filename).readlines()

      dataKeys = dataFromFile[0].strip().split(',')
      dataValues = dataFromFile[1].strip().split(',')

      polarPairs = {key:dataValues[i] for i, key in enumerate(dataKeys)}
      weight = float((polarPairs['Weight (kg)']))

      
      polarCalories = float(polarPairs['Calories'])

      my_time = polarPairs['Duration']
      factors = (60, 1, 1/60)
      duration = sum(i*j for i, j in zip(map(int, my_time.split(':')), factors))
      self.duration = duration
      ###print str(duration)
      ###print "Calories burned (polar) = ", polarPairs['Calories']

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
              if count < 3:
                  count += 1
                  continue
                      
              else:
                  heartrate.append(row[2])

          heartrate = map(int, heartrate)
          self.averageHeartRate(workingHR, polarCalories, weight, age, gender, duration)
          

    def averageHeartRate(self, workingHR, polarCalories, weight, age, gender, duration):
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
          self.caloriesBurned(average, polarCalories, weight, age, gender, duration)
          pass

    def maxHeartRate(self):
      ###returns the maximum heart rate 
      ### call with initialized object
      heartrate1 = map(int, self.heartrate)
      maxHR = 0

      for i in range(len(heartrate1)):
          if heartrate1[i] > maxHR:
              maxHR = heartrate1[i]

      return maxHR

    def minHeartRate():
      ### returns the minimum heart rate 
      ### call with initialized object
      heartrate1 = map(int, self.heartrate)
      minHR = 999

      for i in range(len(heartrate1)):
          if heartrate1[i] < minHR:
              minHR = heartrate1[i]

      return minHR

    def caloriesBurned(self, average, polarCalories, weight, age, gender, duration):
      ### returns the number of calories burned durring the effort
      ### here is a simple formula:
      ### Male: Calories/min = (-55.0969 + (0.6309 * Heart Rate) + (0.1988 * Weight) + (0.2017 * Age)) / 4.184
      ### Female: Calories/min = (-20.4022 + (0.4472 * Heart Rate) - (0.1263 * Weight) + (0.074 * Age)) / 4.184 
      ### how does is compare to the Polar calculated value
      printAgeGender = 0
      if (gender.lower() == 'male'):
          heartRate = 0.6309 * average
          weightCal = 0.1988 * (weight)
          caloriesBurned = (-55.0969 + heartRate + weightCal + (0.2017 * float(age)))/4.184
          print "Formula: " + str(round(caloriesBurned*duration, 1))
          print "Polar: " + str(polarCalories)
          
          with open(storeInfo + ".csv", 'ab') as csvfile:
              filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
              if (printAgeGender == 0):
                  filewriter.writerow([str(polarCalories), str(round(caloriesBurned*duration, 1)),'' ,age, gender])
                  printAgeGender = 1
              else:
                  filewriter.writerow([str(polarCalories), str(round(caloriesBurned*duration, 1))])


      elif (gender.lower() == 'female'):
          heartRate = 0.4472 * average
          weightCal = 0.1263 * (weight)
          caloriesBurned = (-20.4022 + heartRate - weightCal + (0.074 * float(age)))/4.184
          print "Formula: " + str(round(caloriesBurned*duration, 1))
          print "Polar: " + str(polarCalories)

          with open(storeInfo + ".csv", 'ab') as csvfile:
              filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
              if (printAgeGender == 0):
                  filewriter.writerow([str(polarCalories), str(round(caloriesBurned*duration, 1)),'' ,age, gender])
                  printAgeGender = 1
              else:
                  filewriter.writerow([str(polarCalories), str(round(caloriesBurned*duration, 1))])

#asks for user age, gender, and filename (they need to put in the filetype (ie. (name).csv))
age = 0
gender = ""
proceed = "True"
workingHR = 0
file_input_prompt = "File does not exist, please re-enter file name. Type 'q' to exit: "

          
storeInfo = raw_input("Name the file you want to write the calories info inside of: ")

if not path.exists(storeInfo):
    with open(storeInfo + ".csv", 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['polarCals', 'formCals', '', 'age', 'gender'])

while (proceed == "True" or proceed == "Yes"):
    ###while (age <= 0):
    age = (raw_input("Please enter your age: "))
    workingHR = int(0.64 * (220 - int(age)))
    ###while (gender.lower() != 'male' and gender.lower != 'female'):
    gender = (raw_input("Please enter your gender: "))
    
    filename = (raw_input("Please enter the filename: "))
    filename = checkFile(filename)
    
    calorieCount = HeartRate(workingHR, age, gender, filename)

    proceed = raw_input("Enter \"Yes\" to keep filling in the new csv file: ")
