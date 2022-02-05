import sys
def main():
    """
    lines = []
    while True:
        line = sys.stdin.readlines()
        if line:
            lines.append(line)
        else:
            break
    print(lines)"""
    lines = sys.stdin.readlines()
    for line in lines:
        x1, y1, x2, y2, p = line.split()
        distanceX = abs(float(x1) - float(x2)) ** float(p)
        distanceY = abs(float(y1)-float(y2)) ** float(p)
        distance = (distanceX + distanceY) ** (1/float(p))
        formatted_string = "{:.10f}".format(distance)
        float_value = float(formatted_string)
        print(float_value)
if __name__ == '__main__':
    main()
"""
here the problem is when I get zero as an input the compile error pops up. 
"""
