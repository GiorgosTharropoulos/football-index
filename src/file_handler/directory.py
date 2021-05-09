from os import listdir
from os.path import isfile, join
from typing import List
from .file import File


class Directory():

    def __init__(self, path: str):
        self.path = path
        self.files: List[File] = [File(file) for file in listdir(path)
                                  if isfile(join(path, file))]

    def are_files_matching(self, other: 'Directory') -> bool:
        for own_file, other_file in zip(self.files, other.files):
            if own_file.sanitize() != other_file.sanitize():
                return False
        return True

    def __repr__(self) -> str:
        return self.path

    def __iter__(self) -> File:
        for file in self.files:
            yield file

    def __getitem__(self, index) -> File:
        return self.files[index]
