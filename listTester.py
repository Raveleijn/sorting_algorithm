from randomListGenerator import *
from NearlySorted import *
from heapsort import *
from bubblesort import *
from MergeSort import *
from InvertedLijst import *
from datetime import datetime

def TestSorted(list):
  sorted = True
  for i in range(len(list)-1):
    if list[i]>list[i+1]:
      sorted = False
      break
  return sorted

def inputCorrect(inputQuestion, secondQuestion, Condition):
  answer = input(inputQuestion)
  inputCorrect = Condition(answer)
  while not inputCorrect:
    answer = input(secondQuestion)
    inputCorrect = Condition(answer)
  return answer   

sortType = inputCorrect('What sorting algorithm do you want to use? (heapsort, bubblesort or mergesort) \n', 'Please enter heapsort, bubblesort or mergesort \n', lambda a : a in ['heapsort', 'bubblesort', 'mergesort'])

listType = inputCorrect('What list type do you want to use? (random, nearly sorted or inversed) \n', 'Please enter random, nearly sorted or inversed \n', lambda a : a in ['random', 'nearly sorted', 'inversed'])

length = int(inputCorrect('What length should the list have? \n', 'Please input a non negative integer \n', lambda a : a.isdigit()))

sortDict = {'heapsort': HeapSort,
            'bubblesort': bubbleSort,
            'mergesort': mergesort}

listDict = {'random': RandomList,
            'nearly sorted': NearlySorted,
            'inversed': invertedLijst} 

list = listDict[listType](length)
sortFunc = sortDict[sortType]

begintijd = datetime.now()
print(list)
list = sortFunc(list)
print(list)
print(TestSorted(list))
eindtijd = datetime.now()
tijdsduur = eindtijd -  begintijd
print(tijdsduur)
