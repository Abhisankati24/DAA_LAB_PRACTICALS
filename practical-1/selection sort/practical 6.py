def coin_change(N, coins):
    n = len(coins)

    # dp[i][j] = number of ways to make amount j
    # using first i coins
    dp = [[0 for j in range(N + 1)] for i in range(n + 1)]

    # There is one way to make amount 0: choose no coins
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, N + 1):

            # If coin value is greater than amount
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

            # Otherwise:
            # 1. Don't use the coin
            # 2. Use the coin
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]

    return dp[n][N]


N = int(input("Enter the amount: "))

n = int(input("Enter the number of coins: "))

coins = []

for i in range(n):
    x = int(input(f"Enter coin {i + 1}: "))
    coins.append(x)

result = coin_change(N, coins)

print("Number of ways:", result)