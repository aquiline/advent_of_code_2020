import sys
import time


def read_numbers(_file):
    numbers = list()
    for line in open(_file):
        numbers.append(int(line.strip()))
    return numbers


if __name__ == '__main__':
    start = time.time()
    input_numbers = read_numbers(sys.argv[1])

    for i in range(0, len(input_numbers)-2):
        for j in range(i+1, len(input_numbers)-1):
            if input_numbers[i] + input_numbers[j] == 2020:
                print("Merry Christmas!!\n The magic number is: {}".format(input_numbers[i] * input_numbers[j]))

    print("Time taken: {}".format(time.time() - start))
