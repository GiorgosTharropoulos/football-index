import os

from file_handler.file import File

from frame_calculations.frame import Frame
from frame_calculations.load_strategy.csv_strategy import CsvStrategy
from frame_calculations.load_strategy.excel_strategy import ExcelStrategy
from frame_calculations.load_strategy.json_strategy import JsonStrategy


class FrameFactory():
    @classmethod
    def create_frame(cls, path: os.PathLike) -> Frame:
        frame = Frame()
        if os.path.isfile(path):
            file = File(path)
            extension: str = file.get_extension()
            if extension == '.xlsx':
                frame.load_strategy = ExcelStrategy()
                frame.read_data(path)
            elif extension == '.csv':
                frame.load_strategy = CsvStrategy()
                frame.read_data(path)
            elif extension == '.json':
                frame.load_strategy = JsonStrategy()
                frame.read_data(path)
            else:
                raise TypeError("Not supported source of data")
        return frame
