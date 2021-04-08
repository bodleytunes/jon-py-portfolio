import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


import yfinance as yf
from currency_converter import CurrencyConverter

from finquant.portfolio import build_portfolio


def build_portfolio():

    c = CurrencyConverter()

    b = Basket()
    b.total_expenditure = 850  # total distributed funds to portfolio (in GBP)

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
    ]

    ydata = get_yahoo_data(portfolio_list)

    for item in portfolio_list:
        # append a stock to the basket
        b.stocks.append(Stock(item["Name"], item["Allocation"]))
        # each time recalculate the sum of all the weights
        b.sum_of_weights = b._calc_sum_of_weights()
        b.weight_slice_value = b._calc_weight_slice_value()

    print(f"sum of weights: {b.sum_of_weights}")
    print(f"weight slice value: {b.weight_slice_value}")

    # Set Values for basket of stocks
    for stock in b.stocks:
        b._calc_stock_percentage()
        b._calc_stock_purchase_amount()

    # set close price data for each stock
    b._set_stock_close_price(ydata)

    # set number (or fraction) of shares to buy
    b._set_no_of_shares_to_buy(ydata)

    # Display Results
    for stock in b.stocks:
        # trim to 2 decimal places
        stock_purchase_amount = float("{:.2f}".format(stock.purchase_amount))
        stock_percentage = float("{:.2f}".format(stock.percentage))
        stock_close_price = float("{:.2f}".format(stock.close_price))
        stock_close_price_gbp = float(
            "{:.2f}".format(c.convert(stock_close_price, "USD", "GBP"))
        )

        print(
            f"|| Stock Name: {stock.symbol} *({stock.weight}) || Individual Stock Percentage: {stock_percentage}% || Amount to be purchased: £{stock_purchase_amount} of £{b.total_expenditure} || Closed Price: ${stock_close_price} / £{stock_close_price_gbp} || No. of shares to own: {stock.no_of_shares} ||"
        )


def get_yahoo_data(portfolio_list):

    #  Yahoo finance downloads / join all the symbols in one line of strings separated by " " space
    tickers = " ".join(list(i["Name"] for i in portfolio_list))
    # print(tickers)

    ydata = yf.download(
        tickers=tickers,
        period="1d",
        group_by="ticker",
        auto_adjust=True,
        threads=True,
        proxy=None,
    )

    # get list of all the symbols
    symbol_list = list(d[0] for d in ydata)
    # list close price in yfinance dataframe (using iloc)
    # for symbol in symbol_list:
    #    print(ydata[symbol]["Close"].iloc[0])

    return ydata


class Basket:
    def __init__(self):
        self.weight_slice_value = 0
        self.sum_of_weights = 0
        self.percent = 100
        self.total_expenditure = 0
        self.stocks = []

    def _calc_sum_of_weights(self) -> int:
        sum_of_weights = 0
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
            stock.purchase_amount = (self.total_expenditure / 100) * stock.percentage

    def _set_stock_close_price(self, ydata):

        for stock in self.stocks:
            stock.close_price = ydata[stock.symbol]["Close"].iloc[0]

    def _set_no_of_shares_to_buy(self, ydata):

        c = CurrencyConverter()

        for stock in self.stocks:

            purchase_amount_usd = c.convert(stock.purchase_amount, "GBP", "USD")
            # calc the number of shares (or fraction) to buy
            stock.no_of_shares = purchase_amount_usd / stock.close_price


class Stock:
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight
        self.purchase_amount = 0
        self.percentage = 0
        self.close_price = 0
        self.purchase_price = 0


if __name__ == "__main__":
    # main()
    build_portfolio()