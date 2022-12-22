def priority_val(char):
    """
    This function takes in a character and returns a number. a = 1 (through lower z) and A = 27
    (through upper Z)
    """

    if char.islower() == True:
        return ord(char) - 96
    else:
        return ord(char) - 38
    

def priorities_rucksack(filename):
    """
    This function reads the input data, breaks up each line into two compartments,
    and calculates the total of the duplicate character in each rucksack.
    """
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
    
    return priority_sum


def main():
    



if __name__ == "__main__":
    main()
            
