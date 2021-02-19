arr1 = [1, 3, 4, 5, 4, 1]


def max_sub_array(arr, sub_len):
    start, end, max_num = 0, sub_len - 1, 0
    for num in range(0, len(arr) - 1):
        curr = arr[num] + arr[num + 1]
        if curr > max_num:
            max_num = curr

    return max_num


def sliding_window_sub_max(arr, sub_len):
    start, end, max_val, curr = 0, sub_len - 1, 0, 0
    for x in range(0, len(arr)):
        if x <= end:
            curr += arr[x]
        else:
            curr = curr - arr[start]
            curr += arr[x]
            start += 1

        if curr > max_val:
            max_val = curr

    return max_val




if __name__ == '__main__':
    print(max_sub_array(arr1, 3))

    print(sliding_window_sub_max(arr1, 3))
