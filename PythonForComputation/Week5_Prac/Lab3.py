# 1st solution
def find_sum(line):
    list = [int(x) for x in line.split(" ")]
    for i in range(len(list)):
        a = list.pop(i)
        # print(a)
        # print(list)
        # print("*************")
        if sum(list) == a:
            print("The sum is {}".format(str(a)))
            break
        else:
            list.insert(i, a)


# 2nd solution
def find_sum_2(line):
    list = [int(x) for x in line.split(" ")]
    s = sum(list) / 2
    print("The answer is {}".format(str(s)))


line = "2 6 15 4 -2 5"
find_sum(line)
find_sum_2(line)
