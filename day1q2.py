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
    three_sums = 0
    count = 0
    sums.sort()
    three_sums = sums[-1] + sums[-2] + sums[-3]     
        
    return three_sums



def main():
    answer = get_data("big_input.txt")
    print(answer)
    #get_data("small_input.txt")

main()