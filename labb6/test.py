#Denna kod är tagen från claude.ai
def binary_search(the_list, key): 
    """
    Iterativ binärsökning som returnerar nyckeln om den finns,
    None om nyckeln inte finns i listan.
    """
    left = 0
    right = len(the_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if the_list[mid] == key:
            return key
        elif the_list[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    return None

#Denna kod är tagen från canvas sidan labb 6
def main():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main()