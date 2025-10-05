from bintreeFile import Bintree
#Test 1: Skapa träd och lägg till flera ord
svenska = Bintree()
svenska.put("gurka")
svenska.put("äpple")
svenska.put("banan")
svenska.put("citron")

#Test 2: Testa __contains__(finns ordet?)
if "gurka" in svenska:
    print("Hittade gurka!\n ")
else:
    print("Hittade inte gurka!\n ")

if "tomat" in svenska:
    print("Hittade tomat!\n ")
else:
    print("Hittade inte tomat!\n ")

#Test 3: Skriv ut i sorterad ordning:
print("alla ord i sorterad ordning: ")
svenska.write() #ska skriva: banan citron gurka äpple

#Test 4: Testa dubletter
svenska.put("gurka")  #Lägg till samma ord igen 
print("EFter dublett: ")
svenska.write() #ska fortfarande bara ha "gurka"



"""Jag har också använt test kod från del 1 av labben i canvas"""