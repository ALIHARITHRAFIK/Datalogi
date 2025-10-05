from bintreeFile import Bintree

#Första trädet svenska ord (taget från canvas, labb 3)

from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")


#Andra trädet engelska ord'

engelska = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engfil:
    for rad in engfil:
        ord_lista = rad.split() #Dela upp raden i ord 
        for ord in ord_lista:
            ordet = ord.lower().strip('.,!?";:()[]') #Ta bort punktuation
            if ordet == "": #Skippa tomma strängar
                continue 
            if ordet in engelska: #ordet redan i engelska trädet, gör inget
                continue 
            else:      #Nytt engelska ord
                engelska.put(ordet) #Lägg till i engelska trädet
                if ordet in svenska: #Kolla om det också är svenskt 
                    print(ordet, end=" ")



