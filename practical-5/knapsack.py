def knapsack(weights, profit, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                profit[i] + dp[w - weights[i]]
            )
    return dp[capacity]
weights = [1, 2, 5, 6]
profit = [2, 3, 4, 5]
capacity = 8
print("Maximum profit:", knapsack(weights, profit, capacity))