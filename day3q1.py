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
            compartment1 = rucksack[:len(rucksack)//2]
            compartment2 = rucksack[len(rucksack)//2:len(rucksack)-1]
            comp_dict = {}
            for char in compartment1:
                if char not in comp_dict:
                    comp_dict[char] = 1
            for char in compartment2:
                if char in comp_dict:
                    comp_dict[char] = "answer"
            for key in comp_dict:
                if comp_dict[key] == "answer":
                    priority_sum += priority_val(key)

    
    return priority_sum


def main():
    print(priorities_rucksack("Test_Input/rucksack_input.txt"))



if __name__ == "__main__":
    main()
            
