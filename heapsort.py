import math
from randomListGenerator import *

#Plaatst een element in de lijst naar de juiste plek volgens de heap-regels
def Sieve(list, index, length):
  #Vindt de waarden van de node die we willen zeven (de parent) en de children van de node.
  parent = list[index]
  children = 0
  if length > 2*index+1:
    child1 = list[2*index+1]
    children += 1
  if length > 2*index+2:
    child2 = list[2*index+2]
    children += 1

  #Doet een zeefstap afhankelijk van de hoeveelheid children en voert de Sieve functie uit op de list en op de nieuwe plek van de parent-waarde.
  
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

#Maakt de volgorde van een list een heap
def Heapify(list):
  for i in range(len(list)):
    Sieve(list, len(list)-i-1, len(list))
  return(list)

#Deze functie sorteert een heap
def SortHeap(heap):
  lengthHeap = len(heap)
  while lengthHeap != 0:
    heap[lengthHeap-1], heap[0] = heap[0], heap[lengthHeap-1]
    lengthHeap -= 1
    Sieve(heap, 0, lengthHeap)
  return heap

#De functie die de Heapify en Sortheap functies samenneemt
def HeapSort(list):
  Heapify(list)
  SortHeap(list)
  return list
    

