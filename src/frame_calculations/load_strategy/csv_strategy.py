import pandas as pd
from file_handler.directory import Directory
from file_handler.file import File
from .load_strategy import LoadStrategy


class CsvStrategy(LoadStrategy):
    def get_data(self, directory: Directory, file: File):
        return pd.read_csv(directory.path.join(file.filename))
