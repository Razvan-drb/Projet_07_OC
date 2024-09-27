import csv
from itertools import combinations

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
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            stock_name = row['Actions #']
            cost = float(row['Coût par action (en euros)'])
            benefit = float(row['Bénéfice (après 2 ans)'].replace('%', '')) / 100
            profit = cost * benefit
            stocks.append({
                'name': stock_name,
                'cost': cost,
                'profit': profit
            })
    return stocks


def maximize_profit(stocks: list, budget: float) -> tuple:
    """
        Finds the combination of stocks that maximizes profit while staying within the given budget.
        Args:
            stocks (list): A list of stock dictionaries, where each stock contains 'name', 'cost', and 'profit'.
            budget (float): The maximum amount of money (in euros) that can be spent on stocks.
        Returns:
            tuple: A tuple containing the best combination of stocks (list of dictionaries)
                   and the corresponding maximum profit (float).
    """

    best_combination = None
    max_profit = 0

    # do all combinations of stocks and evaluate profit
    for r in range(1, len(stocks) + 1):
        for combo in combinations(stocks, r):
            total_cost = sum(stock['cost'] for stock in combo)
            total_profit = sum(stock['profit'] for stock in combo)

            # combo_names = [stock['name'] for stock in combo]
            # print(f"Combination: {combo_names}, Total Cost: {total_cost:.2f}, Total Profit: {total_profit:.2f}")

            # Check if the combination is within budget
            if total_cost <= budget and total_profit > max_profit:
                max_profit = total_profit
                best_combination = combo

    return best_combination, max_profit


def main():
    """
        Main function that drives the program. Reads stock data, finds the best combination
        of stocks to maximize profit, and prints the result.
        Args:
            None
        Returns:
            None
    """

    budget = 500
    file_path = "../Liste+d'actions+-+P7+Python+-+Feuille+1.csv"

    stocks = read_stock_data(file_path)

    #  Find the best combination of stocks to maximize profit
    best_stocks, max_profit = maximize_profit(stocks, budget)

    if best_stocks:
        print("Best investment combination:")
        for stock in best_stocks:
            print(f"- {stock['name']} (Cost: {stock['cost']} euros, Profit: {stock['profit']:.2f} euros)")
        print(f"Total profit: {max_profit:.2f} euros")
    else:
        print("No valid investment combination found within the budget.")


if __name__ == '__main__':
    main()
