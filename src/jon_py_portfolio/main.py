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

    exposure = {
        0: {"Name": "AAPL", "Allocation": 5},
        1: {"Name": "AMZN", "Allocation": 5},
        2: {"Name": "MSFT", "Allocation": 5},
        3: {"Name": "GOOGL", "Allocation": 5},
        4: {"Name": "AXP", "Allocation": 5},
        5: {"Name": "JNPR", "Allocation": 5},
        6: {"Name": "ANET", "Allocation": 5},
        7: {"Name": "PANW", "Allocation": 5},
        8: {"Name": "CSCO", "Allocation": 5},
        9: {"Name": "NVDA", "Allocation": 5},
        10: {"Name": "TSLA", "Allocation": 5},
        11: {"Name": "SPOT", "Allocation": 5},
        12: {"Name": "V", "Allocation": 5},
        13: {"Name": "MA", "Allocation": 5},
        14: {"Name": "MCD", "Allocation": 5},
        15: {"Name": "NFLX", "Allocation": 5},
        16: {"Name": "PYPL", "Allocation": 5},
        17: {"Name": "TMUS", "Allocation": 5},
        18: {"Name": "LMT", "Allocation": 5},
        19: {"Name": "MSI", "Allocation": 5},
        20: {"Name": "BABA", "Allocation": 5},
        21: {"Name": "PFE", "Allocation": 5},
        22: {"Name": "INTC", "Allocation": 5},
        23: {"Name": "AMD", "Allocation": 5},
        24: {"Name": "TM", "Allocation": 5},
        25: {"Name": "HYUD.IL", "Allocation": 5},
        26: {"Name": "AZN", "Allocation": 5},
        27: {"Name": "ABNB", "Allocation": 5},
        28: {"Name": "AIR", "Allocation": 5},
        29: {"Name": "IAG", "Allocation": 5},
        30: {"Name": "LHA.DE", "Allocation": 5},
        31: {"Name": "HTZGQ", "Allocation": 5},
        32: {"Name": "SIEGY", "Allocation": 5},
        33: {"Name": "BMW.DE", "Allocation": 5},
        34: {"Name": "VOW.DE", "Allocation": 5},
        35: {"Name": "DAI.DE", "Allocation": 5},
        36: {"Name": "SNE", "Allocation": 5},
    }

    # d = dict.fromkeys(map((i for i in names), 0))

    pf_allocation = pd.DataFrame.from_dict(exposure, orient="index")
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


if __name__ == "__main__":
    # main()
    build_stuff()