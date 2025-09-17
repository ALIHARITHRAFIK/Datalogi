
#används för att testade kod

#Test punkt 3
drama1 = Kdrama("squid game", "8.7", "Lee Jung-jae", "95%", "Thriller", "Hwang Dong-hyuk", "Hwang Dong-hyuk", "2021", "9" ,"Netflix" )

drama2 = Kdrama("Legend of the Blue Sea", "8.1", "Jun Ji-hyun, Lee Min-ho", "17.6", "Fantasy,Romance,Comedy", "Jin Hyuk, Park Seon-Ho","Park Ji-eun", "2016", "21", "SBS" )

#Testar alla metoder:
print("======== Testar Metoderna ======\n")
print("Drama 1: ", drama1) #__str__
print("Drama 2: " , drama2)#__str__
print("Drama1 < Drama 2: ", drama1 < drama2)#__lt__
print("Drama1 genre: ", drama1.get_genre())
print("Drama1 is recent: ", drama1.is_recent())
print("Drama2 is recent: ", drama2.is_recent())


#Test punkt 4
print("========Testar alla dramas========\n")
all_dramas = read_all_dramas()
print("Antal draman i listan: ", len(all_dramas))
print("Första dramat: ", all_dramas[0])
if len(all_dramas) > 1:
    print("Andra dramat: ", all_dramas[1])


