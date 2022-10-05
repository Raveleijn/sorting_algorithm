#In deze file gaan we een lijst laten maken die bijna gesorteerd is 

from random import randrange

# in deze code voeg ik steeds een stijgend getal toe en een getal wat random rond dat getal zit, hierdoor is de lijst altijd bijna gesorteerd, want om het getal is het al geordend.

def NearlySorted(lengte):
  NearlySortedLijst = []
  Minimum = 9              #Het beginpunt van de lijst is 9, zodat de lijst geen getallen onder nul kan bevatten
  while len(NearlySortedLijst) < lengte:
    Minimum += randrange(1,10)
    NearlySortedLijst.append(Minimum)
    NearlySortedLijst.append(Minimum + randrange(-10,10))
  return NearlySortedLijst

