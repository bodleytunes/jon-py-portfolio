import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


import yfinance as yf
from currency_converter import CurrencyConverter

from finquant.portfolio import build_portfolio


def main():

    # yfinance
    # msft = yf.Ticker("MSFT AXP")
    # msft.info

    # history = msft.history(period="1y")

    ydata = yf.download(
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

    print(ydata)

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

    pf.ydata.head(5)

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
        {"Name": "AAPL", "Allocation": 35},  # Apple
        {"Name": "AMZN", "Allocation": 95},  # Amazon
        {"Name": "MSFT", "Allocation": 80},  # Microsoft
        {"Name": "GOOGL", "Allocation": 100},  # Google Alphabet
        {"Name": "AXP", "Allocation": 10},  # AMEX
        {"Name": "JNPR", "Allocation": 6},  # Juniper Networks
        {"Name": "ANET", "Allocation": 6},  # Arista Networks
        {"Name": "PANW", "Allocation": 5},  # Palo Alto Networks
        {"Name": "CSCO", "Allocation": 5},  # Cisco Systems
        {"Name": "SNE", "Allocation": 5},  # Sony
        {"Name": "NVDA", "Allocation": 95},  # Nvidia
        {"Name": "TSLA", "Allocation": 100},  # Tesla
        {"Name": "SPOT", "Allocation": 40},  # Spotify
        {"Name": "V", "Allocation": 25},  # Visa
        {"Name": "MA", "Allocation": 25},  # Mastercard
        {"Name": "MCD", "Allocation": 5},  # Mcdonalds
        {"Name": "NFLX", "Allocation": 25},  # Netflix
        {"Name": "PYPL", "Allocation": 25},  # Paypal
        {"Name": "TMUS", "Allocation": 15},  # T-Mobile US
        {"Name": "LMT", "Allocation": 15},  # Lockheed Martin
        {"Name": "MSI", "Allocation": 15},  # Motorola
        {"Name": "BABA", "Allocation": 20},  # Alibaba
        {"Name": "PFE", "Allocation": 15},  # Pfizer
        {"Name": "INTC", "Allocation": 40},  # Intel
        {"Name": "AMD", "Allocation": 95},  # AMD
        {"Name": "TM", "Allocation": 20},  # Toyota
        {"Name": "AZN", "Allocation": 8},  # AstraZeneca
        {"Name": "ABNB", "Allocation": 40},  # Airbnb
        {"Name": "EADSY", "Allocation": 37},  #
        {"Name": "IAG", "Allocation": 15},  # British Airways / IAG
        {"Name": "LHA.DE", "Allocation": 28},  # Lufthansa
        {"Name": "HTZGQ", "Allocation": 15},  # Hertz
        {"Name": "SIEGY", "Allocation": 35},  # Seimens
        {"Name": "BMW.DE", "Allocation": 17},  # BMW
        {"Name": "VOW.DE", "Allocation": 15},  # Volkswagen Audi
        {"Name": "DAI.DE", "Allocation": 17},  # Mercedes Benz (Daimler AG)
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