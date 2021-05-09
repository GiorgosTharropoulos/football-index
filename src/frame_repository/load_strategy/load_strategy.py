from abc import ABC, abstractmethod
from os import PathLike


class LoadStrategy(ABC):
    @abstractmethod
    def get_data(self, path: PathLike):
        pass
