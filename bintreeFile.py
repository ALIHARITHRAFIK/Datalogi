class Node: #Den här klassen initierar noderna i trädet
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def putta(p, newvalue):
    """Funktion som gör själva jobbet att sätta in en ny nod"""
    if p is None:
        return Node(newvalue) #om platsen är tom,skapas noden där
    elif newvalue < p.value: #Om det nya värdet är mindre än den existerande noden så går vi till vänster och rekurserar
        p.left = putta(p.left, newvalue) 
    else:
        p.right = putta(p.right, newvalue) #Uppdaterar högerbarnet med den nya metoden efter rekursion
    return p #Retunerar noden med uppdaterade barn 

def finns( p, value):
    """Den här funktionen söker efter värdet i trädet"""
    if p is None: #Om noden är tom retunera False
        return False
        
    elif value == p.value: #om värdet är hittat retunera True
        return True
    
    elif value < p.value: #Gå rekursivt vänster för att söka värdet 
        return finns(p.left, value)
    else:
        return finns(p.right, value) #Gå rekursivt höger för att söka värdet 

def skriv(p):
    """sDen här funktionen skriver ut träder"""
    if p is not None:
        skriv(p.left) #Kör vänster noden
        print(p.value, end = " ") #printar noden
        skriv(p.right)#Kör höger nod
    

class Bintree:
    def __init__(self):
        self.root = None #initierar roten och börjar tomt 
    
    def put(self, newvalue):
        #sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)
    def __contains__(self,value):
        #True om value finns i trädet, False annars
        return finns(self.root, value)
    def write(self):
        #skriver ut trädet i inorder
        skriv(self.root)
        print("\n")
    

