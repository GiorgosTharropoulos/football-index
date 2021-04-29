from __future__ import annotations

from enum import Enum
from typing import Optional


class DataTypes(Enum):
    NUMERIC: str = 'numeric'
    STRING: str = 'string'
    DATETIME: str = 'date'


class Column:
    def __init__(self,
                 original_name: str,
                 target_name: str,
                 data_type: DataTypes,
                 is_successful: bool = False,
                 is_per90: bool = True,
                 is_absolute: bool = False,
                 is_percentage: bool = False,
                 should_convert: bool = True,
                 is_calculated: bool = False,
                 should_be_per_mins: bool = True,
                 corresponding_column: Optional[Column] = None) -> None:
        self.original_name = original_name
        self.target_name = target_name
        self.data_type = data_type
        self.is_per90 = is_per90
        self.is_absolute = is_absolute
        self.is_successful = is_successful
        self.is_percentage = is_percentage
        self.should_convert = should_convert
        self.is_calculated = is_calculated
        self.should_be_per_mins = should_be_per_mins
        self.corresponding_column = corresponding_column

    @property
    def is_per90(self):
        return self.__is_per90

    @is_per90.setter
    def is_per90(self, is_per90: bool):
        if self.data_type == DataTypes.STRING and is_per90:
            raise TypeError('A column containing strings cannot' +
                            ' be a per 90 column')
        else:
            self.__is_per90 = is_per90

    @property
    def corresponding_column(self):
        return self.__corresponding_column

    @corresponding_column.setter
    def corresponding_column(self, column: Optional[Column]):
        # Corresponding column is optional, only if a column
        # was provided set it to the corresponding column attribute.
        self.__corresponding_column: Optional[Column]
        if column:
            if self.is_successful:
                if column.is_successful:
                    raise Exception(
                        f'Corresponding column: {column.original_name}' +
                        ' cannot be a success column.')
                self.__corresponding_column = column
            else:
                raise Exception(
                    f'{self.original_name} is not a success column')
        else:
            self.__corresponding_column = None

    @property
    def is_percentage(self):
        return self.__is_percentage

    @is_percentage.setter
    def is_percentage(self, is_percentage: bool):
        if (self.is_per90 or self.is_absolute) and is_percentage:
            raise Exception(
                f'Column: {self.original_name} cannot be a percentage' +
                ' column, as it is a per 90 or an absolute value column.')
        else:
            self.__is_percentage = is_percentage

    @property
    def is_absolute(self):
        return self.__is_absolute

    @is_absolute.setter
    def is_absolute(self, is_absolute: bool):
        if self.is_per90 and is_absolute:
            raise Exception(f'Column {self.original_name} cannot be an' +
                            ' absolute column, as it is already a' +
                            ' per 90 column.')
        else:
            self.__is_absolute = is_absolute

    def __repr__(self) -> str:
        raise NotImplementedError
