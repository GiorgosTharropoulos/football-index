from os import listdir, PathLike
from os.path import isfile, join, abspath
from typing import Any, Generator, List
from .file import File


class Directory():

    def __init__(self, path: PathLike[str]):
        self.path = abspath(path)
        self.files: List[File] = [File(join(abspath(path), file))
                                  for file in listdir(abspath(path))
                                  if isfile(join(abspath(path), file))]

    def are_files_matching(self, other: 'Directory') -> bool:
        for own_file, other_file in zip(self.files, other.files):
            if own_file.sanitize() != other_file.sanitize():
                return False
        return True

    def __repr__(self) -> str:
        return str(self.path)

    def __iter__(self) -> Generator:
        for file in self.files:
            yield file

    def __getitem__(self, index) -> Any:
        return self.files[index]
