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

    filtered_stocks = [stock for stock in stocks if stock['cost'] > 0]

    # Create a dynamic programming table where dp_table[i][available_budget]
    # store the maximum profit for the first the stocks and budget.
    num_stocks = len(filtered_stocks)
    dp_table = [[0] * (budget + 1) for _ in range(num_stocks + 1)]

    stock_selection = [[[] for _ in range(budget + 1)] for _ in range(num_stocks + 1)]

    # dynamic programming table
    for stock_index in range(1, num_stocks + 1):
        current_stock = filtered_stocks[stock_index - 1]
        current_cost = int(current_stock['cost'])
        current_profit = current_stock['profit']

        for available_budget in range(budget + 1):
            # Option 1: Don't take the current stock
            profit_without_stock = dp_table[stock_index - 1][available_budget]

            # Option 2: Take the stock, if cost allows
            if current_cost <= available_budget:
                profit_with_stock = dp_table[stock_index - 1][available_budget - current_cost] + current_profit
            else:
                profit_with_stock = 0

            # Choose the better option between taking the stock or not
            if profit_with_stock > profit_without_stock:
                dp_table[stock_index][available_budget] = profit_with_stock
                stock_selection[stock_index][available_budget] = stock_selection[stock_index - 1][
                                                                     available_budget - current_cost] + [current_stock]
            else:
                dp_table[stock_index][available_budget] = profit_without_stock
                stock_selection[stock_index][available_budget] = stock_selection[stock_index - 1][available_budget]

    # The best combination of stocks and the maximum profit
    best_stock_combination = stock_selection[num_stocks][budget]
    max_profit = dp_table[num_stocks][budget]

    return best_stock_combination, max_profit



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

    stocks = read_stock_data("dataset2_Python+P7.csv")

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
