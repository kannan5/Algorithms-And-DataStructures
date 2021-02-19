def house_robber(costs, n, cost):
    if n < 0:
        return 0
    cost = max(costs[n] + house_robber(costs, n - 2, cost), house_robber(costs, n - 1, cost))
    return cost

def house_robber_dp(dp, costs, n, cost):
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    dp[n] = max(costs[n] + house_robber_dp(dp, costs, n - 2, cost), house_robber_dp(dp, costs, n - 1, cost))
    return dp[n]

def house_robber_dp_bottom_up(costs):
    n = len(costs)
    dp = [0 for _ in range(0, n + 1)]
    dp[1] = costs[0]
    for i in range(2, n + 1):
        dp[i] = max(costs[i-1]+dp[i-2], dp[i-1])
    return dp[n]

def house_robber_dp_bottom_up_rec(costs):
    n = len(costs)
    dp = [0 for _ in range(0, n + 1)]
    dp_dec = [False for _ in range(0, n)]
    dp_dec[0] = True
    dp[1] = costs[0]
    for i in range(2, n + 1):
        curr = (costs[i - 1] + dp[i - 2])
        if curr > dp[i - 1]:
            dp[i] = curr
            dp_dec[i - 1] = True
        else:
            dp[i] = dp[i - 1]
            dp_dec[i - 1] = False
    i = n - 1
    while i >= 0:
        if dp_dec[i]:
            print("The House {0} is Selected Having {1}".format(i, costs[i]))
            i -= 2
        else:
            i -= 1

    return dp[n]

if __name__ == '__main__':
    costs = [20, 25, 30, 15, 10]
    dp = [-1 for _ in range(0, len(costs))]
    print(house_robber(costs, len(costs) - 1, 0))
    # print(house_robber_dp(dp,costs, len(costs) - 1, 0))
    print(house_robber_dp_bottom_up_rec(costs))
