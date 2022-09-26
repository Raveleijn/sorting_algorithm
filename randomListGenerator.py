import random
def randomList(size, min, max):
  numbersLeft = list(range(min, max+1))
  randList = []
  for i in range(size):
    randNumber = random.randint(0, len(numbersLeft)-1)
    randList.append(numbersLeft[randNumber])
    numbersLeft.pop(randNumber)
  return randList

  