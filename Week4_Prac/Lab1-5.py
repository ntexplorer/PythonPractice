import csv
d = {}
with open('towns.csv') as t:
    t_csv = csv.reader(t)
    for row in t_csv:
        d[row[0]] = int(row[1])
print(d)
print("\n########################\n")
# 2
width = max([len(x) for x in d])
print(width)
for town, pop in d.items():
    print("{0:>{2}} : {1:<}".format(town, pop, width))
# in {0:>{2}} 0 stand for the first element in the format, :> means sticking to the right, {2}means push x units according to the 3 element(width)
# 3
print("\n########################\n")
print("{0}".format("Hello"))
print("{0:>{1}}".format("Hello", 10))
print("{0:>{1}}".format("Hello", 20))
