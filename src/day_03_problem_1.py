import sys
import time

from tqdm import tqdm


def get_next_path_index(total_length, position):
    next_position = position % total_length
    if next_position == 0:
        return total_length
    return next_position


def check_if_tree_present(path, position):
    if path[position] == '#':
        return True
    return False


if __name__ == '__main__':
    start = time.time()
    input_file = sys.argv[1]

    tree_count = 0
    current_slope_pos = 1
    slope_increment = 3
    for index, line in tqdm(enumerate(open(input_file))):
        if index == 0:
            continue
        input_path = line.strip()
        path_length = len(input_path)
        current_slope_pos += slope_increment

        if current_slope_pos <= path_length:
            if check_if_tree_present(input_path, current_slope_pos - 1):
                tree_count += 1
        else:
            adjusted_path_index = get_next_path_index(path_length, current_slope_pos)
            if check_if_tree_present(input_path, adjusted_path_index - 1):
                tree_count += 1

    print("Merry Christmas!!\n Trees encountered: {}".format(tree_count))
    print("Time taken: {}".format(time.time() - start))
