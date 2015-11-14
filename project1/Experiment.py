import sys

def largest(list):
  #if len(list) == 0:
    #raise ValueError("Cannot call largest on empty list")
  #max = -sys.maxint # "smallest" possible int
  #max = 0
  max = list[0]
  for index in range(len(list)):
    if (list[index] > max):
      max = list[index]
  return max
  # print "i am done"
  # a = 10
  # a = a+1  
  # a = a+1  
  # a = a+1
  # a = a+1
  # a = a+1  
  # a = a+1
  # a = a+1 
  # a = a+1
  # a = a+1   
