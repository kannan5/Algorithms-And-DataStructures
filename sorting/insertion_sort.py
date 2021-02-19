# Insertion Sort will take O(N)^2 Time Complexity and O(1) Space Complexity


def InsertionSort(input):
    input_len = len(input)
    for cur_pos in range(1, input_len):
        if input[cur_pos - 1] > input[cur_pos]:
            input[cur_pos], input[cur_pos - 1] = input[cur_pos - 1], input[cur_pos]
            if (cur_pos - 1) > 0:
                for prev_pos in range(cur_pos, 0, -1):
                    if input[prev_pos] < input[prev_pos - 1]:
                        input[prev_pos], input[prev_pos - 1] = input[prev_pos - 1], input[prev_pos]

    return input


if __name__ == '__main__':
    print(InsertionSort([8, 5, 2, 9, 6, 2, 3]))