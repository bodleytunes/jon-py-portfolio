import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

import yfinance as yf

from finquant.portfolio import build_portfolio


def main():

    # yfinance
    # msft = yf.Ticker("MSFT AXP")
    # msft.info

    # history = msft.history(period="1y")

    data = yf.download(
        tickers="AAPL AMZN MSFT GOOGL AXP \
             JNPR ANET PANW CSCO NVDA TSLA \
                 SPOT V MA MCD NFLX PYPL \
                      TMUS LMT MSI BABA PFE \
                          INTC AMD TM HYUD.IL AZN ABNB AIR IAG \
                              LHA.DE HTZGQ SIEGY BMW.DE VOW.DE DAI.DE SNE",
        period="1d",
        group_by="ticker",
        auto_adjust=True,
        threads=True,
        proxy=None,
    )

    print(data)

    names = [
        "AAPL",
        "AMZN",
        "MSFT",
        "GOOGL",
        "AXP",
        "JNPR",
        "ANET",
        "PANW",
        "CSCO",
        "NVDA",
        "TSLA",
        "SPOT",
        "V",
        "MA",
        "MCD",
        "NFLX",
        "PYPL",
        "TMUS",
        "LMT",
        "MSI",
        "BABA",
        "PFE",
        "INTC",
        "AMD",
        "TM",
        "HYUD.IL",
        "AZN",
        "ABNB",
        "AIR",
        "IAG",
        "LHA.DE",
        "HTZGQ",
        "SIEGY",
        "BMW.DE",
        "VOW.DE",
        "DAI.DE",
        "SNE",
    ]

    # d = {
    #     (index for index, item in enumerate(names)):
    #     "Name": (n for n in names),
    #     "Allocation": 10,
    # }

    d = dict.fromkeys(i for i in names)
    print(d)

    # Finquant
    start_date = "2020-01-01"
    end_date = "2021-03-29"
    pf = build_portfolio(
        names=names,
        start_date=start_date,
        end_date=end_date,
        data_api="yfinance",
    )

    pf.data.head(5)

    pf.properties()

    # data.

    # df = pd.read_json
    # Read in price data
    # df = pd.read_csv(
    #    "tests/resources/stock_prices.csv", parse_dates=True, index_col="date"
    # )
    # pd.read_pickle


def build_stuff():

    # exposure = [
    #     {"Name": "AAPL", "Allocation": 5},
    #     {"Name": "AMZN", "Allocation": 5},
    #     {"Name": "MSFT", "Allocation": 5},
    #     {"Name": "GOOGL", "Allocation": 5},
    #     {"Name": "AXP", "Allocation": 5},
    #     {"Name": "JNPR", "Allocation": 5},
    #     {"Name": "ANET", "Allocation": 5},
    #     {"Name": "PANW", "Allocation": 5},
    #     {"Name": "CSCO", "Allocation": 5},
    #     {"Name": "NVDA", "Allocation": 5},
    #     {"Name": "TSLA", "Allocation": 5},
    #     {"Name": "SPOT", "Allocation": 5},
    #     {"Name": "V", "Allocation": 5},
    #     {"Name": "MA", "Allocation": 5},
    #     {"Name": "MCD", "Allocation": 5},
    #     {"Name": "NFLX", "Allocation": 5},
    #     {"Name": "PYPL", "Allocation": 5},
    #     {"Name": "TMUS", "Allocation": 5},
    #     {"Name": "LMT", "Allocation": 5},
    #     {"Name": "MSI", "Allocation": 5},
    #     {"Name": "BABA", "Allocation": 5},
    #     {"Name": "PFE", "Allocation": 5},
    #     {"Name": "INTC", "Allocation": 5},
    #     {"Name": "AMD", "Allocation": 5},
    #     {"Name": "TM", "Allocation": 5},
    #     {"Name": "AZN", "Allocation": 5},
    #     {"Name": "ABNB", "Allocation": 5},
    #     {"Name": "AIR", "Allocation": 5},
    #     {"Name": "IAG", "Allocation": 5},
    #     {"Name": "LHA.DE", "Allocation": 5},
    #     {"Name": "HTZGQ", "Allocation": 5},
    #     {"Name": "SIEGY", "Allocation": 5},
    #     {"Name": "BMW.DE", "Allocation": 5},
    #     {"Name": "VOW.DE", "Allocation": 5},
    #     {"Name": "DAI.DE", "Allocation": 5},
    #     {"Name": "SNE", "Allocation": 5},
    # ]

    exposure = [
        {"Name": "AAPL", "Allocation": 35},
        {"Name": "AMZN", "Allocation": 95},
        {"Name": "MSFT", "Allocation": 80},
        {"Name": "GOOGL", "Allocation": 100},
        {"Name": "AXP", "Allocation": 10},
        {"Name": "JNPR", "Allocation": 6},
        {"Name": "ANET", "Allocation": 6},
        {"Name": "PANW", "Allocation": 5},
        {"Name": "CSCO", "Allocation": 5},
        {"Name": "SNE", "Allocation": 5},
        {"Name": "NVDA", "Allocation": 95},
        {"Name": "TSLA", "Allocation": 100},
        {"Name": "SPOT", "Allocation": 40},
        {"Name": "V", "Allocation": 25},
        {"Name": "MA", "Allocation": 25},
        {"Name": "MCD", "Allocation": 5},
        {"Name": "NFLX", "Allocation": 25},
        {"Name": "PYPL", "Allocation": 25},
        {"Name": "TMUS", "Allocation": 15},
        {"Name": "LMT", "Allocation": 15},
        {"Name": "MSI", "Allocation": 15},
        {"Name": "BABA", "Allocation": 20},
        {"Name": "PFE", "Allocation": 15},
        {"Name": "INTC", "Allocation": 40},
        {"Name": "AMD", "Allocation": 95},
        {"Name": "TM", "Allocation": 20},
        {"Name": "AZN", "Allocation": 5},
        {"Name": "ABNB", "Allocation": 40},
        {"Name": "EADSY", "Allocation": 37},
        {"Name": "IAG", "Allocation": 18},
        {"Name": "LHA.DE", "Allocation": 28},
        {"Name": "HTZGQ", "Allocation": 15},
        {"Name": "SIEGY", "Allocation": 35},
        {"Name": "BMW.DE", "Allocation": 17},
        {"Name": "VOW.DE", "Allocation": 15},
        {"Name": "DAI.DE", "Allocation": 17},
        {"Name": "SNE", "Allocation": 15},
    ]

    pf_allocation = pd.DataFrame(exposure)
    names = pf_allocation["Name"].values.tolist()

    start_date = "2020-01-01"
    end_date = "2021-03-29"

    pf = build_portfolio(
        names=names,
        pf_allocation=pf_allocation,
        start_date=start_date,
        end_date=end_date,
        data_api="yfinance",
    )

    pf.properties()

    print(pf)


