from bintreeFile import Bintree
from linkedQFile import LinkedQ 



def makechildren(ord, slutord, svenska, gamla, q):
    """ skapar alla barn till ett ord genom att byta ut en bokstav i taget"""

    alfabet = "abcdefghijlkmopqrstuvxyzåäö"
   

    for i in range(len(ord)): #For-loopen körs enligt antalet bokstäver i ordet
        for bokstav in alfabet:
            if bokstav != ord[i]: #Bokstaven i alfabetet ska inte matcha bokstaven i 
                nytt_ord = ord[:i] + bokstav + ord[i+1:] #Byter ut bokstaven i och behåller resten

                if nytt_ord in svenska and nytt_ord not in gamla:
                    gamla.put(nytt_ord)

                if nytt_ord == slutord:
                    print("Det finns en väg till", slutord)
                    return True #Hittade slutordet!
                q.enqueue(nytt_ord) #Lägg i kön                    
    return False #Hittade inte slutordet 









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
    q.enqueue(startord)

    #Huvudlisngan som skapar den snabbaste sökvägen
    hittad = False
    while not q.isEmpty():
        word = q.dequeue() #Tar det första ordet från kön

       

        if makechildren(word,slutord,svenska,gamla, q):
            hittad = True 
            break

    if not hittad:
            print("Det fanns ingen väg till ", slutord)
   



main()

         

















