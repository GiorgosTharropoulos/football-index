import os

import pandas as pd
from file_handler.directory import Directory
from file_handler.file import File
from .load_strategy import LoadStrategy


class ExcelStrategy(LoadStrategy):
    def get_data(self, directory: Directory, file: File):
        return pd.read_excel(os.path.join(directory.path, file.filename))
