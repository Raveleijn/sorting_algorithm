#In deze file gaan we een lijst laten maken die bijna gesorteerd is 

from random import randrange

#Dit is het beginpunt van de lijst, zodat de lijst geen getallen onder nul kan bevatten
Minimum = 9

# in deze code voeg ik steeds een stijgend getal toe en een getal wat random rond dat getal zit, hierdoor is de lijst altijd bijna gesorteerd, want om het getal is het al geordend.
def NearlySorted(lengte):
  NearlySortedLijst = []
  Minimum = 9
  while len(NearlySortedLijst) < lengte:
    Minimum += randrange(1,10)
    NearlySortedLijst.append(Minimum)
    NearlySortedLijst.append(Minimum + randrange(-10,10))
    return NearlySortedLijst