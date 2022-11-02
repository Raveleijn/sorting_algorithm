#Importeert de benodigde library
import random

#genereert een random list
def RandomList(size=10000, minVal=1, maxVal=9999):
  #Maakt een gesorteerde list van de mogelijke waarden
  maxVal = max(size, maxVal)
  numbersLeft = list(range(minVal, maxVal+1))
  randList = []
  for i in range(size):
    #Kiest voor elk element in de randomlijst een random element uit de gesorteerde lijst en haalt deze weg, zodat er geen gedupliceerde elementen zijn
    randNumberIndex = random.randint(0, len(numbersLeft)-1)
    randList.append(numbersLeft[randNumberIndex])
    numbersLeft.pop(randNumberIndex)
  return randList

  