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
    



def readfile(filename):
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
    Binärsökning i sorterad lista.
    Denna kod är från Claude AI 
    """
    low = 0
    high = len(sorterad_lista) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorterad_lista[mid].artist == artist:
            return sorterad_lista[mid]
        elif sorterad_lista[mid].artist < artist:
            low = mid + 1
        else:
            high = mid - 1
    return None


def create_hashtable(lista):
    """
    Skapar en hashtabell (dict) för snabb sökning.
    Denna kod är från Claude AI.
    """
    hashtable = {}
    for song in lista:
        if song.artist not in hashtable:
            hashtable[song.artist] = []
        hashtable[song.artist].append(song)
    return hashtable


def hash_sok(hashtable, artist):
    """
    Sökning i hashtabell.
    Denna kod är från Claude AI.
    """
    return hashtable.get(artist, None)

#========== main-Funktion ========
def main():

    filename = "unique_tracks.txt"

    lista = readfile(filename)
    lista = lista[0:1000000] #För att välja n till tabellen
    n = len(lista)
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    bintid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")

    hashtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("hashsökningen tog", round(hashtid, 4) , "sekunder")


   

 
main()
