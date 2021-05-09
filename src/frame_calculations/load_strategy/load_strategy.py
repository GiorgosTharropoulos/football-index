from abc import ABC, abstractmethod

from file_handler.file import File
from file_handler.directory import Directory


class LoadStrategy(ABC):
    @abstractmethod
    def get_data(self, directory: Directory, file: File):
        pass
