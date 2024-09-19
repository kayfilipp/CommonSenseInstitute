import os
from fredapi import Fred
import pandas as pd
fred = Fred(os.getenv('FRED_API_KEY'))


def __get_data(series_name: str, latest_only: bool = False):
    data: pd.DataFrame = fred.get_series(series_name)
    if not latest_only:
        return data
    return data.sort_index().tail(1)


def all_employees_non_farm_iowa(latest_only: bool = False):
    return __get_data('IANA', latest_only)


def all_employees_manufacturing_iowa(latest_only: bool = False):
    return __get_data('IAMFGN', latest_only)


def all_transactions_house_price_iowa(latest_only: bool = False):
    return __get_data('IASTHPI', latest_only)

