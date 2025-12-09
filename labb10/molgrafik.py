from linkedQFile import LinkedQ
import unittest


def version():
    """Kolla vilken version av Python vi har"""
    import sys
    datatyp = type(sys.version_info)
    if datatyp == type(()):
        version = sys.version_info[0]
    else:
        version = sys.version_info.major
    return version

if version() == 3:
    from tkinter import *
else:
    from Tkinter import *



class Syntaxfel(Exception):
    pass




class Ruta:
    def __init__(self, atom = "()", num = 1):
        self.atom = atom
        self.num = num
        self.next=None
        self.down=None


class Molgrafik:

    def __init__(self):
        self.root=None
        self.stor=("Courier",18,"bold")
        self.liten=("Courier",14,"bold")

    def ram(self,master,sidan):
        """Returnerar en ram. Parametrar: master (grafikfonstret), sidan (vilken sida den ska ligga mot, t ex LEFT) """
        ramen=Frame(master,bg="white")
        ramen.pack(side=sidan,fill=BOTH)
        return ramen

    def atomruta(self,master,namn,num):
        """Ritar en atomruta. Parametrar: master (grafikfonstret), namn (atomnamnet), num (antal atomer) """
        ruta=Frame(master,bg="yellow",borderwidth=2,relief=GROOVE)
        ruta.pack(side=LEFT)
        atom=Frame(ruta,bg="yellow")
        atom.pack(side=LEFT)
        Label(atom,text=namn,font=self.stor,bg="yellow").pack()
        Frame(atom, height=5, bg="yellow").pack()
        if num>1:
            Label(ruta, text=str(num),font=self.liten,bg="yellow").pack(side=BOTTOM)

    def streck(self,master):
        """ Ritar ett streck. Parametrar: master (grafikfonstret) """
        strecket=Frame(master)
        strecket.pack(side=LEFT,fill=BOTH,expand=True)
        Frame(strecket,bg="white",height=20).pack(fill=X)
        Frame(strecket,bg="red",height=4,width=25).pack(fill=X)
        Frame(strecket,bg="white").pack(fill=BOTH,expand=1)

    def stolpe(self,master):
        """ Ritar en stolpe. Parametrar: master (grafikfonstret) """
        hela=self.ram(master,TOP)
        stolpen=self.ram(hela,LEFT)
        Frame(stolpen,bg="white",width=15).pack(side=LEFT)
        Frame(stolpen,bg="red",width=4,height=25).pack(side=LEFT)
        Frame(hela,bg="white").pack(fill=BOTH,expand=1)

    def picture(self,master,p):
        """ Ritar bilden. Parametrar: master (grafikfonstret), p (referens till datstrukturen som ska ritas) """
        if p is None: return
        storruta=self.ram(master,LEFT)
        rest=self.ram(master,LEFT)
        uppruta=self.ram(storruta,TOP)
        nerruta=self.ram(storruta,TOP)
        self.atomruta(uppruta,p.atom,p.num)
        if p.down:
            self.stolpe(nerruta)
            self.picture(nerruta,p.down)
            self.ram(nerruta,TOP)
        if p.next:
            self.streck(uppruta)
            self.picture(rest,p.next)

    def show(self,p):
        """ Ritar hela bilden. Parametrar: p (referens till datastrukturen som ska ritas) """
        if self.root!=None:
            self.root.destroy()
        self.root=Tk()
        Label(self.root,text="  ",font=self.stor,bg="white").pack(side=LEFT,fill=Y)
        self.picture(self.root,p)
        #mainloop() #Kommentera bort om du anv. IDLE (IDLE har egen mainloop())




#Godkända atomer
godkanda_atomer = """H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr
Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv """.split()

atom_vikt = "H 1.00794;\
He 4.002602;\
Li 6.941;\
Be 9.012182;\
B 10.811;\
C 12.0107;\
N 14.0067;\
O 15.9994;\
F 18.9984032;\
Ne 20.1797;\
Na 22.98976928;\
Mg 24.3050;\
Al 26.9815386;\
Si 28.0855;\
P 30.973762;\
S 32.065;\
Cl 35.453;\
K 39.0983;\
Ar 39.948;\
Ca 40.078;\
Sc 44.955912;\
Ti 47.867;\
V 50.9415;\
Cr 51.9961;\
Mn 54.938045;\
Fe 55.845;\
Ni 58.6934;\
Co 58.933195;\
Cu 63.546;\
Zn 65.38;\
Ga 69.723;\
Ge 72.64;\
As 74.92160;\
Se 78.96;\
Br 79.904;\
Kr 83.798;\
Rb 85.4678;\
Sr 87.62;\
Y 88.90585;\
Zr 91.224;\
Nb 92.90638;\
Mo 95.96;\
Tc 98;\
Ru 101.07;\
Rh 102.90550;\
Pd 106.42;\
Ag 107.8682;\
Cd 112.411;\
In 114.818;\
Sn 118.710;\
Sb 121.760;\
I 126.90447;\
Te 127.60;\
Xe 131.293;\
Cs 132.9054519;\
Ba 137.327;\
La 138.90547;\
Ce 140.116;\
Pr 140.90765;\
Nd 144.242;\
Pm 145;\
Sm 150.36;\
Eu 151.964;\
Gd 157.25;\
Tb 158.92535;\
Dy 162.500;\
Ho 164.93032;\
Er 167.259;\
Tm 168.93421;\
Yb 173.054;\
Lu 174.9668;\
Hf 178.49;\
Ta 180.94788;\
W 183.84;\
Re 186.207;\
Os 190.23;\
Ir 192.217;\
Pt 195.084;\
Au 196.966569;\
Hg 200.59;\
Tl 204.3833;\
Pb 207.2;\
Bi 208.98040;\
Po 209;\
At 210;\
Rn 222;\
Fr 223;\
Ra 226;\
Ac 227;\
Pa 231.03588;\
Th 232.03806;\
Np 237;\
U 238.02891;\
Am 243;\
Pu 244;\
Cm 247;\
Bk 247;\
Cf 251;\
Es 252;\
Fm 257;\
Md 258;\
No 259;\
Lr 262;\
Rf 265;\
Db 268;\
Hs 270;\
Sg 271;\
Bh 272;\
Mt 276;\
Rg 280;\
Ds 281;\
Cn 285"

