import sys
import time

from tqdm import tqdm

REQUIRED_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}


def parse_line(input_line):
    keys = set()
    key_value_pairs = input_line.strip().split(' ')
    for key_value_pair in key_value_pairs:
        key, value = key_value_pair.split(':')
        keys.add(key)
    return keys


def is_valid_passport(keys):
    if len(REQUIRED_FIELDS.intersection(keys)) >= 7:
        return True
    return False


if __name__ == '__main__':
    start = time.time()
    parsed_keys = set()
    valid_passports = 0
    for line in tqdm(open(sys.argv[1])):
        if line == "\n":
            if is_valid_passport(parsed_keys):
                valid_passports += 1
            parsed_keys = set()
        else:
            parsed_keys.update(parse_line(line))

    if is_valid_passport(parsed_keys):
        valid_passports += 1

    print("Merry Christmas!!\n Valid passports: {}".format(valid_passports))
    print("Time taken: {}".format(time.time() - start))
