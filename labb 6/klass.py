import timeit

class Music():
    def __init__(self,track_id, song_id,artist,title): #Innitierar alla parametrar som kommer att användas i objekten (kolla om kommentaren är rätt)
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.title = title

    def __str__(self): #Retunerar en sträng med information om låtarna
        return "Track ID: " + self.track_id + "Song ID: " + self.song_id + "Artist: " + self.artist + "Title: " + self.title 
    
    def __lt__(self, other): #Jämför två artist namn beroende på vilken bokstav som kommer först
        return self.artist < other.artist
    



def readfile(filename): #Denna funktion är till för att läsa filen
    songs = []
    with open(filename,"r", encoding="utf-8") as file:
        for row in file:
            parts = row.split("<SEP>")
            lista_av_objekt = Music(parts[0], parts[1], parts[2], parts[3] )
            songs.append(lista_av_objekt)
    print("Antalet inlästa låtar: " + str(len(songs)))
    print("Första låten är: " + str(songs[0]))

    return songs



def linsok(lista,artist):
    for loop in lista: #Loopar igenom listan
        if loop.artist == artist: #Jämför artistnamn
            return loop #Retunerar artisten om vi hittar 
    return None #Annars retunera None

    



# ========== DESSA FUNKTIONER ÄR FRÅN AI (Claude AI)==========
# (Du får använda dessa direkt enligt uppgiften)

def binsok(sorterad_lista, artist):
    """
    Binärsökning: Kollar mitten av listan, jämför alfabetiskt med den artist vi söker.
    Om artisten vi söker kommer senare i alfabetet → sök uppåt (högre index).
    Om artisten vi söker kommer tidigare i alfabetet → sök nedåt (lägre index).
    Upprepar tills artisten hittas eller listan är slut..
    Denna kod är från Claude AI 
    """
    low = 0 #Börjar längst ner i listan
    high = len(sorterad_lista) - 1 #Slutar längst upp i listan
    
    while low <= high: #Loopar till den hittar artisten
        mid = (low + high) // 2 #Räknar ut mitten mellan low och high 
        if sorterad_lista[mid].artist == artist:
            return sorterad_lista[mid] #Om Artisten i mitten matchas så retuneras den
        elif sorterad_lista[mid].artist < artist: #Om artisen i mitten  för tidig i listan
            low = mid + 1 #Sök i den övre halvan 
        else:  #Om artisen  i mitten  är sen i listan
            high = mid - 1 #Sök i den nedre halvan
    return None #Om artisten inte hittas alls


def create_hashtable(lista):
    """
    Hashtabell: Organiserar låtar per artist som en "telefonbok".
    Varje artist blir en nyckel som pekar direkt på alla deras låtar.
    Gör sökning supersnabb - ingen looping behövs!
    Denna kod är från Claude AI.
    """
    hashtable = {} #Skapar en tom hashtabell
    for song in lista: #Går igenom vare sång i listan
        if song.artist not in hashtable: #Kollar om artisten redan finns
            hashtable[song.artist] = [] #Om inte,skapas en tom lista för den artisten
        hashtable[song.artist].append(song) #Lägger till låten
    return hashtable


def hash_sok(hashtable, artist):
    """
    Sökning i hashtabell.
    Denna kod är från Claude AI.
    """
    return hashtable.get(artist, None)





def bubble_sort(lista):
    """
    Bubble Sort: Jämför två grannar åt gången och byter plats om de är i fel ordning.
    Varje varv "bubblar", alltså byts plats, den största artisten till slutet.
    Upprepar tills hela listan är sorterad alfabetiskt.
    Långsam men enkel metod! O(n²)
    Från Claude AI
    """
    n = len(lista) # Antal element
    arr = lista.copy() #Kopierar listan utan att ändra orginalet
    
    for i in range(n):
        swapped = False #Håller koll om något byts
        for j in range(0, n - i - 1): #Jämför parvis element i listan och hoppar över redan sorterade sista elementet.
            if arr[j].artist > arr[j + 1].artist: #Om vänster är större än höger (Alfabetiskt)
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #Byts plats
                swapped = True #Markera att något har byts
        if not swapped:
            break
    return arr #Listan retuneras


def merge_sort(lista):
    """
    Merge Sort: Delar listan i två halvor, sorterar varje halva (rekursivt),
    och slår sedan ihop dem i rätt ordning. O(n log n)
    Från Claude AI
    """
    if len(lista) <= 1: #Om listan har 0 eller 1 element är den redan sorterad så den retuneras.
        return lista
    
    mid = len(lista) // 2 #Dela listan i två halvor, för att få mitten.
    left = merge_sort(lista[:mid]) #Sorterar vänstra halvan,anropar sig rekursivt för varje halva
    right = merge_sort(lista[mid:]) #Sorterar högra halvan och anropar också sig sjävt. 
    
    return merge(left, right) #slå ihop de sorterade lsitorna


