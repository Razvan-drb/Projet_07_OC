import csv

def read_stock_data(file_path: str):
    """
    Reads stock data from a CSV file and returns a list of stock dictionaries.
    Args:
        file_path (str): The path to the CSV file containing stock data.
    Returns:
        List[dict]: A list of dictionaries, each containing the name, cost, and profit of a stock.
    """
    stocks = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stock = {
                'name': row['name'],
                'cost': float(row['price']),
                'profit': float(row['profit'])
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

    budget = int(budget)

    valid_stocks = [stock for stock in stocks if stock['cost'] > 0]

    #  a dynamic programming table (dp_table)
    # will store the maximum profit possible for the first stock_idx stocks on available_budget.
    total_stocks = len(valid_stocks)
    dp_table = [[0] * (budget + 1) for _ in range(total_stocks + 1)]

    selected_stocks = [[[] for _ in range(budget + 1)] for _ in range(total_stocks + 1)]

    for stock_idx in range(1, total_stocks + 1):
        current_stock = valid_stocks[stock_idx - 1]
        stock_cost = int(current_stock['cost'])
        stock_profit = current_stock['profit']

        for available_budget in range(budget + 1):
            # Option 1: Don't select the current stock
            profit_without_stock = dp_table[stock_idx - 1][available_budget]

            # Option 2: Select the stock if its cost is within the available budget
            if stock_cost <= available_budget:
                profit_with_stock = dp_table[stock_idx - 1][available_budget - stock_cost] + stock_profit
            else:
                profit_with_stock = 0

            if profit_with_stock > profit_without_stock:
                dp_table[stock_idx][available_budget] = profit_with_stock
                selected_stocks[stock_idx][available_budget] = selected_stocks[stock_idx - 1][
                                                                   available_budget - stock_cost] + [current_stock]
            else:
                dp_table[stock_idx][available_budget] = profit_without_stock
                selected_stocks[stock_idx][available_budget] = selected_stocks[stock_idx - 1][available_budget]

    # The best combination of stocks and the corresponding maximum profit
    optimal_combination = selected_stocks[total_stocks][budget]
    maximum_profit = dp_table[total_stocks][budget]

    return optimal_combination, maximum_profit



def main():
    """
    Main function that drives the optimized program. Reads stock data, finds the best combination
    of stocks to maximize profit using dynamic programming, and prints the result.
    Args:
        None
    Returns:
        None
    """

    budget = 500

    stocks = read_stock_data("dataset1_Python+P7.csv")

    best_combination, max_profit = knapsack(stocks, budget)

    total_cost = sum(stock['cost'] for stock in best_combination)

    # Best combination of stocks and their profit
    if best_combination:
        print("\nBest Investment Combination (Optimized):")
        for stock in best_combination:
            print(f"{stock['name']} (Cost: {stock['cost']}, Profit: {stock['profit']})")
        print(f"Total Cost: {total_cost:.2f} euros")
        print(f"Total Profit: {max_profit:.2f} euros")
    else:
        print("No valid investment combination found.")


if __name__ == "__main__":
    main()
