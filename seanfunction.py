#NOTE: this is in Python 2, not Python 3
"""This is the (very) inefficient version of the calorie calculation code. I still need to make it more efficient and include 
age + gender - Laura"""
import csv

test_list1 = []


class HeartRate:
    def __init__(self, filename='filename.csv'):
      weight = 0
      ### Sean:
      ### csv.reader() is a  better solution, but I'll do this quickly
      ### Feel free to fix / improve.
      dataFromFile = open(filename).readlines()

      dataKeys = dataFromFile[0].strip().split(',')
      dataValues = dataFromFile[1].strip().split(',')

      polarPairs = {key:dataValues[i] for i,key in enumerate(dataKeys)}
      print polarPairs
      weight = int(polarPairs['Weight (kg)'])
      print weight
      
      
      print "Calories burned = ", polarPairs['Calories']

      heartrate = []
      self.heartrate = heartrate
      ### Sean:
      ### Now, get the heartrate list from the file.
      #Laura:
      #I have to modify this later so it isn't hard coding :c
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
          self.averageHeartRate(weight)
          

    def averageHeartRate(self, weight):
      ### returns a float to two decimals of the average heart rate during
      ### the effort
      ### how does is compare to the Polar calculated value
      heartrate1 = map(int, self.heartrate)
      divide = len(heartrate1)
      sum1 = 0
      
      for i in range(divide):
          sum1 += heartrate1[i]

      average = float(sum1)/divide
      average = round(average, 2)
      self.caloriesBurned(average, weight)

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


    def caloriesBurned(self, average, weight):
      ### returns the number of calories burned durring the effort
      ### here is a simple formula:
      ### Male: Calories/min = (-55.0969 + (0.6309 * Heart Rate) + (0.1988 * Weight) + (0.2017 * Age)) / 4.184
      ### Female: Calories/min = (-20.4022 + (0.4472 * Heart Rate) - (0.1263 * Weight) + (0.074 * Age)) / 4.184 
      ### how does is compare to the Polar calculated value
      
      heartRate = 0.6309 * average
      weightStuff = 0.1988 * weight
      age = 16
      caloriesBurned = (-55.0969 + heartRate + weightStuff + (0.2017 * age))
      print caloriesBurned
          
          



test_list2 = HeartRate(filename='filename.csv')

