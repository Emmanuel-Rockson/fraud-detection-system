
"""Functions for loading the raw transaction data."""

import pandas as pd

from fraud_detection.config import DATA_RAW


def _load_file(filename: str) -> pd.DataFrame:
    """Load one raw CSV file and apply basic cleaning.

    Args:
        filename: Name of the CSV file inside data/raw/.

    Returns:
        A DataFrame with the leftover index column removed and the
        transaction timestamp converted to datetime.
    """
    df = pd.read_csv(DATA_RAW / filename)

    # Drop the leftover "Unnamed: 0" column
    df = df.drop(columns=["Unnamed: 0"])

    # Convert transaction timestamp from text to datetime
    df["trans_date_trans_time"] = pd.to_datetime(
        df["trans_date_trans_time"]
    )

    return df


def load_raw_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the training and test sets.

    Returns:
        (train, test) DataFrames.
    """
    train = _load_file("fraudTrain.csv")
    test = _load_file("fraudTest.csv")
    return train, test
