from randomListGenerator import *
from NearlySorted import *
from heapsort import *
from bubblesort import *
from MergeSort import *
from InvertedLijst import *

sortType  = input('What sorting algorithm do you want to use? (heapsort, bubblesort, mergesort) \n')
listType  = input('What list type do you want to use? (random, nearly sorted, inversed) \n')
length = int(input('What length? \n'))

sortDict = {'heapsort': HeapSort,
            'bubblesort': bubbleSort,
            'mergesort': mergesort}

listDict = {'random': RandomList,
            'nearly sorted': NearlySorted,
            'inversed': invertedLijst} 

list = listDict[listType](length)
sortFunc = sortDict[sortType]

print(list)
list = sortFunc(list)
print(list)
print(TestSorted(list))

