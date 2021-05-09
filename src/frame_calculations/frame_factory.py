from file_handler.directory import Directory
from file_handler.file import File
from .frame import Frame
from .load_strategy.csv_strategy import CsvStrategy
from .load_strategy.excel_strategy import ExcelStrategy


class FrameFactory():
    @classmethod
    def create_frame(cls, directory: Directory, file: File) -> Frame:
        frame = Frame()
        extension: str = file.get_extension()
        if extension == '.xlsx':
            frame.load_strategy = ExcelStrategy()
            frame.read_data(directory=directory, file=file)
        elif extension == '.csv':
            frame.load_strategy = CsvStrategy()
            frame.read_data(directory=directory, file=file)
        return frame
