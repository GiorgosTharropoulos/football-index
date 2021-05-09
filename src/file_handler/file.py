import os
from typing import Union


class File():
    def __init__(self, path: Union[str, os.PathLike]):
        self.path = path
        self.file_name = os.path.basename(path)

    def remove_extension(self) -> 'File':
        file_name, _ = os.path.splitext(self.file_name)
        return File(file_name)

    def get_extension(self) -> str:
        _, extension = os.path.splitext(self.file_name)
        return extension

    def remove_final_prefix_from_file(self) -> 'File':
        return File(str(self.path).replace('final_', ''))

    def sanitize(self) -> 'File':
        return File(self
                    .remove_final_prefix_from_file()
                    .remove_extension().path)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, File):
            return NotImplemented
        return self.path == other.path

    def __repr__(self):
        return f'{self.path}'
