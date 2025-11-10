
class HashNode:

   def __init__(self, key = "", data = None): #Noder till klassen Hashtable 
         """key är nyckeln som anvands vid hashningen
            data är det objekt som ska hashas in"""
         self.key = key
         self.data = data

  


class Hashtable:

   def __init__(self, size): 
      """size: hashtabellens storlek"""
      self.size = size
      self.table = [[] for i in range(size)] #Skapar antal listor baserat på size-parametern

   def store(self, key, data):
      """key är nyckeln
         data är objektet som ska lagras
         Stoppar in "data" med nyckeln "key" i tabellen."""
      index = self.hashfunction(key)

      for node in self.table[index]:
         if node.key == key:
            node.data = data
            return
   
      self.table[index].append(HashNode(key, data))
      

   def search(self, key):
      """key är nyckeln
         Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
         Om "key" inte finns ska det bli KeyError """
      index = self.hashfunction(key)
      for node in self.table[index]:
         if node.key == key:
            return node.data
  
      
      raise KeyError

   def hashfunction(self, key):
      """key är nyckeln
         Beräknar hashfunktionen för key"""
      hash_value = 0
      for char in key:
         #ord() konverterar varje tecken till heltal
         hash_value = hash_value * 31 + ord(char)
      return hash_value % self.size
   

   
