class dp:
    def knapsack(self, capacity, weight, value, i):
        if capacity == 0 or i == -1: return 0
        current_weight = weight[i]
        if capacity >= weight[i]:
            return max(value[i] + self.knapsack(capacity - current_weight, weight, value, i - 1),
                       self.knapsack(capacity, weight, value, i - 1))
        else:
            return self.knapsack(capacity, weight, value, i - 1)

    def knapsack_dp_memo(self, capacity, weight, value, i, dp):
        if capacity == 0 or i == -1 : return 0
        if dp[capacity][i] != -1: return dp[weight][i]
        if capacity >= weight[i]:
            res = max(value[i] + self.knapsack_dp_memo(capacity - weight[i], weight, value, i - 1, dp),
                      self.knapsack_dp_memo(capacity, weight, value, i - 1, dp))
            return res
        else:
            res = self.knapsack_dp_memo(capacity, weight, value, i - 1, dp)
            return res

    # def knapsack_dp_tab(self, capacity, weight, value):
    #     dp = [[-1 for i in range(len(weights) + 1)] for j in range(0, 21)]
    #     for i in range(1, len(weights) + 1):
    #         for w in range(0, len(capacity) +1):
    #             if weight[i - 1] <= capacity:
                    # dp[w][i] = max(dp[])




if __name__ == '__main__':
    a = dp()
    weights = [3, 7, 10, 6]
    values = [4, 14, 10, 5]
    print(a.knapsack(20, weights, values, len(weights) - 1))
    dp = [[-1 for i in range(len(weights)+1)] for j in range(0,  21)]
    adp = [[-1 for i in range(0, 4 + 1)] for j in range(0, 20 + 1)]
    print(a.knapsack_dp_memo(20, weights, values, len(weights) - 1, dp))