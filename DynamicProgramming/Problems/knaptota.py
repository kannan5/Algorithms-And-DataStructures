class knaptota:

    def knapcheck(self, total_weight, i, weights, values):
        if total_weight == 0 or i < 0:
            return 0
        if weights[i] <= total_weight:
            return max(values[i] + self.knapcheck(total_weight - weights[i], i - 1, weights, values),
                      self.knapcheck(total_weight, i - 1, weights, values))
        else:
            return self.knapcheck(total_weight, i - 1, weights, values)

    def knapcheck_dp(self, total_weight, i, weights, values, dp_table):
        if total_weight == 0 or i < 0:
            return 0

        if dp_table[total_weight][i] != -1:
            return dp_table[total_weight][i]

        if weights[i] <= total_weight:
            res = max(values[i] + self.knapcheck_dp(total_weight - weights[i], i - 1, weights, values, dp_table),
                      self.knapcheck_dp(total_weight, i - 1, weights, values, dp_table))
            dp_table[total_weight][i] = res
            return res
        else:
            res = self.knapcheck_dp(total_weight, i - 1, weights, values, dp_table)
            dp_table[total_weight][i] = res
            return res

    def knapsack_memo(self, W, i, weights, values, dp):
        if W == 0 or i == -1: return 0
        if dp[W][i] != -1:
            return dp[W][i]
        if weights[i] <= W:
            res = max(values[i] + self.knapsack_memo(W - weights[i], i - 1, weights, values, dp),
                      self.knapsack_memo(W, i - 1, weights, values, dp))
            dp[W][i] = res
            return res
        else:
            res = self.knapsack_memo(W, i - 1, weights, values, dp)
            dp[W][i] = res
            return res


if __name__ == '__main__':
    a = knaptota()
    adp = [[-1 for i in range(0, 4 + 1)] for j in range(0, 20 + 1)]
    print(a.knapcheck_dp(20, 3, [3, 7, 10, 6], [4, 14, 10, 5], adp))
    print(a.knapsack_memo(20, 3, [3, 7, 10, 6], [4, 14, 10, 5], adp))
    print(a.knapcheck(20, 3, [3, 7, 10, 6], [4, 14, 10, 5]))
