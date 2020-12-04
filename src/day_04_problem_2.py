import re
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
MINIMUM_BYR = 1920
MAXIMUM_BYR = 2002

MINIMUM_IYR = 2010
MAXIMUM_IYR = 2020

MINIMUM_EYR = 2020
MAXIMUM_EYR = 2030

MINIMUM_CM_HGT = 150
MAXIMUM_CM_HGT = 193

MINIMUM_IN_HGT = 59
MAXIMUM_IN_HGT = 76

VALID_ECL = {
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth',
}


def parse_line(input_line):
    keys_map = dict()
    key_value_pairs = input_line.strip().split(' ')
    for key_value_pair in key_value_pairs:
        key, value = key_value_pair.split(':')
        value = value.strip()
        keys_map[key] = value
    return keys_map


def is_int_valid(value, min_value, max_value):
    try:
        int_value = int(value)
        if min_value <= int_value <= max_value:
            return True
        return False
    except ValueError:
        return False


def validate_byr(passport):
    byr = passport['byr']
    if is_int_valid(byr, MINIMUM_BYR, MAXIMUM_BYR):
        return True
    return False


def validate_iyr(passport):
    iyr = passport['iyr']
    if is_int_valid(iyr, MINIMUM_IYR, MAXIMUM_IYR):
        return True
    return False


def validate_eyr(passport):
    eyr = passport['eyr']
    if is_int_valid(eyr, MINIMUM_EYR, MAXIMUM_EYR):
        return True
    return False


def validate_hgt(passport):
    hgt = passport['hgt']
    if not re.search(r'^\d+(cm|in)$', hgt):
        return False
    height, unit, _ = re.split(r'(cm|in)', hgt)
    _min, _max = int(), int()
    if unit == 'cm':
        _min = MINIMUM_CM_HGT
        _max = MAXIMUM_CM_HGT
    elif unit == 'in':
        _min = MINIMUM_IN_HGT
        _max = MAXIMUM_IN_HGT
    if is_int_valid(height, _min, _max):
        return True
    return False


def validate_hcl(passport):
    hcl = passport['hcl']
    if re.search(r'^#[0-9a-f]{6}$', hcl):
        return True
    return False


def validate_ecl(passport):
    ecl = passport['ecl']
    if ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return True
    return False


def validate_pid(passport):
    pid = passport['pid']
    if re.search(r'^[0-9]{9}$', pid):
        return True
    return False


VALIDATING_FUNCTIONS = [
    validate_byr,
    validate_iyr,
    validate_eyr,
    validate_hgt,
    validate_hcl,
    validate_ecl,
    validate_pid,
]


def is_valid_passport(passport):
    if len(REQUIRED_FIELDS.intersection(passport.keys())) < 7:
        return False
    for validating_function in VALIDATING_FUNCTIONS:
        if not validating_function(passport):
            return False
    return True


if __name__ == '__main__':
    start = time.time()
    parsed_passport = dict()
    valid_passports = 0
    for line in tqdm(open(sys.argv[1])):
        if line == "\n":
            if is_valid_passport(parsed_passport):
                valid_passports += 1
            parsed_passport = dict()
        else:
            parsed_passport.update(parse_line(line))

    if is_valid_passport(parsed_passport):
        valid_passports += 1

    print("Merry Christmas!!\n Valid passports: {}".format(valid_passports))
    print("Time taken: {}".format(time.time() - start))
