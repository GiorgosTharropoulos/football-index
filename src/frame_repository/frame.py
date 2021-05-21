import os
from typing import Optional

import pandas as pd

from .load_strategy.load_strategy import LoadStrategy


class Frame():
    load_strategy: LoadStrategy
    df: Optional[pd.DataFrame] = None

    def read_data(self, path: os.PathLike):
        self.df: pd.DataFrame = self.load_strategy.get_data(
            path)
