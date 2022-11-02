#Importeren van benodigde libraries en functies van andere files
from randomListGenerator import *
from NearlySorted import *
from heapsort import *
from bubblesort import *
from MergeSort import *
from InvertedLijst import *
import time
import tracemalloc


#Test of een lijst gesorteerd is
def TestSorted(list):
  sorted = True
  for i in range(len(list)-1):
    if list[i]>list[i+1]:
      sorted = False
      break
  return sorted

#Functie die input krijgt die aan een specifieke conditie voldoet
def inputCorrect(inputQuestion, secondQuestion, Condition):
  answer = input(inputQuestion)
  inputCorrect = Condition(answer)
  while not inputCorrect:
    answer = input(secondQuestion)
    inputCorrect = Condition(answer)
  return answer   


#De vragen over welk sorting algorithm, welk lijsttype en welke lijstlengte je wilt
sortType = inputCorrect('What sorting algorithm do you want to use? (heapsort, bubblesort or mergesort) \n', 'Please enter heapsort, bubblesort or mergesort \n', lambda a : a in ['heapsort', 'bubblesort', 'mergesort'])

listType = inputCorrect('What list type do you want to use? (random, nearly sorted or inversed) \n', 'Please enter random, nearly sorted or inversed \n', lambda a : a in ['random', 'nearly sorted', 'inversed'])

length = int(inputCorrect('What length should the list have? \n', 'Please input a non negative integer \n', lambda a : a.isdigit()))

times = int(inputCorrect('How many times do you want to repeat this algorithm? \n', 'Please input a non negative integer \n', lambda a : a.isdigit()))

#Het selecteren van de bijbehorende functies
sortDict = {'heapsort': HeapSort,
            'bubblesort': bubbleSort,
            'mergesort': mergesort}

listDict = {'random': RandomList,
            'nearly sorted': NearlySorted,
            'inversed': invertedLijst} 


listGen = listDict[listType]
sortFunc = sortDict[sortType]

#De functie die een list genereert met de gegeven generatorfunctie, deze sorteert met de gegeven sorteerfunctie

def TestAlgorithm(listGen, sortFunc):
  list = listGen(length)
  #print(list)
  print("Dit is de lijst die u opriep")

  begintijd = time.time()
  tracemalloc.start()

  list = sortFunc(list)
  eindtijd = time.time()
  memory = tracemalloc.get_traced_memory()
  tracemalloc.stop()

  #print(list)
  print("Dit is de gesorteerde lijst")
  print('Is de lijst gesorteerd?: {}'.format(TestSorted(list)))

  tijdsduur = eindtijd -  begintijd
  print("Het duurde {} milliseconden en koste maximaal {} bytes aan geheugen!".format(tijdsduur*1000, memory[1]))
  return tijdsduur, memory[1]


#hier wordt de hiervoor gedefinieerde functie uitgevoerd
totTijdsduur = 0
totGeheugen = 0
for i in range(times):
  tijdsduur, geheugen = TestAlgorithm(listGen, sortFunc)
  totTijdsduur += tijdsduur
  totGeheugen += geheugen
print('De gemiddelde tijdsduur was {} milliseconden en het gemiddelde maximale geheugengebruik was {} bytes.'.format(totTijdsduur*1000/times, totGeheugen/times))
  