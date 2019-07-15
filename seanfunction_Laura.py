#NOTE: this is in Python 2, not Python 3
import csv
import os.path
from os import path

test_list1 = []


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
    def __init__(self, age, gender, filename):
      weight = 0
      ### Sean:
      ### csv.reader() is a  better solution, but I'll do this quickly
      ### Feel free to fix / improve.

      if (path.exists('calories.csv')):
          pass

      else:
          with open('calories.csv', 'wb')as csvfile:
              filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
              filewriter.writerow(['Polar Calories', 'Formula Calories'])
              
      dataFromFile = open(filename).readlines()

      dataKeys = dataFromFile[0].strip().split(',')
      dataValues = dataFromFile[1].strip().split(',')

      polarPairs = {key:dataValues[i] for i, key in enumerate(dataKeys)}
      weight = float((polarPairs['Weight (kg)']))
      
      polarCalories = float(polarPairs['Calories'])
      print "Calories burned (polar) = ", polarPairs['Calories']

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
          self.averageHeartRate(polarCalories, weight, age, gender)
          

    def averageHeartRate(self, polarCalories, weight, age, gender):
      ### returns a float to two decimals of the average heart rate during
      ### the effort
      ### how does is compare to the Polar calculated value
      max_heart_rate = 220 - int(age)
      min_HR = max_heart_rate * 0.64
      max_HR = max_heart_rate * 0.89

      heartrate1 = map(int, self.heartrate)
      divide = len(heartrate1)
      sum1 = 0
      
      for i in range(divide):
          sum1 += heartrate1[i]
          
      average = float(sum1)/divide
      average = round(average, 2)

      if ((average >= min_HR) and (average <= max_HR)):
          average = float(sum1)/divide
          average = round(average, 2)
          print average
          self.caloriesBurned(average, polarCalories, weight, age, gender)
          
      else:
          print ("Invalid range of heartrate.")

    def maxHeartRate():
      ### returns a float to two decimals of the maximum heart rate during
      ### the effort
      ### how does is compare to the Polar calculated value
      pass

    def minHeartRate():
      ### returns a float to two decimals of the minimum heart rate during
      ### the effort
      ### how does is compare to the Polar calculated value
      pass


    def caloriesBurned(self, average, polarCalories, weight, age, gender):
      ### returns the number of calories burned durring the effort
      ### here is a simple formula:
      ### Male: Calories/min = (-55.0969 + (0.6309 * Heart Rate) + (0.1988 * Weight) + (0.2017 * Age)) / 4.184
      ### Female: Calories/min = (-20.4022 + (0.4472 * Heart Rate) - (0.1263 * Weight) + (0.074 * Age)) / 4.184 
      ### how does is compare to the Polar calculated value

      if (gender.lower() == 'male'):
          heartRate = 0.6309 * average
          weightCal = 0.1988 * (weight)
          caloriesBurned = (-55.0969 + heartRate + weightCal + (0.2017 * float(age)))
          print "Formula: " + str(caloriesBurned)

          with open('calories.csv', 'ab') as csvfile:
              filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
              filewriter.writerow([str(polarCalories), str(caloriesBurned)])

      elif (gender.lower() == 'female'):
          heartRate = 0.4472 * average
          weightCal = 0.1263 * (weight)
          caloriesBurned = (-20.4022 + heartRate - weightCal + (0.074 * float(age)))
          print "Formula: " + str(caloriesBurned)

          with open('calories.csv', 'ab') as csvfile:
              filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
              filewriter.writerow([str(polarCalories), str(caloriesBurned)])

age = (raw_input("Please enter your age: "))
gender = (raw_input("Please enter your gender: "))
filename = (raw_input("Please enter the filename: "))
file_input_prompt = "File does not exist, please re-enter file name. Type 'q' to exit: "

filename = checkFile(filename)
          
calorieCount = HeartRate(age, gender, filename)
