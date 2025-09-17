from array import array

class ArrayQ:
    def __init__(self): #Initiera array
        self.__arr = array('i',[]) #Där 'i' är själva positionen

    def isEmpty(self): #Funktionen kollar om arrayen är tom 
        return len(self.__arr) == 0 
    
    def enqueue(self,x): #Funktionen lägger till variabler till arrayen
        self.__arr.append(x)
    
    def dequeue(self): #Funktionen tar bort första variablen från arrayen
        return self.__arr.pop(0)
    
    def size(self): #Funktionen retunerar längden av arrayen
        return len(self.__arr)
    


if __name__ == "__main__": #För att inte köra test-koden när du importerar
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")
