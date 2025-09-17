from linkedQFile import LinkedQ

#Denna funktion utför magitricket
def trollkarl_trick(kortlek): #"kort_lista" är då listan vi får som vi ska sätta in 
        q = LinkedQ()
        for kort in kortlek: #Sätter in alla kort i arrayen
            q.enqueue(kort)

        utlagda_kort = [] #Denna lista är till för att spara dem kort som visades av tricket
        antal_steg = 1

        while not q.isEmpty(): 

            kort = q.dequeue() #Tar ut det första kortet

            if antal_steg % 2 == 1: #Om vi är i ett udda steg så kommer kortet läggas i den sista platsen i arrayen
                q.enqueue(kort)
            else: 
                utlagda_kort.append(kort) #Om det är jämnt steg, så ska kortet visas

            antal_steg += 1 #ökar antalet steg med 1 
        
        
            
        return utlagda_kort 





#Denna funktion testar programmet
def testavprogram():
   kort_lista = input().split()
   resultat = trollkarl_trick(kort_lista)
   print(*resultat) #Printar ut alla värden i listan,*är "unpacking"

testavprogram()






        

        


    


