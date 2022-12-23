"""
I need to create a function that can read lines in a file and calculate whether one range is
a superset of another range. (or includes it)
"""

def is_superset(filename):
    times = 0
    with open(filename) as file:

        for line in file:
            line = line.strip()
            line = line.split(",")
            range1 = line[0]
            range2 = line[1]
            for i in range(len(range1)):
                if range1[i] == "-":
                    start_range1 = int(range1[:i])
                    end_range1 = int(range1[i+1:len(range1)])
                    range1_set = set()
                    for num in range(start_range1,end_range1 + 1):
                        range1_set.add(num)
            for i in range(len(range2)):
                if range2[i] == "-":
                    start_range2 = int(range2[:i])
                    end_range2 = int(range2[i+1:len(range2)])
                    range2_set = set()
                    for num in range(start_range2,end_range2+1):
                        range2_set.add(num)
            if range1_set.issuperset(range2_set):
                times += 1
            if range2_set.issubset(range1_set):
                times += 1
    return times

def main():
    print(is_superset("Test_Input/day4_real_input.txt"))

if __name__ == "__main__":
    main()