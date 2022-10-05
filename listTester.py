from randomListGenerator import *
from NearlySorted import *
from heapsort import *
from bubblesort import *
from MergeSort import *

sortType  = input('What sorting algorithm do you want to use? (heapsort, bubblesort, mergesort) \n ')
listType  = input('What list type do you want to use? (random, nearly sorted, inversed) \n ')
length = str(input('What length? \n'))

listDict = {'random': RandomList,
            'nearly sorted': NearlySorted,
            'inversed': invertedLijst} 

list = listDict['listType'](length)


if sort == 'heapsort':
  for i in range(1):
    print(list)
    Heapify(list)
    print(list)
    SortHeap(list)
    print(list)
    print(str(i)+': '+str(TestSorted(list)))
if sort == 'bubblesort':
  lijst = invertedLijst(10000)
  print(lijst)
  bubbleSort(lijst)
  print(lijst)
  print(TestSorted(lijst))
  
