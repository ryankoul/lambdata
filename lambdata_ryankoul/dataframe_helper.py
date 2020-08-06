"""
Some functions to help clean and handle DataFrames
"""

import pandas as pd
import numpy as np


def df_splitter(df, train_split=0.8):
    """
    Accepts a DataFrame and returns a train and test set.
    Default split is 80% train, 20% test.
    """

    df = df.copy()                      # Make shallow copy to not modify original
    df = df.sample(frac=1)              # Randomize copy
    split = int(len(df) * train_split)  # Find index cutoff using train split
    return df[:split], df[split:]       # Split and return randomized dataframe


def add_list_to_dataframe(ls, df, col_name='new_col'):
    """
    Adds list to DataFrame as new column.
    Default column name is 'new_col'.
    """
    assert len(ls) == len(
        df.index), "list must be same length as df columns"

    df[col_name] = ls

    return df


# # Test data
# df = pd.DataFrame(
#     np.random.randint(0, 100, size=(10, 10)),
#     columns=list('ABCDEFGHIJ')
# )
# # # Instantiate class, test method
# # test_df = MyDataFrame()
# train, test = df_splitter(df)

# assert train.shape == (8, 10), test.shape == (2, 10)


# # Test
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(add_list_to_dataframe(list_1, df))
