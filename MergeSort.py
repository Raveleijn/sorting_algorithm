#we gaan hier een algoritme maken dat eenllijst sorteert met de methode van merge sort

#Hier maken we gebruik van een recursieve functie om te blijven spitten en daarna mergen totdat de lijst helemaal gesorteerd is


def mergesort(List):
    if len(List) == 1:
        return List
    ListA, ListB = splitlist(List)
    ListASorted = mergesort(ListA)
    ListBSorted = mergesort(ListB)
    ListSorted = merge(ListASorted, ListBSorted)
    return ListSorted


#Hier wordt de lijst gesplitst in twee lijsten met ieder de helft van de getallen
def splitlist(list):
    i = 0
    ListA = []
    ListB = []
    while i < len(list) / 2:
        ListA.append(list[i])
        i += 1
    while i >= (len(list) / 2) and i < len(list):
        ListB.append(list[i])
        i += 1
    return ListA, ListB


#Hier voegen we twee lijsten samen door steeds het eerste getal van beide lijsten met elkaar te vergelijken en de laagste aan een derde lijst toe te voegen, waarna ik dat getal verwijder uit de eerste lijst en er weer een nieuw eerste getal ontstaat.
def merge(ListASorted, ListBSorted):
    ListSorted = []
    while (len(ListASorted) != 0) and (len(ListBSorted) != 0):
        if ListASorted[0] <= ListBSorted[0]:
            ListSorted.append(ListASorted[0])
            ListASorted.pop(0)
        elif ListASorted[0] > ListBSorted[0]:
            ListSorted.append(ListBSorted[0])
            ListBSorted.pop(0)
    while (len(ListASorted) == 0) ^ (len(ListBSorted) == 0):
        while (len(ListASorted) == 0) and (len(ListBSorted) != 0):
            ListSorted.append(ListBSorted[0])
            ListBSorted.pop(0)
        while (len(ListBSorted) == 0) and (len(ListASorted) != 0):
            ListSorted.append(ListASorted[0])
            ListASorted.pop(0)
    return ListSorted
