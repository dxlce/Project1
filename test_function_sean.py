#NOTE: this is in Python 2, not Python 3
import csv

test_list1 = []
class HeartRate:
    def __init__(self, filename='filename.csv'):


      ### Sean:
      ### csv.reader() is a  better solution, but I'll do this quickly
      ### Feel free to fix / improve.
      dataFromFile = open(filename).readlines()

      dataKeys = dataFromFile[0].strip().split(',')
      dataValues = dataFromFile[1].strip().split(',')

      polarPairs = {key:dataValues[i] for i,key in enumerate(dataKeys)} 

      print "Calories burned = ", polarPairs['Calories']

      self.heartrate = []
      ### Sean:
      ### Now, get the heartrate list from the file.  

    def averageHeartRate():
      ### returns a float to two decimals of the average heart rate during
      ### the effort
      ### how does is compare to the Polar calculated value
      pass

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


    def caloriesBurned(gender='female'):
      ### returns the number of calories burned durring the effort
      ### here is a simple formula:
      ### Male: Calories/min = (-55.0969 + (0.6309 * Heart Rate) + (0.1988 * Weight) + (0.2017 * Age)) / 4.184
      ### Female: Calories/min = (-20.4022 + (0.4472 * Heart Rate) - (0.1263 * Weight) + (0.074 * Age)) / 4.184 
      ### how does is compare to the Polar calculated value
      pass



test_list2 = HeartRate(filename='RayHao_Speedwalking.csv')



 
