
def get_data(filename):
    cal_list = []
    with open(filename) as file:
        # data = file.readlines()
        # for line in data:
        #     line.strip("\n")
        #     print(line)

        for line in file:
            #line = line.split()
            cal_list.append(line.strip())
    sums = []
    summed = 0
    for values in cal_list:
        if values == "":
            sums.append(summed)
            summed = 0
            continue
        else:
            summed += int(values)
            
            
    return max(sums)



def main():
    answer = get_data("Test_Input/big_input.txt")
    print(answer)
    #get_data("small_input.txt")

main()
