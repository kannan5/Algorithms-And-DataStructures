import sys


def rod_profit(profits, len):
    if len == 0:
        return 0
    max_profit = -1
    for i in range(0, len):
        max_profit = max(profits[i] + rod_profit(profits, len - i - 1), max_profit)
    return max_profit


def rod_profit_dp(profits_list, dp, len):
    if len == 0:
        return 0
    if dp[len] != -1:
        return dp[len]
    max_profit = -1
    for i in range(0, len):
        max_profit = max(max_profit, profits_list[i] + rod_profit_dp(profits_list, dp, len - i - 1))
    dp[len] = max_profit
    return max_profit

def rod_profit_dp_bottom(profits, l):
    dp = [0 for _ in range(0, l + 1)]
    for i in range(1, l+1):
        dp[i] = -sys.maxsize
        for y in range(0, i):
            dp[i] = max(dp[i], profits[y] + dp[i -y -1])
    return dp[l]

def max_profit_dp(L, p):
    dp = [0 for _ in range(0, L + 1)]
    for l in range(1, L + 1):
        dp[l] = -sys.maxsize
        for i in range(0, l):
            dp[l] = max(dp[l], p[i] + dp[l - i - 1])
    return dp[L]

def rod_profit_dp_bottom_rec(profits_list, l):
    dp_val = [0 for _ in range(0, l + 1)]
    for i in range(1, l+1):
        dp_val[i] = -1
        for y in range(0, l):
            curr = profits_list[y] + dp_val[l - i - 1]
            if curr > dp_val[l]:
                dp_val[l] = curr
    return dp_val[l]


if __name__ == '__main__':
    profits_list = [1, 5, 8, 9, 10, 14, 17, 20, 24, 30]
    len = 6
    dp = [-1 for _ in range(0, len + 1)]
    print(rod_profit(profits_list, len))
    print(rod_profit_dp(profits_list, dp, len))
    print(rod_profit_dp_bottom(profits_list, len))
    print(max_profit_dp(len, profits_list))
