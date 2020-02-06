from math import *

def main():
    file = open("input.txt", "r")
    output = open("output.txt", "w")
    sum = 0
    sum2 = 0

    for line in file.readlines():
        isZero = False
        value = int(line)
        sum = calculate(value)

        while isZero is False:
            if calculate(value) > 0:
                sum2 += calculate(value);
                value = calculate(value)
            else:
                isZero = True

    output.write(str(sum)+ "\n")
    output.write(str(sum2))

def calculate(value):
    return floor(value / 3) - 2

main()
