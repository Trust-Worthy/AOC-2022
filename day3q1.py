

def priorities_rucksack(filename):

    with open(filename) as file:
        compartment1 = ""
        compartment2 = ""
        for rucksack in file:
            rucksack.strip()
            rucksack.split()
            compartment1 = slice(0,len(rucksack)//2)
            compartment2 = slice(len(rucksack)//2,len(rucksack))
            

            
