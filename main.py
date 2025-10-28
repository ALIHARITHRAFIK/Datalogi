from bintreeFile import Bintree
from linkedQFile import LinkedQ 

class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent
        
#Förklara denn del mer, finns i canvas, den används dock inte i koden direkt
class SolutionFound (Exception):
    pass


def writechain(node): #Skriver ut kedjan från startord till slutord rekursivt
    if node.parent is not None:
        writechain(node.parent) #Gå till föräldern först
    print(node.word) #skriv ut ordet 


def makechildren(nod, slutord, svenska, gamla, q):
    """ skapar alla barn till ett ord genom att byta ut en bokstav i taget"""
    ord = nod.word

    alfabet = "abcdefghijlkmopqrstuvxyzåäö"
   

    for i in range(len(ord)): #For-loopen körs enligt antalet bokstäver i ordet
        for bokstav in alfabet:
            if bokstav != ord[i]: #Bokstaven i alfabetet ska inte matcha bokstaven i 
                nytt_ord = ord[:i] + bokstav + ord[i+1:] #Byter ut bokstaven i och behåller resten

                if nytt_ord in svenska and nytt_ord not in gamla:
                    gamla.put(nytt_ord)

                    #Skapa ParentNode
                    barn_nod = ParentNode(nytt_ord, nod)

                    if nytt_ord == slutord:
                        writechain(barn_nod)
                        return True #Retunera True när hittad
                    
                    q.enqueue(barn_nod)

    return False #Retunera False om inte hittad


     




def main():
    #Läser in ordlistan
    svenska = Bintree()

    with open("word3.txt", "r", encoding = "utf-8") as f:
          for line in f:
              word = line.strip().lower()
              if len(word) == 3: #Bara tre bokstavsord
                  svenska.put(word)
    print("Ordlistan är inläst")

    #Fråga efter startord och slutord
    startord = input("Ange startord: ").strip().lower()
    slutord = input("Ange slutord: ").strip().lower()

    #Kontrollera att orden finns i ordlistan
    if startord not in svenska:
          print("Detta startord finns inte")
          return
    if slutord not in svenska:
          print("Detta slutford finns inte")
          return
    
    #Skapa trädet för gamla ord (dumbarn)
    gamla = Bintree()
    gamla.put(startord) #startordet är redan "besökt"


    #För att hitta snabbaste vägen

    #Skapa kön och lägg in startordet
    q = LinkedQ()
    startnod = ParentNode(startord) #skapa ParentNode för startord
    q.enqueue(startnod)

    hittad = False

    #Huvudlisngan som skapar den snabbaste sökvägen
    while not q.isEmpty():
        nod = q.dequeue()

        

        if makechildren(nod,slutord,svenska,gamla, q):
            hittad = True 
            break

    if not hittad:
            print("Det fanns ingen väg till ", slutord)





main()

         
















