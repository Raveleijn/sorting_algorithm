from random import randrange

def invertedLijst(length):
  InvertedLijst = []
  x = 0
  while len(InvertedLijst) < length:
    x += randrange(1, 10)
    InvertedLijst.append( 6*length - x)
  return InvertedLijst