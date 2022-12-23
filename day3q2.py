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
    These three lines are then converted into sets.
    Then I look through the first set to see what character appears in all three sets.
    """
    priority_sum = 0
    elf_group = []
    file = open(filename)

    content = file.readlines()
    for line in content:
        line = line.strip()
    count = 0
    num = len(content)
    while count < num:
        elf_group.append(content[count:count+3])
        count += 3

    for list in elf_group:
        set1 = set(list[0])
        set2 = set(list[1])
        set3 = set(list[2])
        for char in set1:
            if char != "\n":
                if char in set2 and char in set3:
                    priority_sum += priority_val(char)

    
    file.close()       
    return priority_sum


def main():
    print(group_elf_rucksacks("Test_Input/rucksack_input.txt"))



if __name__ == "__main__":
    main()
            
