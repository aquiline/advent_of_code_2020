import sys
import time

from tqdm import tqdm

if __name__ == '__main__':
    start = time.time()
    input_file = sys.argv[1]

    count = 0
    for line in tqdm(open(input_file)):
        policy, password = line.strip().split(':')
        min_max_string, character = policy.split(' ')
        _min, _max = min_max_string.split('-')
        _min = int(_min)
        _max = int(_max)
        if _min <= password.count(character) <= _max:
            count += 1
    print("Merry Christmas!!\n Valid number of passwords are: {}".format(count))
    print("Time taken: {}".format(time.time() - start))
