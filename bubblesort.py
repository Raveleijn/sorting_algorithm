from random import randrange

def invertedLijst(length):
  InvertedLijst = []
  x = 0
  while len(InvertedLijst) < length:
    x += randrange(1, 10)
    InvertedLijst.append( 6*length - x)
  return InvertedLijst


def bubbleSort(arr):
      LengteArray = len(arr)
      wissel = False
      for i in range(LengteArray-1):
          for j in range(0, LengteArray-i-1):
              if arr[j] > arr[j + 1]:
                  wissel = True
                  arr[j], arr[j + 1] = arr[j + 1],  arr[j]
         
          if not wissel:
            return arr

