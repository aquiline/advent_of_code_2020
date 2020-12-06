import math
import sys
import time

from tqdm import tqdm

MINIMUM = 0
MAXIMUM_ROW = 127
MAXIMUM_COL = 7

ROW_UPPER = 'B'
ROW_LOWER = 'F'

COL_UPPER = 'R'
COL_LOWER = 'L'


def get_upper_range(_min, _max):
    middle = math.ceil((float(_min) + float(_max)) / 2)
    return middle, _max


def get_lower_range(_min, _max):
    middle = math.floor((float(_min) + float(_max)) / 2)
    return _min, middle


def decode_binary_partitioned_string(binary_string, min_value, max_value, upper_range_character, lower_range_character):
    for character in binary_string:
        if character == upper_range_character:
            min_value, max_value = get_upper_range(min_value, max_value)
        elif character == lower_range_character:
            min_value, max_value = get_lower_range(min_value, max_value)
    if min_value != max_value:
        raise ValueError("Error decoding location: {}\t{}\t{}".format(binary_string, min_value, max_value))
    return max_value


def get_seat_id(_row, _col):
    return (_row * 8) + _col


if __name__ == '__main__':
    start = time.time()
    input_file = sys.argv[1]

    max_seat_id = 0
    for line in tqdm(open(input_file)):
        seat_string = line.strip()
        row = decode_binary_partitioned_string(seat_string[0:7], MINIMUM, MAXIMUM_ROW, ROW_UPPER, ROW_LOWER)
        col = decode_binary_partitioned_string(seat_string[7:10], MINIMUM, MAXIMUM_COL, COL_UPPER, COL_LOWER)
        max_seat_id = max(max_seat_id, get_seat_id(row, col))

    print("Merry Christmas!!\n Max seat id: {}".format(int(max_seat_id)))
    print("Time taken: {}".format(time.time() - start))
