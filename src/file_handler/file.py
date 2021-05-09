import os


class File():
    def __init__(self, filename: str):
        self.filename = filename

    def remove_extension(self) -> 'File':
        file_name, _ = os.path.splitext(self.filename)
        return File(file_name)

    def get_extension(self) -> str:
        _, extension = os.path.splitext(self.filename)
        return extension

    def remove_final_prefix_from_file(self) -> 'File':
        return File(self.filename.replace('final_', ''))

    def sanitize(self) -> 'File':
        return File(self
                    .remove_final_prefix_from_file()
                    .remove_extension().filename)

    def get_absolute_path(self) -> 'File':
        return File(os.path.abspath(self.filename))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, File):
            return NotImplemented
        return self.filename == other.filename

    def __repr__(self):
        return f'{self.filename}'
