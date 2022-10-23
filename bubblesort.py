#hier gaan we bubble sort toepassen door eerst alles te definiëren in een array en de lengte te definiëren
def bubbleSort(arr):
  LengteArray = len(arr)
  for i in range(LengteArray-1): #hier zorgen we dat alle getallen van de lijst in de array worden gezet
    wissel = False
    for j in range(0, LengteArray-i-1): #in de volgende stappen draaien we de getallen in de array om en is wissel dus true als rechts lager is dan links
      if arr[j] > arr[j + 1]:
        wissel = True
        arr[j], arr[j + 1] = arr[j + 1],  arr[j]
    if not wissel: #als hij een keer de lijst door is gegaan en geen wissels meer vindt dan returnt hij de array en krijg je de gesorteerde lijst terug
      return arr
  return arr
