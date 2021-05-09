from os import listdir
from os.path import isfile, join
from .file import File


class Directory():

    def __init__(self, path: str):
        self.path = path
        self.files: list[File] = [File(file) for file in listdir(path)
                                  if isfile(join(path, file))]

    def are_files_matching(self, other: 'Directory') -> bool:
        for own_file, other_file in zip(self.files, other.files):
            if own_file.sanitize() != other_file.sanitize():
                return False
        return True

    def __repr__(self) -> str:
        return self.path
