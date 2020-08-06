"""
lambdata: a collection of Data Science helper functdions
"""

import pandas as pd
import numpy as np
from lambdata_ryankoul.dataframe_helper import df_splitter, add_list_to_dataframe

TEST = pd.DataFrame(np.ones(10))
COLORS = ('Blue', 'Orange', 'Red', 'Green', 'Violet', 'Cyan')


# def increment(number):
#     """Increases a given number by 1."""
#     return number + 1


# assert increment(number) - number == 1, 'increment test failed'
