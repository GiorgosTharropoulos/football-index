import os

import pandas as pd

from .load_strategy.load_strategy import LoadStrategy


class Frame():
    load_strategy: LoadStrategy

    def read_data(self, path: os.PathLike):
        self.df: pd.DataFrame = self.load_strategy.get_data(
            path)
