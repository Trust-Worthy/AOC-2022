def priority_val(char):
    """
    This function takes in a character and returns a number. a = 1 (through lower z) and A = 27
    (through upper Z)
    """

    if char.islower() == True:
        return ord(char) - 96
    else:
        return ord(char) - 38
    

def group_elf_rucksacks(filename):
    """
    
    """
    priority_sum = 0
    with open(filename) as file:

        count = 0
        elf_group = []
        for rucksack in file:
            
            for char in rucksack:
                if count == 3:
                    break
                elif char == "\n":
                    elf_group.append(rucksack)
                    count += 1
                    
    return elf_group


def main():
    print(group_elf_rucksacks("Test_Input/basic_rucksack.txt"))



if __name__ == "__main__":
    main()
            
