from os import PathLike

import pandas as pd
from .load_strategy import LoadStrategy


class ExcelStrategy(LoadStrategy):
    def get_data(self, path: PathLike):
        return pd.read_excel(path)
