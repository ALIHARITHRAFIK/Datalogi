from bintreeFile import Bintree


def skapabarn(ord, svenska,gamla):
    """ skapar alla barn till ett ord genom att byta ut en bokstav i taget"""

    alfabet = "abcdefghijlkmopqrstuvxyzåäö"
    barn = []

    for i in range(len(ord)): #For-loopen körs enligt antalet bokstäver i ordet
        for bokstav in alfabet:
            if bokstav != ord[i]: #Bokstaven i alfabetet ska inte matcha bokstaven i 
                nytt_ord = ord[:i] + bokstav + ord[i+1:] #Byter ut bokstaven i och behåller resten

                if nytt_ord in svenska and nytt_ord not in gamla:
                    print(nytt_ord)
                    gamla.put(nytt_ord)
                    barn.append(nytt_ord)
    return barn 



























