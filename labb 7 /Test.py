import csv
from dictHash import DictHash
from hashtable import Hashtable



class Kdrama: #Denna klass som representerar ett koreanskt drama
    def __init__(self,DramaName, Rating, Actors, ViewShipRate, Genre, Director, Writer, Year, NoOfEpisodes, Network):
        #Konstruktör som skapar ett kdrama-objekt med alla attibut
        self.DramaName = DramaName
        self.Rating = Rating
        self.Actors = Actors
        self.ViewShipRate = ViewShipRate
        self.Genre = Genre
        self.Director = Director
        self.Writer = Writer
        self.Year = Year
        self.NoOfEpisodes = NoOfEpisodes
        self.Network = Network

    def __str__(self):
        #Returnerar en sträng med dramats viktigaste information
        return "Drama Name: " + self.DramaName + " ,Rating: " + self.Rating + " ,Genre: " + self.Genre + " ,Year: " + self.Year #Retunerar en sträng
    
    def __lt__(self,other): #Self = Drama 1 och other = Drama 2
        #Jämför två draman baserat på rating (för sortering)
        return float(self.Rating) < float(other.Rating)
    
    def get_genre(self):
        #Retunerar dramats genre
        return self.Genre 
    
    def is_recent(self):
        #Kollar om dramat är från 2021 eller senare 
        return int(self.Year) > 2020





def read_all_dramas(): #Lägger dramorna i csv filen till en lista
    kdrama_list = [] #Listan för kdramorna
    with open("kdrama.csv" , "r",  newline = "") as file:
        content = csv.DictReader(file) #csv.DictReader läser CSV-filen och konverterar varje rad till en dictionary
        for row in content:
            drama = Kdrama(row["Drama Name"],row["Rating(Out of 10)"], row["Actors"], 
                       row["Viewship Rate"], row["Genre"], row["Director"],row["Writer"],row["Year"],row["No of Episodes"],row["Network"])
            kdrama_list.append(drama)
    return kdrama_list



def search_drama_name(kdrama_list): #Denna funktion är till för att kunna söka fram dramorna i listan
    SearchKdrama = input("Skriv vilken kdrama du söker: ")
    for loop in kdrama_list: #Går igenom varje drama i listan, ett i taget
        if SearchKdrama.lower() in loop.DramaName.lower(): #Kollar om sökordet finns i det akutella dramats namn           
            print(loop)


def create_hashtable(kdrama_list):
    size = len(kdrama_list) * 2
    d = Hashtable(size)
    for drama in kdrama_list:
        d.store(drama.DramaName,drama)
    return d
        


def testkod():
    dramas = read_all_dramas()
    d = create_hashtable(dramas)

   


    sök = input("Skriv namnet på dramat du vill söka efter: ")
    try:
        result = d.search(sök)
        print("Hittade: ", result)
    except KeyError:
        print("Kunde inte hitta dramat")




   


testkod()