def merge(left, right):
    """merge() tar två redan sorterade listor och jämför dem element för 
    element för att skapa en slutgiltig sorterad lista.- från Claude AI"""
    result = []
    i = j = 0    # Pekare för left och right

    while i < len(left) and j < len(right):  # Så länge båda listorna har element
        if left[i].artist <= right[j].artist:   # Jämför första elementet i varje lista  
            result.append(left[i]) #Ta från vänster 
            i += 1   # Flytta vänster-pekaren framåt
        else:
            result.append(right[j])  # Ta från höger
            j += 1 # Flytta höger-pekaren framåt
    
    result.extend(left[i:])  # Lägg till det som är kvar i left
    result.extend(right[j:]) # Lägg till det som är kvar i right
    return result


#========== main-Funktion ========
def main():
    filename = "unique_tracks.txt"

    lista = readfile(filename)
    lista = lista[0:500000] #För att välja n till tabellen

    sorterad_lista = sorted(lista) #Skapar en sorterad lista för binärsökningen

    hashtable = create_hashtable(lista) #Skapar hashtabellen för sökningen i en hashtabell


    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    print("Söknings-delen:")

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    bintid = timeit.timeit(stmt = lambda: binsok(sorterad_lista, testartist), number = 10000)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")

    hashtid = timeit.timeit(stmt = lambda: hash_sok(hashtable, testartist), number = 10000)
    print("hashsökningen tog", round(hashtid, 4) , "sekunder")


    print("Sorterings-delen: ")
    bubble = timeit.timeit(stmt = lambda: bubble_sort(lista), number = 1)
    print("bubble tog", round(bubble, 4) , "sekunder")
    merge = timeit.timeit(stmt = lambda: merge_sort(lista), number = 1)
    print("merge tog", round(merge, 4) , "sekunder")




   

 
main()


"""
Resultatet från labben:

Sökning:
                    n = 250 000           n = 500 000      n = 1 000 000
Linjärsökning O(n):      11.41025s             0.5827s          0.0976s
Binärsökning O(log n):    0.0137s              0.0130s          0.0121s
Hashtabell O(1):         0.0006s               0.0006s          0.0006s


Sortering:
                                   n = 1000        n = 10 000 
Långsam sorteringsmetod (Bubble) O(n²):  0.0337s         3.9065s 
Snabbare sorteringsmetod (Merge sort) O(n logn):  0.0011s         0.0147s

Kommentar: n för över 10 000 har inte testats då det skulle ta alldeses för lång tid.

Analys:

Resultatet i tabellen om de olika sökmetoderna stämmer inte helt med teorin om man kollar på linjärsökningen.Då 
tiden minskar när n ökar ( 11.41s --> 0.58s --> 0.0976s), vilket inte ska kunna gå för O(n).Detta sker på grund av att i min kod så 
söker jag efter den sista artisten i varje slicad lista, i den orginella 
osorterade listan och det ger olika tider. T.ex. För n = 250k: artisten kanske ligger på plats 200 000 i filen --> lång söktid, 
men för n = 1M: artisten kanske ligger på plats 10 000 i filen --> kort söktid. Det hade vart bättre att söka för samma artist, för att få 
ett mindre missgivande resultat.Vad gäller Binär söktid är tiden nästan konstant 
för alla n, vilket funkar bra med teorin och Hashtabellen är exakt samma för alla n vilket är också bra enligt teorin. 
Om vi gör en hastighets jämförelse mellan Binärsökning och hashtabell så ser vi att i worst case är Binär ca 11.39s snabbare linjär och 
hashtabellen är ca 11,41s snabbare.Däremot den snabbaste sökmetod bland alla tre är som man ser i tabellen Hashtabellen.

I tabellen som innehåller resultaten från sorteringsmetoderna, så ser vi att den lång samma metoden, Bubble Sort,
ökar från 0.034s till 3.91s. Den ökar alltså ca 100 gånger. Däremot om vi kollar på den snabba metoden, Merge sort,
så ökar den från 0.001s till 0.015s. Den ökar alltså med ca 13 gånger. Slutsatsen som kan tas från tabbelen är att Bubble sort är
alldeles för långsam och inte så effektiv vad gäller stora databaser, men detta gäller inte för Merge Sort som är mycket snabbare och effektivare. 




"""