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

    all_seat_ids = list()
    for line in tqdm(open(input_file)):
        seat_string = line.strip()
        row = decode_binary_partitioned_string(seat_string[0:7], MINIMUM, MAXIMUM_ROW, ROW_UPPER, ROW_LOWER)
        col = decode_binary_partitioned_string(seat_string[7:10], MINIMUM, MAXIMUM_COL, COL_UPPER, COL_LOWER)
        all_seat_ids.append(get_seat_id(row, col))

    sorted_seat_ids = sorted(all_seat_ids)
    prev_seat_id = sorted_seat_ids[0]

    my_seat_id = int()
    for i in range(1, len(sorted_seat_ids)):
        current_seat_id = sorted_seat_ids[i]
        if (current_seat_id - prev_seat_id) == 2:
            my_seat_id = prev_seat_id + 1
            break
        else:
            prev_seat_id = current_seat_id
    print("Merry Christmas!!\n My seat id: {}".format(int(my_seat_id)))
    print("Time taken: {}".format(time.time() - start))
