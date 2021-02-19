import time


def knapsack(W, i, weights, values):
    if W == 0 or i == -1:
        return 0
    if weights[i] <= W:
        return max(values[i] + knapsack(W - weights[i], i - 1, weights, values),
                   knapsack(W, i - 1, weights, values))
    else:
        return knapsack(W, i - 1, weights, values)


def knapsack_memo(W, i, weights, values, dp):
    if W == 0 or i == -1:
        return 0
    if dp[W][i] != -1:
        return dp[W][i]
    if weights[i] <= W:
        res = max(values[i] + knapsack_memo(W - weights[i], i - 1, weights, values, dp),
                  knapsack_memo(W, i - 1, weights, values, dp))
        dp[W][i] = res
        return res
    else:
        res = knapsack_memo(W, i - 1, weights, values, dp)
        dp[W][i] = res
        return res


def knapsack_DP(W, weights, values):
    dp = [[0 for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
    dp[W][0] = 0
    for i in range(1, len(weights) + 1):
        for w in range(0, W + 1):
            if weights[i - 1] <= w:
                dp[w][i] = max(dp[w][i - 1], dp[w - weights[i - 1]][i - 1] + values[i - 1])
            else:
                dp[w][i] = dp[w][i - 1]
    return dp[W][len(weights)]


def knapsack_DP_reconstruct(W, weights, values):
    dp = [[0 for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
    n = len(weights)
    decisions = [[False for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
    dp[W][0] = 0
    for i in range(1, n + 1):
        for w in range(0, W + 1):
            if weights[i - 1] <= w:
                if dp[w - weights[i - 1]][i - 1] + values[i - 1] > dp[w][i - 1]:
                    # We record the decision here that its beneficial to pick the ith item
                    decisions[w][i] = True
                    dp[w][i] = dp[w - weights[i - 1]][i - 1] + values[i - 1]
                else:
                    dp[w][i] = dp[w][i - 1]
            else:
                dp[w][i] = dp[w][i - 1]

    i = n
    w = W
    while i > 0 and w > 0:
        if decisions[w][i]:
            print("Picked up {} , Weight {} , Value {}".format(i - 1, weights[i - 1], values[i - 1]))
            w -= weights[i - 1]
            i -= 1;
        else:
            i -= 1
    return dp[W][n]


tic, toc = float, float

weights = [3, 7, 10, 6]
values = [4, 14, 10, 5]
W = 20
N = len(weights)
# Recursive solution
tic = time.perf_counter()
print(knapsack(W, N - 1, weights, values))
toc = time.perf_counter()
print(f"the Knapsack Time Interval {toc - tic:0.4f} seconds")

# Memoization
dp = [[-1 for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]

tic = time.perf_counter()
print(knapsack_memo(W, N - 1, weights, values, dp))
toc = time.perf_counter()
print(f"the Knapsack Memoization Time Interval {toc - tic:0.4f} seconds")

# Bottom up
tic = time.perf_counter()
print(knapsack_DP(W, weights, values))
toc = time.perf_counter()
print(f"the Knapsack Bottom UP Time Interval {toc - tic:0.4f} seconds")

# Bottom up with solution reconstruction
tic = time.perf_counter()
print(knapsack_DP_reconstruct(W, weights, values))
toc = time.perf_counter()
print(f"the Knapsack Bottom Up RC Time Interval {toc - tic:0.4f} seconds")
