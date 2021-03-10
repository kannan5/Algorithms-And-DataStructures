new_arr = [1, 2, 4, 5, 6, 7, 8, 9]
new_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binarysearch(arr, search_val):
    while arr is not None:
        size = len(arr)
        pos = size // 2
        move_ptr = arr[pos]
        if move_ptr == search_val:
            return str(search_val) + " Is Found "
        if move_ptr > search_val:
            arr = arr[:pos]
        if move_ptr < search_val:
            arr = arr[pos:]


if __name__ == '__main__':
    print(binarysearch(new_arr, 4))
