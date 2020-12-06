import sys
import time

from tqdm import tqdm


if __name__ == '__main__':
    start = time.time()
    unique_yesses_per_group = set()
    sum_of_yesses = 0
    for line in tqdm(open(sys.argv[1])):
        if line == "\n":
            sum_of_yesses += len(unique_yesses_per_group)
            unique_yesses_per_group = set()
        else:
            unique_yesses_per_group.update(set(line.strip()))
    sum_of_yesses += len(unique_yesses_per_group)

    print("Merry Christmas!!\n Sum of unique yesses per group: {}".format(sum_of_yesses))
    print("Time taken: {}".format(time.time() - start))
