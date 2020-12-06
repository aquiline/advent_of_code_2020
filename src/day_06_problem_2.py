import sys
import time

from tqdm import tqdm


if __name__ == '__main__':
    start = time.time()
    common_yesses_per_group = set()
    sum_of_yesses = 0
    new_line = True
    for line in tqdm(open(sys.argv[1])):
        if line == "\n":
            sum_of_yesses += len(common_yesses_per_group)
            common_yesses_per_group = set()
            new_line = True
        else:
            if new_line:
                common_yesses_per_group = set(line.strip())
                new_line = False
            else:
                common_yesses_per_group = common_yesses_per_group.intersection(set(line.strip()))
    sum_of_yesses += len(common_yesses_per_group)

    print("Merry Christmas!!\n Sum of common yesses per group: {}".format(sum_of_yesses))
    print("Time taken: {}".format(time.time() - start))
