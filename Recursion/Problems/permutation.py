
def Permutation(input_list, partial, used):
    input_len = len(input_list)
    if len(partial) == input_len:
        print(partial)
    else:
        for i in range(0, input_len):
            if not used[i] and not (input_list[i] == input_list[i - 1] and not used[i - 1]):
                used[i] = True
                partial.append(input_list[i])
                Permutation(input_list, partial, used)
                used[i] = False
                partial.pop(-1)


if __name__ == '__main__':
    Permutation([1, 2, 3, 4], [], 4 * [False])
