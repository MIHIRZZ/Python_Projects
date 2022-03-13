#Get the numbers out of file using regular expression and sum up all of them

import re
x = open("actual.txt")    #You can use any numeric data file, which may have text, symbols, or anything
l1 = list()
sum = 0
for line in x:
    #line.split()
    y = re.findall('([0-9]+)', line)
    #if len(y) == -1: continue  there are empty strings but I don't know how to remove them
    #print(y)
    l1.append(y)
for v in l1:
    for v1 in v:
        sum += int(v1)
print(sum)
 
# for actual.txt sum = 394998
# for sample.txt sum = 445833
