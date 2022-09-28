import math

from randomListGenerator import *

randoml = randomList(10,0,9)
print(randoml)

def Heapify(list):
  for i in range(len(list)):
    Sieve(list, len(list)-i-1)
  return(list)


def Sieve(list, index):
  element = list[index]
  if len(list)>2*index+1:
    if list[index]>list[2*index+1]:
      list[index], list[2*index+1] = list[2*index+1], list[index]
  
  if len(list)>2*index+2:
    if list[index]>list[2*index+2]:
      list[index], list[2*index+2] = list[2*index+2], list[index]
  
  if element != list[index]:
    if element == list[2*index+1]:
      Sieve(list, 2*index+1)
    else:
      Sieve(list, 2*index+2)

def SortHeap(heap):
  sortedList = []
  while len(heap) != 0:
    sortedList.append(heap[0])
    heap[0] = heap[-1]
    heap.pop(-1)
    if(len(heap) != 0):
      Sieve(heap, 0)
  return sortedList

heapTest = Heapify(randoml)
print(heapTest)
sortedTest = SortHeap(heapTest)
print(sortedTest)
      
      
    
    
