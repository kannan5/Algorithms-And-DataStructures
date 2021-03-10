

import sys
curr = sys.maxsize

def find_travel(i, arr, iter):
    if i ==0:
        return 0
    min_path = sys.maxsize
    for x in range(1, min(i, iter) + 1):
        min_path = min(min_path, arr[i] + find_travel(i - x, arr, iter))
    return min_path


def find_travel_memo(i, arr, dp, iter):
    if i ==0:
        return 0
    if dp[i] != -1:
        return dp[i]
    min_path = sys.maxsize
    for x in range(1, min(i, iter) + 1):
        min_path = min(min_path, arr[i] + find_travel(i - x, arr, iter))
        dp[i] = min_path
    return dp[i]


def find_travel_tab(arr, iter):
    len_arr = len(arr)
    dp = [sys.maxsize for _ in range(0, len_arr)]
    dp[0] = 0
    for i in range(0, len_arr):
        for j in range(1, min(iter, i)+1):
            dp[i] = min(dp[i],  arr[i] + dp[i - j])
    return dp[len_arr - 1]

def find_travel_tab_rec(arr, iter):
    len_arr = len(arr)
    dp = [sys.maxsize for _ in range(0, len_arr)]
    dp_choice = [0 for _ in range(0, len_arr)]
    dp[0] = 0
    for i in range(0, len_arr):
        for j in range(1, min(iter, i)+1):
            if dp[i] > arr[i] + dp[i - j]:
                dp[i] = arr[i] + dp[i - j]
                dp_choice[i] = i - j
    print("The ReConstructed Path:")
    k = len_arr - 1
    print(str(k)+"->", end="")
    while k>0:
        k = dp_choice[k]
        print(str(k)+"->", end="")
    return dp[len_arr - 1]




if __name__ == '__main__':
    arr = [20, 30, 40, 25, 15, 20, 28]
    dp = [-1 for _ in range(0, len(arr))]
    print(find_travel_memo(len(arr) - 1, arr, dp, 3))
    print(find_travel_tab_rec(arr, 3))
