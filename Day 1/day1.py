from math import *

def main():
    file = open("input.txt", "r")
    sum = 0

    for line in file.readlines():
        sum += processLine(line);

    output = open("output.txt", "w")
    output.write(str(sum))

def processLine(line):
    return floor(int(line) / 3) - 2

main()
