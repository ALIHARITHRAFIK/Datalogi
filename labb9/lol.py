
def main():
    """Huvudprogrammet"""
    while True:
        line = input().strip()
        molekyler = line.split()

        for mol in molekyler:
            if mol == "#":
                return #Avsluta helt
            resultat = kolla_molekyl(mol)
            print(resultat)
