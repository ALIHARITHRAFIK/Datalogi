from linkedQFile import LinkedQ
import unittest

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
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    
    if not q.peek().isupper():
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + resten_av_kon(q))
    
    
    #Ta upp stor bokstav
    q.dequeue() 

    #Om nästa tecken är liten bokstav, ta upp den också
    if not q.isEmpty() and q.peek().islower():
        letter(q)


 

def LETTER(q):
    """ <LETTER>::= A | B | C | ... | Z"""
    if q.isEmpty() or not q.peek().isupper():
        raise Syntaxfel("Saknad stor bokstav vid radslutet" +  resten_av_kon(q) )


def letter(q):
    """  <letter>::= a | b | c | ... | z"""
    if q.isEmpty() or not q.peek().islower():
        raise Syntaxfel("Saknad liten bokstav vid radslutet" +  resten_av_kon(q) )
    q.dequeue()
     

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
            raise Syntaxfel("För litet tal vid radslutet ")
        #Annars fortsätt läsa resten av siffrorna (t.ex. "12" är OK)
    else:
        #Första siffran är 2-9, ta bort den 
        q.dequeue()
        
        #Ta upp resterande siffror
    while not q.isEmpty() and q.peek().isdigit():
        q.dequeue()



def resten_av_kon(q):
    """Hjälpfunktion flr att få resten av kön som en sträng"""
def resten_av_kon(q):
    """Hjälpfunktion flr att få resten av kön som en sträng"""
    result = ""
    while not q.isEmpty():
        result += str(q.dequeue())
    return result




def kolla_molekyl(molekyl_str):
    """Huvudfunktion som kollar en molekylsträng"""
    q = LinkedQ()
    for loop in molekyl_str:
        q.enqueue(loop)
    try:
        molekyl(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as e:
        return str(e)

def main():
    """Huvudprogrammet"""
    while True:
        line = input().strip()
        if line == "#":
            break
        print(kolla_molekyl(line))



if __name__ == '__main__':
    main() #Kattis ignorerar allt efter detta, så Unittest är inte med








#=============================== UNIT TEST =======================================================
class TestMolekyl(unittest.TestCase):

    def test_korrekta_molekyer(self):
        """Testa att korrekta molekyler godkänns"""
        self.assertEqual(kolla_molekyl('H2'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(kolla_molekyl('P21'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(kolla_molekyl('Ag3'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(kolla_molekyl('Fe12'), 'Formeln är syntaktiskt korrekt')

    def test_saknad_stor_bokstav(self):
        """Testa molekyler som börjar med liten bokstav"""
        resultat = kolla_molekyl('a')
        self.assertIn('Saknad stor bokstav', resultat)

        resultat = kolla_molekyl('cr12')
        self.assertIn('Saknad stor bokstav', resultat)

    def test_for_litet_tal(self):
        """Testa molekyler med 0 eller 1 som första siffra"""
        resultat = kolla_molekyl('Cr0')
        self.assertIn('För litet tal', resultat)

        resultat = kolla_molekyl('Pb1')
        self.assertIn('För litet tal', resultat)

        resultat = kolla_molekyl('H01011')
        self.assertIn('För litet tal', resultat)

    def test_syntaxfel_kastas(self):
        """Testa att Syntaxfel kastas korrekt"""
        q = LinkedQ()
        q.enqueue('a') #Liten bokstav

        with self.assertRaises(Syntaxfel):
            atom(q)







