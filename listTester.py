from randomListGenerator import *
from NearlySorted import *
from heapsort import *
from bubblesort import *
from MergeSort import *

sort  = input('heapsort, bubblesort, mergesort? ')
if sort == 'heapsort':
  for i in range(1):
    randoml = randomList(10,0,9)
    print(randoml)
    Heapify(randoml)
    print(randoml)
    print(randoml)
    print(str(i)+': '+str(TestSorted(randoml)))
if sort == 'bubblesort':
  lijst = invertedLijst(100)
  print(lijst)
  bubbleSort(lijst)
  print(lijst)
  print(TestSorted(lijst))
  
