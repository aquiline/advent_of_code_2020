import sys
import time

from tqdm import tqdm

if __name__ == '__main__':
    start = time.time()
    input_file = sys.argv[1]

    count = 0
    for line in tqdm(open(input_file)):

        policy, password = line.strip().split(':')
        password = password.strip()
        index_string, character = policy.split(' ')
        index_1, index_2 = index_string.split('-')
        index_1 = int(index_1)
        index_2 = int(index_2)
        if not (password[index_1 - 1] == character and password[index_2 - 1] == character) and \
                not (password[index_2 - 1] != character and password[index_1 - 1] != character):
            count += 1
    print("Merry Christmas!!\n Valid number of passwords are: {}".format(count))
    print("Time taken: {}".format(time.time() - start))
