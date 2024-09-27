import csv


def read_stock_data(file_path: str):
    """
    Reads stock data from a CSV file and returns a list of stock dictionaries.
    Args:
        file_path (str): The path to the CSV file containing stock data.
    Returns:
        List[dict]: A list of dictionaries, each containing the name, cost,
                    and profit of a stock.
    """
    stocks = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stock = {
                'name': row['Actions #'],
                'cost': float(row['Coût par action (en euros)']),
                'profit': float(row['Bénéfice (après 2 ans)'].strip('%')) / 100 * float(
                    row['Coût par action (en euros)'])
            }
            stocks.append(stock)

    return stocks


def knapsack(stocks: list, budget: float):
    """
    Optimized function to find the combination of stocks that maximizes profit
    while staying within the given budget using dynamic programming (knapsack algorithm).
    Args:
        stocks (list): A list of stock dictionaries, where each stock contains 'name', 'cost', and 'profit'.
        budget (float): The maximum amount of money (in euros) that can be spent on stocks.
    Returns:
        tuple: A tuple containing the best combination of stocks (list of dictionaries)
               and the corresponding maximum profit (float).
    """
    # Convert budget to integer for use in dynamic programming table (knapsack problem)
    budget = int(budget)

    # Create a DP table where dp[i][j] will store the maximum profit for the first i stocks and a budget of j
    n = len(stocks)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Track which stocks were picked
    picks = [[[] for _ in range(budget + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        stock = stocks[i - 1]
        cost = int(stock['cost'])
        profit = stock['profit']

        for j in range(1, budget + 1):
            if cost <= j:
                # Option 1: Don't take the stock
                option1 = dp[i - 1][j]

                # Option 2: Take the stock
                option2 = dp[i - 1][j - cost] + profit

                if option2 > option1:
                    dp[i][j] = option2
                    picks[i][j] = picks[i - 1][j - cost] + [stock]
                else:
                    dp[i][j] = option1
                    picks[i][j] = picks[i - 1][j]
            else:
                # If the stock can't be taken, carry forward the previous solution
                dp[i][j] = dp[i - 1][j]
                picks[i][j] = picks[i - 1][j]

    # The maximum profit is found at dp[n][budget]
    return picks[n][budget], dp[n][budget]


def main():
    """
    Main function that drives the optimized program. Reads stock data, finds the best combination
    of stocks to maximize profit using dynamic programming, and prints the result.
    Args:
        None
    Returns:
        None
    """
    # Set the budget to 500 euros
    budget = 500

    # Read stock data from the CSV file
    stocks = read_stock_data("../Liste+d'actions+-+P7+Python+-+Feuille+1.csv")

    best_combination, max_profit = knapsack(stocks, budget)

    # best combination of stocks and their profit
    if best_combination:
        print("\nBest Investment Combination (Optimized):")
        for stock in best_combination:
            print(f"{stock['name']} (Cost: {stock['cost']}, Profit: {stock['profit']})")
        print(f"Total Profit: {max_profit:.2f} euros")
    else:
        print("No valid investment combination found.")


if __name__ == "__main__":
    main()
