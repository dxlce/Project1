#NOTE: this is in Python 2, not Python 3
import csv

test_list1 = []
class HeartRate:
    def __init__(self, test_list):
      self.test_list = test_list

      test_read = open('filename.csv')
      csv_read = csv.reader(test_read)
      for row in csv_read:
        test_list.append(row[2])

      print test_list

    """def openFile(test_list):
      print "hi"
      test_read = open('filename.csv')
      csv_read = csv.reader(test_read)
      for row in csv_read:
        test_list.append((row[2]))
      

      print (test_list)"""

test_list2 = HeartRate(test_list1)
test_list2.__init__


 
