from random import randrange

def invertedLijst(length): #de lenght van de lijst geef je aan bij het selecteren van welke lijst
  InvertedLijst = []
  x = 0
  while len(InvertedLijst) < length: #zorgt ervoor dat er precies zoveel getallen in de lijst zitten als aangegeven
    x += randrange(1, 10) #geeft een beetje variatie aan de getallen zodat het niet gewoon een reeks van precies aflopende getallen
    InvertedLijst.append( 6*length - x) #zorgt ervoor dat er genoeg getallen zijn om te genereren en vormt stap voor stap de aflopende lijst, als hier geen 6* stond was er namelijk lenght-x en zou je op negatieve resultaten uitkomen in je lijst
  return InvertedLijst #geeft je de inverted lijst terug
