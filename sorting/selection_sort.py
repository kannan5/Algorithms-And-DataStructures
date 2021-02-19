import sys

arr1 = [5,7,2,5,6,8,3]




def selection_sort(arr):
    current_idx, len_arr = 0, len(arr)
    while current_idx < len_arr - 1:
        smallest_idx = current_idx
        for x in range(current_idx +1, len_arr):
            if arr[smallest_idx] > arr[x]:
                smallest_idx = x
        arr[smallest_idx], arr[current_idx] = arr[current_idx], arr[smallest_idx]
        current_idx += 1
    return arr


if __name__ == '__main__':
    arr2 = [2,6,3,8,4,8,2,1,5,9]
    print(selection_sort(arr2))
