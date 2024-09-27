# INCLUDES 0s AND NEGATIVE NUMBS

# def knapsack(stocks: list, budget: float):
#     """
#     Optimized function to find the combination of stocks that maximizes profit
#     while staying within the given budget using dynamic programming (knapsack algorithm).
#     Args:
#         stocks (list): A list of stock dictionaries, where each stock contains 'name', 'cost', and 'profit'.
#         budget (float): The maximum amount of money (in euros) that can be spent on stocks.
#     Returns:
#         tuple: A tuple containing the best combination of stocks (list of dictionaries)
#                and the corresponding maximum profit (float).
#     """
#     # Convert budget to integer for use in dynamic programming table (knapsack problem)
#     budget = int(budget)
#
#     # Separate stocks with zero cost and handle them outside the DP process
#     zero_cost_stocks = [stock for stock in stocks if stock['cost'] == 0]
#     non_zero_cost_stocks = [stock for stock in stocks if stock['cost'] > 0]
#
#     # Create a DP table where dp[i][j] will store the maximum profit for the first i stocks and a budget of j
#     n = len(non_zero_cost_stocks)
#     dp = [[0] * (budget + 1) for _ in range(n + 1)]
#
#     # Track which stocks were picked
#     picks = [[[] for _ in range(budget + 1)] for _ in range(n + 1)]
#
#     # Fill the DP table
#     for i in range(1, n + 1):
#         stock = non_zero_cost_stocks[i - 1]
#         cost = int(stock['cost'])  # Convert to integer
#         profit = stock['profit']
#
#         for j in range(budget + 1):
#             # Option 1: Don't take the stock
#             option1 = dp[i - 1][j]
#
#             # Option 2: Take the stock (only if the cost is <= current budget 'j')
#             if cost <= j:  # Ensure we don't try to access negative indices
#                 option2 = dp[i - 1][j - cost] + profit
#             else:
#                 option2 = 0  # Invalid option if cost is greater than j
#
#             # Take the better of the two options
#             if option2 > option1:
#                 dp[i][j] = option2
#                 picks[i][j] = picks[i - 1][j - cost] + [stock]
#             else:
#                 dp[i][j] = option1
#                 picks[i][j] = picks[i - 1][j]
#
#     # The maximum profit is found at dp[n][budget]
#     best_combination = picks[n][budget]
#     max_profit = dp[n][budget]
#
#     # Add zero-cost stocks to the result
#     if zero_cost_stocks:
#         best_combination.extend(zero_cost_stocks)
#         max_profit += sum(stock['profit'] for stock in zero_cost_stocks)
#
#     return best_combination, max_profit