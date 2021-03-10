new_arr = [1, 2, [3, 4], 5, 6, [7, 8]]

new_arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def print_arr(arr):
    sum = 0
    d_sum, depth = 0, 1
    for x in arr:
        if type(x) is not list:
            sum += x
        else:
            depth += 1
            for y in x:
                d_sum += y
            sum += (d_sum * depth)
            d_sum = 0
            depth -= 1


def print_arr_rec(arr, depth=1):
    sum = 0
    for x in arr:
        if type(x) is not list:
            sum += x
        else:
            sum += print_arr_rec(x, depth+1)
    return sum * depth

if __name__ == '__main__':
    print(print_arr_rec(new_arr))
