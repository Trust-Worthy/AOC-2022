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
    This function reads all the lines in the file and groups those lines in groups of three.
    """
    priority_sum = 0
    elf_group = []
    file = open(filename)

    content = file.readlines()
    count = 0
    num = len(content)
    while count < num:
        elf_group.append(content[count:count+3])
        count += 3

    
    file.close()       
    return elf_group


def main():
    print(group_elf_rucksacks("Test_Input/basic_rucksack.txt"))



if __name__ == "__main__":
    main()
            
