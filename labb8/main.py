from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass


def molekyl(q):
    """   <molekyl> ::= <atom> | <atom><num>"""
    atom(q)
    if not q.isEmpty() and q.peek().isdigit():
        num(q)


def atom(q):
    """   <atom>  ::= <LETTER> | <LETTER><letter>"""
    if q.isEmpty():
        raise Syntaxfel("sakand storbokstav vid radslutet")
    
    if not q.isEmpty().isupper():
        raise Syntaxfel("sakand storbokstav vid radslutet" +  resten_av_kon(q))
    
    #Ta upp stor bokstav
    q.dequeue() 

    #Om nästa tecken är liten bokstav, ta upp den också
    if not q.isEmpty() and q.peek().islower():
        letter(q)


 

def LETTER(q):
    """ <LETTER>::= A | B | C | ... | Z"""
    if q.isEmpty() or not q.peek().isupper():
        raise Syntaxfel("sakand storbokstav vid radslutet" +  resten_av_kon(q) )


def letter(q):
    """  <letter>::= a | b | c | ... | z"""
    if q.isEmpty() or not q.peek().islower():
        raise Syntaxfel("sakand liten bokstav vid radslutet" +  resten_av_kon(q) )
     

def num(q):
    """ <num>   ::= 2 | 3 | 4 | ..."""
    if q.isEmpty():
        raise Syntaxfel("Saknad siffra")
    
    if not q.peek().isdigit(): #Om första tecknet inte är en siffra
        raise Syntaxfel("Saknad siffra")
    
    if q.peek() in ["0", "1"]: #Första siffran får inte vara 0 eller 1
        raise Syntaxfel("För litet tal vid radslutet " + resten_av_kon(q))
    

    #Ta upp första siffran
    q.dequeue()

    #Ta upp resterande siffror
    while not q.isEmpty() and q.peek().isdigit():
        q.dequeue

    


def resten_av_kon(q):
    """Hjälpfunktion flr att få resten av kön som en sträng"""
    result = ""
    while not q.isEmpty():
        result += str(q.dequeue())
    return result



def kolla_molekyl(molekyl_str):
    """Huvudfunktion som kollar en molekylsträng"""
    q = LinkedQ
    for loop in molekyl_str:
        q.enqueue(loop)
    try:
        molekyl(q)
        return "Formeln har rätt syntax"
    except syntaxfel as e:
        return str(e)

def main():
    """Huvudprogrammet"""
    molekyl_str = input("Ange molekyl: ")
    resultat = kolla_molekyl(molekyl_str)
    print(resultat)