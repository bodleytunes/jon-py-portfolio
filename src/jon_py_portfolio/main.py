import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

import yfinance as yf


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
        threads=False,
        proxy=None,
    )

    # data.

    # df = pd.read_json
    # Read in price data
    # df = pd.read_csv(
    #    "tests/resources/stock_prices.csv", parse_dates=True, index_col="date"
    # )


if __name__ == "__main__":
    main()