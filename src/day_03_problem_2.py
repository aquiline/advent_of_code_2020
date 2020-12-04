import sys
import time
from tqdm import tqdm

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


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

    final_answer = 1
    for right, down in tqdm(SLOPES):
        tree_count = 0
        current_slope_pos = 1
        slope_increment = right

        for index, line in enumerate(open(input_file)):
            if index == 0:
                continue
            if down % 2 == 0:
                if (index + 1) % down != 1:
                    continue
            else:
                if index % down != 0:
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
        final_answer *= tree_count

    print("Merry Christmas!!\n Multiplied trees encountered: {}".format(final_answer))
    print("Time taken: {}".format(time.time() - start))
