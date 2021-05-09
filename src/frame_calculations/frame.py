from typing import Union
import pandas as pd
from file_handler.directory import Directory

from file_handler.file import File
from .load_strategy.load_strategy import LoadStrategy


class Frame():
    load_strategy: LoadStrategy

    def read_data(self, directory: Directory, file: File):
        self.df: pd.DataFrame = self.load_strategy.get_data(
            directory=directory, file=file)
