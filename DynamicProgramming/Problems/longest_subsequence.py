def long_list(i, Arr):
    if i == 0:
        return 1
    max_el = 1
    for j in range(0, i):
        curr = long_list(j, Arr)
        if Arr[i] > Arr[j]:
            curr += 1
        max_el = max(max_el, curr)
    return max_el


def long_list_dp(i, Arr, dp):
    if i == 0:
        return 1
    max_el = 1

    if dp[i] != 0:
        return dp[i]

    for j in range(0, i):
        curr = long_list_dp(j, Arr, dp)
        if Arr[i] > Arr[j]:
            curr += 1
        max_el = max(max_el, curr)
        dp[i] = max_el
    return dp[i]

def subsequent_num(arr):
    len_arr = len(arr)
    dp = [0 for _ in range(0, len_arr)]
    dp[0] = 1
    for i in range(0, len_arr):
        dp[i] = 1
        for j in range(0, i):
            curr = dp[j]
            if arr[i] > arr[j]:
                curr += 1
            dp[i] = max(dp[i], curr)
    return dp[i]




if __name__ == '__main__':
    Arr = [2, 4, 6, 5, 3, 8]
    dp = [0 for _ in range(0, len(Arr))]
    print(subsequent_num(Arr))