def hämta_atomvikt(atomnamn):
    """Hjälpfunktion: Letar upp vikten r en atom direkt i textsträngen"""

    #Vi loopar igenom strängen atom_vikt varje gång vi behöver vikt
    for element in atom_vikt.split(';'):
        if element.strip():
            parts = element.strip().split()
            if len(parts) == 2 and parts[0] == atomnamn:
                    return float(parts[1])
    return 0.0 #om atomen inte hittas
                    




def formel(q):
    """<formel>::= <mol> \n - RETUNERAR Träd"""
 
    mol_tree = mol(q)



    #Efter mol() ska kön vara tom
    if not q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + resten_av_kon(q))
    
    return mol_tree

def mol(q):
    """<mol>   ::= <group> | <group><mol>"""
    mol_tree = group(q)

    #Om det finns mer kvar och det inte är ), fortsätt läsa fler grupper
    if not q.isEmpty() and q.peek() != ')':
        mol_tree.next = mol(q)
    return mol_tree


def group(q):
    """<group> ::= <atom> |<atom><num> | (<mol>) <num>"""
    if q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    
    ruta = Ruta()
    
    #Om gruppen börjar med (
    if q.peek() == '(':
        q.dequeue() #Ta bort '('
        ruta.down = mol(q) #Sätt down till molekylen inuti

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
        
        ruta.num = num(q)
        
    

    #Om gruppen börjar med stor bokstav
    elif q.peek().isalpha(): #isalpha ser till att det är en bokstav, vare sig stor eller liten- 
        ruta.atom = atom(q) #sätt atom

        #Om det följs av ett tal 
        if not q.isEmpty() and q.peek().isdigit():
            ruta.num = num(q)

    #Annars är det fel
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + resten_av_kon(q))
    
    return ruta


        





def atom(q):
    """   <atom>  ::= <LETTER> | <LETTER><letter> """
    if q.isEmpty():
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    
    if not q.peek().isupper():
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + resten_av_kon(q))
    
    #Läs atomnamnet
    atom_namn = q.peek()
    q.dequeue()

    #Om nästa tecken är liten bokstav, lägg till den. Sker bara en bokstav åt gången
    if not q.isEmpty() and q.peek().islower():
        atom_namn += q.peek()
        q.dequeue()


    #Kontrollera att atomen finns i listan
    if atom_namn not in godkanda_atomer:
        raise Syntaxfel("Okänd atom vid radslutet " + resten_av_kon(q))
    
    return atom_namn
    
    


 

     

def num(q):
    """ <num>   ::= 2 | 3 | 4 | ... - Retunera tal"""
    if q.isEmpty():
        raise Syntaxfel("Saknad siffra ")
    
    if not q.peek().isdigit(): #Om första tecknet inte är en siffra
        raise Syntaxfel("Saknad siffra ") 
    
    #Om första siffran 0, är det fel direkt
    if q.peek() == '0':
        q.dequeue() 
        raise Syntaxfel("För litet tal vid radslutet " +  resten_av_kon(q))
    
    num_str = ""

    #Om första siffran är 1, kolla om det bara är "1" eller om det följs av fler siffror
    if q.peek() == '1':
        num_str = '1'
        q.dequeue() #Ta bort 1
        #Om inga fler siffror följer, då var det bara "1" vilket är fel
        if q.isEmpty() or not q.peek().isdigit():
            raise Syntaxfel("För litet tal vid radslutet "+ resten_av_kon(q))
 

        while not q.isEmpty() and q.peek().isdigit():
            num_str += q.peek()
            q.dequeue()
    else:
        #Första siffran är 2-9, ta bort den 
        num_str = q.peek()
        q.dequeue()
        
        #Ta upp resterande siffror
        while not q.isEmpty() and q.peek().isdigit():
            num_str += q.peek()
            q.dequeue()

    return int(num_str)


