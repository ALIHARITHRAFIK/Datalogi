from linkedQFile import LinkedQ

#Godkända atomer
godkanda_atomer = """H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr
Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv """.split()

class Syntaxfel(Exception):
    pass

def formel(q):
    """<formel>::= <mol> \n"""
    mol(q)

    #Efter mol() ska kön vara tom
    if not q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + resten_av_kon(q))

def mol(q):
    """<mol>   ::= <group> | <group><mol>"""
    group(q)

    #Om det finns mer kvar och det inte är ), fortsätt läsa fler grupper
    if not q.isEmpty() and q.peek() != ')':
        mol(q)

def group(q):
    """<group> ::= <atom> |<atom><num> | (<mol>) <num>"""
    if q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    
    #Om gruppen börjar med (
    if q.peek() == '(':
        q.dequeue() #Ta bort '('
        mol(q) #Läs molekylen inuti parentesen

        #Nu måste det komma en )
        if q.isEmpty() or q.peek() != ')':
            if q.isEmpty():
                raise Syntaxfel("Saknad högerparentes vid radslutet")
            else:
                raise Syntaxfel("Saknad högerparentes vid radslutet " + resten_av_kon(q))
    

    
        q.dequeue() #Ta bort ')'

        #Efter ) måste det komma ett tal
        if q.isEmpty() or not q.peek().isdigit():
            raise Syntaxfel("Saknad siffra vid radslutet " + resten_av_kon(q))
    
        num(q)

    #Om gruppen börjar med stor bokstav
    elif q.peek().isalpha(): #isalpha ser till att det är en bokstav, vare sig stor eller liten- 
        atom(q)

        #Om det följs av ett tal 
        if not q.isEmpty() and q.peek().isdigit():
            num(q)

    #Annars är det fel
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + resten_av_kon(q))


        





def atom(q):
    """   <atom>  ::= <LETTER> | <LETTER><letter>"""
    if q.isEmpty():
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    
    if not q.peek().isupper():
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + resten_av_kon(q))
    
    #Läs atomnamnet
    atom_namn = q.peek()
    q.dequeue()

    #Om nästa tecken är liten bokstav, lägg till den
    if not q.isEmpty() and q.peek().islower():
        atom_namn += q.peek()
        q.dequeue()



    #Kontrollera att atomen finns i listan
    if atom_namn not in godkanda_atomer:
        raise Syntaxfel("Okänd atom vid radslutet " + resten_av_kon(q))
    
    
  


 

     

def num(q):
    """ <num>   ::= 2 | 3 | 4 | ..."""
    if q.isEmpty():
        raise Syntaxfel("Saknad siffra ")
    
    if not q.peek().isdigit(): #Om första tecknet inte är en siffra
        raise Syntaxfel("Saknad siffra ") 
    
    #Om första siffran 0, är det fel direkt
    if q.peek() == '0':
        q.dequeue() 
        raise Syntaxfel("För litet tal vid radslutet " +  resten_av_kon(q))

    #Om första siffran är 1, kolla om det bara är "1" eller om det följs av fler siffror
    if q.peek() == '1':
        q.dequeue() #Ta bort 1
        #Om inga fler siffror följer, då var det bara "1" vilket är fel
        if q.isEmpty() or not q.peek().isdigit():
            raise Syntaxfel("För litet tal vid radslutet "+  resten_av_kon(q))
        #Annars fortsätt läsa resten av siffrorna (t.ex. "12" är OK)
    else:
        #Första siffran är 2-9, ta bort den 
        q.dequeue()
        
        #Ta upp resterande siffror
    while not q.isEmpty() and q.peek().isdigit():
        q.dequeue()




def resten_av_kon(q):
    """Hjälpfunktion för att få resten av kön som en sträng"""
    result = ""
    while not q.isEmpty(): #While loop som går genom kön,så länge den är inte tom 
        result += str(q.dequeue()) #Varje uttaget element görs om till text och läggs till i strängen
    return result




def kolla_molekyl(molekyl_str):
    """Huvudfunktion som kollar en molekylsträng"""
    q = LinkedQ()
    for loop in molekyl_str: #molekyl_str byts ut mot  inputen av användaren
        q.enqueue(loop) #Lägger varje tecken i kön
    try:
        formel(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as e:
        return str(e)


def main():
    """Huvudprogrammet"""
    print("Skriv in molekyler (separera med mellanslag). Avsluta med #.")
    
    while True:
        # Texten inuti input() visas i terminalen
        line = input("Molekyl: ").strip()
        
        # Om man bara trycker Enter utan att skriva något, hoppa till nästa varv
        if not line:
            continue

        molekyler = line.split()

        for mol in molekyler:
            if mol == "#":
                print("Avslutar programmet.")
                return # Avsluta helt
            
            resultat = kolla_molekyl(mol)
            print(resultat)


if __name__ == '__main__':
    main() #Kattis ignorerar allt efter detta, så Unittest är inte med




