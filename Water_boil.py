"""
Ok so this file is for "the watched pot never boils"

here you are given the number in first line that number shows that the person boiled the water that many times last week.

following by a pair of numbers will be given which means a person looked away between those numbers. i.e 1 7 means from second 1 to 7
the person looked away (I am assuming    the burner should be on during that period and otherwise the burner should be off)

for output side:
if the water started boiling at the same point of time (the last second of last time should be same) return "edward is right"
otherwise "gunilla has a point"

"""
import sys
def main():
    timeOfLookedAway = int(input())
    summation = 0
    count = 0
    lines = sys.stdin.readlines()
    for line in lines:
        count += 1
        a, b = line.split()
        while timeOfLookedAway > 0:
            print(a)
            print(b)
            summation += abs(int(a) - int(b))
            timeOfLookedAway -= 1
    print(summation)
    
    if summation < 7:
        print("gunilla has a point")
        #break
    else:
        print("edward is right")
        #break

if __name__ == '__main__':
    main()