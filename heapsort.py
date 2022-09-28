import math

from randomListGenerator import *


def Heapify(list):
  for i in range(len(list)):
    Sieve(list, len(list)-i-1, len(list))
  return(list)


def Sieve(list, index, length):
  parent = list[index]
  children = 0
  if length > 2*index+1:
    child1 = list[2*index+1]
    children += 1
  if length > 2*index+2:
    child2 = list[2*index+2]
    children += 1

  if children == 1:
    if child1>parent:
      list[index], list[2*index+1] = list[2*index+1], list[index]
      Sieve(list, 2*index+1, length)

  if children == 2:
    if child1>child2:
      if child1>parent:
        list[index], list[2*index+1] = list[2*index+1], list[index]
        Sieve(list, 2*index+1, length)
    else:
      if child2>parent:
        list[index], list[2*index+2] = list[2*index+2], list[index]
        Sieve(list, 2*index+2, length)
  return list

def SortHeap(heap):
  lengthHeap = len(heap)
  while lengthHeap != 0:
    heap[lengthHeap-1], heap[0] = heap[0], heap[lengthHeap-1]
    lengthHeap -= 1
    Sieve(heap, 0, lengthHeap)
  return heap

def TestHeap(heap):
  correct = True
  for i in range(len(heap)):
    if len(heap)>2*i+1:
      if heap[i]<heap[2*i+1]:
        correct = False
        break;
    if len(heap)>2*i+2:
      if heap[i]<heap[2*i+2]:
        correct = False
        break
  return correct

def TestSorted(list):
  sorted = True
  for i in range(len(list)-1):
    if list[i]>list[i+1]:
      sorted = False
      break
  return sorted
    

for i in range(100):
  randoml = randomList(100,0,99)
  Heapify(randoml)
  SortHeap(randoml)
  print(TestSorted(randoml))


  
      
      
    
    
