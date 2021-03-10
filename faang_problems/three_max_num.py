arr1 = [31, 2, 13, 4, 45, 223, 42]



def three_max_sum(arr):
    max_arr = [-1, -1, -1]
    temp, temp1 = -1, -1
    for curr in arr:
        if curr > max_arr[2]:
            temp = max_arr[2]
            max_arr[2] = curr
            if temp > max_arr[1] and temp>0:
                temp1 = max_arr[1]
                max_arr[1] = temp
            if temp1 > max_arr[0] and temp1>0:
                max_arr[0] = temp1

        elif curr > max_arr[1]:
            temp = max_arr[1]
            if curr > max_arr[1]:
                temp1 = max_arr[1]
                max_arr[1] = curr
            if temp1 > max_arr[0]:
                max_arr[0] = temp1

        elif curr > max_arr[0]:
           max_arr[0] = curr

    return max_arr


def three_max_sum_imp(arr):
    max_arr = [-1, -1, -1]
    temp, temp1 = -1, -1
    for curr in arr:
        if curr > max_arr[2]:
            temp = max_arr[2]
            max_arr[2] = curr
            curr = temp

        if curr > max_arr[1]:
            temp = max_arr[1]
            max_arr[1] = curr
            curr = temp

        if curr > max_arr[0]:
           max_arr[0] = curr

    return max_arr


if __name__ == '__main__':
    print(three_max_sum_imp(arr1))





