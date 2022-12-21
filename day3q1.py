def priority_val(char):

    if char.islower() == True:
        return ord(char) - 96
    else:
        return ord(char) - 38
    

def priorities_rucksack(filename):
    priority_sum = 0
    with open(filename) as file:
        compartment1 = ""
        compartment2 = ""
        for rucksack in file:
            rucksack.strip()
            rucksack.split()
            compartment1 = slice(0,len(rucksack)//2)
            compartment2 = slice(len(rucksack)//2,len(rucksack))

            set(compartment1)
            set(compartment2)

            for i,j in zip(compartment1,compartment2):
                if i == j:
                    priority_sum += priority_val(i)



            
