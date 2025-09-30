from bintreeFile import Bintree

#Första trädet svenska ord (taget från canvas, labb 3)
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

#Andra trädet engelska ord
engelska = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engfil:
    for rad in engfil:
        ordet = rad.strip()
        if ordet in engelska: #Inget görs om raden är inlagt i engelska 
            continue
        else:
            engelska.put(ordet) #Lägg in i engelska trådet
            if ordet in svenska: #Om det även finns i svenska, ska det skrivas ut
                print(ordet, end= " ")
print("\n")
