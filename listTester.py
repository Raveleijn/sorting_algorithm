from randomListGenerator import *
from heapsort import *

for i in range(1):
  randoml = randomList(10,0,9)
  print(randoml)
  Heapify(randoml)
  print(randoml)
  SortHeap(randoml)
  print(randoml)
  print(str(i)+': '+str(TestSorted(randoml)))