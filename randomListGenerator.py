#import the random library
import random

def RandomList(size=10000, minVal=0, maxVal=9999):
  maxVal = max(size-1, maxVal)
  numbersLeft = list(range(minVal, maxVal+1))                      #creates a list of numbers to choose from
  randList = []                                              #the list we're going to add ranodm values to
  for i in range(size):
    randNumberIndex = random.randint(0, len(numbersLeft)-1)  #choose a random index for the new random number
    randList.append(numbersLeft[randNumberIndex])            #add the random number from numbersLeft
    numbersLeft.pop(randNumberIndex)                          #remove the random number from numbersLeft
  return randList

  