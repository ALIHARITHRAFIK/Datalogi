class Node:
    def __init__(self,value):
        self.value = value #Vad noden innehåller
        self.next = None #Pekar på nästa nod (börjar som none)
    
class LinkedQ:
    def __init__(self):
        self.__first = None #Pekar på den första noden 
        self.__last = None #Pekar på den sista noden

    #Kollar om kön är tom
    def isEmpty(self): 
        return self.__first is None 
    
    def enqueue(self,x):
        En_Node = Node(x) #Där x är värdet i noden

        #Om kön är tom kommer både attirbuterna att peka på samma node
        if self.isEmpty():
            self.__first = En_Node
            self.__last =  En_Node
        else:
            self.__last.next = En_Node #Pekar på nästa node
            self.__last = En_Node #Nya noden blir det sista 

    def dequeue(self):

        if self.isEmpty(): #Ser till att det inte kraschar om det börjar med en tom kö
            return None
        
        värde = self.__first.value #Spara värde
        self.__first = self.__first.next #Pekar på nästa nod

        #Om kön blir tom:
        if self.__first is None:
            self.__last = None 

        return värde 
    
    def peek(self):
        if self.__first is None: #Kollar om kön är tom
            return None #Då retuneras None
        return self.__first.value #Annars retuneras första värdet


            

        


         


    

    
