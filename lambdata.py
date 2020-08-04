"""
Lambdata: A collection of Data Science helper functions
"""

import pandas as pd
import numpy as np
TEST = pd.DataFrame()


## Train/test split function for a dataframe
# Inherit from panda's DataFrame
# class MyDataFrame(pd.DataFrame):
#     def num_cells(self):
#         return self.shape[0] * self.shape[1]

def df_splitter(df, train_split=0.8):
    """
    Accepts a DataFrame and returns a train and test set.
    Default split is 80% train, 20% test.
    """

    df = df.copy()                        # Make shallow copy to not modify original
    df = df.sample(frac=1)                # Randomize copy
    split = int(len(df) * train_split)    # Use given train proportion to find cutoff
    return df[:split], df[split:]         # Split and return the randomized DataFrame

# Test
df = pd.DataFrame(
    np.random.randint(0, 100, size=(10, 10)), 
    columns=list('ABCDEFGHIJ')
    )
train, test = df_splitter(df)

assert train.shape == (8, 10), test.shape == (2, 10)


# Check DataFrame nulls