def weight(mol): 
    """Beräkna molekylvikten rekursivt"""
    if mol is None:
        return 0.0
    
    #Vikt för denna ruta
    if mol.atom == "()":
        #Parantesgrupp - räkna vikten av down * num
        vikt = weight(mol.down) * mol.num
    else:
        #Atom - hämta atomvikt * num
        vikt = hämta_atomvikt(mol.atom) * mol.num
    
    #Lägg till vikten av next
    vikt += weight(mol.next)

    return vikt





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
        mol_tree = formel(q)
        return mol_tree
        
    except Syntaxfel as e:
        print(str(e))
        return None




def main():
    """Huvudprogrammet"""
    mg = Molgrafik()
    while True:
        formel_str = input("Molekyl: "). strip()

        if formel_str == "":
            break
        
     
        mol_tree = kolla_molekyl(formel_str)

        if mol_tree is not None:
            print("Formeln är syntaktiskt korrekt")
            vikt = weight(mol_tree)
            print("Molekylvikt: ", vikt)

            mg.show(mol_tree)
         
    


if __name__ == '__main__':
    main() #Kattis ignorerar allt efter detta, så Unittest är inte med


#=============================== UNIT TEST =======================================================
class TestMolekyl(unittest.TestCase):

    def test_korrekta_molekyer(self):
        """Testa att korrekta molekyler godkänns"""
        #assertEqual är till för att se till att funktionen ger samma svar: "Formeln är ..."
        self.assertEqual(kolla_molekyl('H2'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(kolla_molekyl('P21'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(kolla_molekyl('Ag3'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(kolla_molekyl('Fe12'), 'Formeln är syntaktiskt korrekt')

    def test_saknad_stor_bokstav(self):
        """Testa molekyler som börjar med liten bokstav"""
        resultat = kolla_molekyl('a') #Kör funktionen med "a", spara resultatet
        self.assertIn('Saknad stor bokstav', resultat) #Kolla att texten finns med i resultatet 

        resultat = kolla_molekyl('cr12')
        self.assertIn('Saknad stor bokstav', resultat)

        resultat = kolla_molekyl('Nacl')
        self.assertIn('Saknad stor bokstav', resultat)




    def test_for_litet_tal(self):
        """Testa molekyler med 0 eller 1 som första siffra"""
        resultat = kolla_molekyl('Cr0')
        self.assertIn('För litet tal', resultat)

        resultat = kolla_molekyl('Pb1')
        self.assertIn('För litet tal', resultat)

        resultat = kolla_molekyl('H01011')
        self.assertIn('För litet tal', resultat)

        resultat = kolla_molekyl('H0')
        self.assertIn('För litet tal', resultat)

        resultat = kolla_molekyl('H1C')
        self.assertIn('För litet tal', resultat)

        resultat = kolla_molekyl('H02C')
        self.assertIn('För litet tal', resultat)

    def test_syntaxfel_kastas(self):
        """Testa att Syntaxfel kastas korrekt"""
        #Skaoa en kö med ett fel i (liten bokstav)
        q = LinkedQ()
        q.enqueue('a') #Liten bokstav

        #assertRaises förväntar sig att ett syntaxfel ska kastas
        with self.assertRaises(Syntaxfel):
            atom(q) #Anropar atom funktionen, den ska kasta ett syntaxfel

#==================================== NYA TESTER FÖR LABB 9 ============================================
    def test_sample_input_1(self):
        self.assertEqual(kolla_molekyl('Na'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(kolla_molekyl('H2O'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(kolla_molekyl('Si(C3(COOH)2)4(H2O)7'), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(kolla_molekyl('Na332'), 'Formeln är syntaktiskt korrekt')

    def test_okand_atom(self):
        """Testa okänd atom"""
        resultat = kolla_molekyl('C(Xx4)5')
        self.assertIn('Okänd atom vid radslutet', resultat)

    def test_saknad_siffra_efter_parantes(self):
        """Testa sakand siffra efter parentes"""
        resultat = kolla_molekyl('C(OH4)C')
        self.assertIn('Saknad siffra vid radslutet', resultat)

    def test_saknad_hogerparantes(self):
        """Testa sakand saknad högerparentes"""
        resultat = kolla_molekyl('C(OH4C')
        self.assertIn('Saknad högerparentes vid radslutet', resultat)

    def test_felaktig_gruppstart(self):
        """Testa felaktig gruppstart"""
        resultat = kolla_molekyl('H2O)Fe')
        self.assertIn('Felaktig gruppstart vid radslutet', resultat)

        resultat = kolla_molekyl('(Cl)2)3')
        self.assertIn('Felaktig gruppstart vid radslutet', resultat)

        resultat = kolla_molekyl(')')
        self.assertIn('Felaktig gruppstart vid radslutet', resultat)

        resultat = kolla_molekyl('2')
        self.assertIn('Felaktig gruppstart vid radslutet', resultat)
















