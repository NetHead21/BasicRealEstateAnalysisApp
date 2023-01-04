import csv
import os
import statistics
import time

from data_types import Purchase


def main():
    print_header()
    file_name: str = get_data_file()
    data: list = load_file(file_name)
    query_data(data)


def get_data_file() -> str:
    base_dir = os.path.dirname(__file__)
    return os.path.join(base_dir, "data", "Sacramento-RealEstate-Transactions.csv")


def load_file(file_name: str):
    start = time.perf_counter()
    with open(file_name, "r", encoding="utf-8") as file_reader:
        reader = csv.DictReader(file_reader)
        purchases: list = [Purchase.create_from_dict(row) for row in reader]
        print(f"Done is {time.perf_counter() - start}")
        return purchases


def query_data(data: list[Purchase]):
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print(f"Most expensive house is ${high_purchase.price:,}")

    low_purchase = data[0]
    print(f"The least expensive house is ${low_purchase.price:,}")

    # average price house
    prices: list = [purchase.price for purchase in data]
    average_price = statistics.mean(prices)
    print(f"The average hour price is ${int(average_price):,}")

    # average price of 2 bedrooms houses
    prices: list = [purchase.price for purchase in data if purchase.beds == 2]
    average_price = statistics.mean(prices)
    print(f"The average 2-bed price is {int(average_price):,}")


def print_header():
    print("-" * 27)
    print("REAL ESTATE DATA MINING APP")
    print("-" * 27)


if __name__ == "__main__":
    main()