def build_portfolio():

    portfolio_list = [
        {"Name": "AAPL", "Allocation": 35},
        {"Name": "AMZN", "Allocation": 95},
        {"Name": "MSFT", "Allocation": 80},
        {"Name": "GOOGL", "Allocation": 100},
        {"Name": "AXP", "Allocation": 10},
        {"Name": "JNPR", "Allocation": 6},
        {"Name": "ANET", "Allocation": 6},
        {"Name": "PANW", "Allocation": 5},
        {"Name": "CSCO", "Allocation": 5},
        {"Name": "SNE", "Allocation": 5},
        {"Name": "NVDA", "Allocation": 95},
        {"Name": "TSLA", "Allocation": 100},
        {"Name": "SPOT", "Allocation": 40},
        {"Name": "V", "Allocation": 25},
        {"Name": "MA", "Allocation": 25},
        {"Name": "MCD", "Allocation": 5},
        {"Name": "NFLX", "Allocation": 25},
        {"Name": "PYPL", "Allocation": 25},
        {"Name": "TMUS", "Allocation": 15},
        {"Name": "LMT", "Allocation": 15},
        {"Name": "MSI", "Allocation": 15},
        {"Name": "BABA", "Allocation": 20},
        {"Name": "PFE", "Allocation": 15},
        {"Name": "INTC", "Allocation": 40},
        {"Name": "AMD", "Allocation": 95},
        {"Name": "TM", "Allocation": 20},
        {"Name": "AZN", "Allocation": 5},
        {"Name": "ABNB", "Allocation": 40},
        {"Name": "EADSY", "Allocation": 37},
        {"Name": "IAG", "Allocation": 18},
        {"Name": "LHA.DE", "Allocation": 28},
        {"Name": "HTZGQ", "Allocation": 15},
        {"Name": "SIEGY", "Allocation": 35},
        {"Name": "BMW.DE", "Allocation": 17},
        {"Name": "VOW.DE", "Allocation": 15},
        {"Name": "DAI.DE", "Allocation": 17},
        {"Name": "SNE", "Allocation": 15},
    ]

    b = Basket()
    b.total_expenditure = 1000  # total distributed funds to portfolio

    # b.stocks.append(Stock(symbol="GOOGL", weight=95))

    for item in portfolio_list:
        # append a stock to the basket
        b.stocks.append(Stock(item["Name"], item["Allocation"]))
        # each time recalculate the sum of all the weights
        b.sum_of_weights = b._calc_sum_of_weights()
        b.weight_slice_value = b._calc_weight_slice_value()

    print(f"sum of weights: {b.sum_of_weights}")
    print(f"weight slice value: {b.weight_slice_value}")

    for stock in b.stocks:
        b._calc_stock_percentage()
        b._calc_stock_purchase_amount()

    for stock in b.stocks:
        print(
            f"|| Stock Name: {stock.symbol} || Individual Stock Percentage: {stock.percentage} || Amount to be purchased: £{stock.purchase_amount} of £{b.total_expenditure} ||"
        )


class Basket:
    def __init__(self):
        self.weight_slice_value = 0
        self.sum_of_weights = 0
        self.percent = 100
        self.total_expenditure = 0
        self.stocks = []

    def _calc_sum_of_weights(self) -> int:
        sum_of_weights = 0
        # Todo - this should only loop if not already a sum of weights, if its more than 0 then it should just add the latest weight to it and not have to keep looping
        for stock in self.stocks:
            sum_of_weights = sum_of_weights + stock.weight

        return sum_of_weights

    def _calc_weight_slice_value(self) -> int:
        weight_slice_value = 100 / self.sum_of_weights
        return weight_slice_value

    def _calc_stock_percentage(self):

        for stock in self.stocks:
            stock.percentage = stock.weight * self.weight_slice_value

    def _calc_stock_purchase_amount(self):

        for stock in self.stocks:
            stock.purchase_amount = (self.sum_of_weights / 100) * stock.percentage


class Stock:
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight
        self.purchase_amount = 0
        self.percentage = 0


if __name__ == "__main__":
    # main()
    build_portfolio()