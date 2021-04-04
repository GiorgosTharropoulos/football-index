# noqa: F841
import pytest

from ..column import Column, DataTypes


class TestColumns:
    def test_defaults(self):
        column = Column('Column name', 'Target Name', DataTypes.NUMERIC)
        assert column.original_name == 'Column name'
        assert column.target_name == 'Target Name'
        assert column.data_type == DataTypes.NUMERIC
        assert column.is_per90 is True
        assert column.is_absolute is False
        assert column.is_successful is False
        assert column.is_percentage is False
        assert column.should_convert is True
        assert column.is_calculated is False
        assert column.corresponding_column is None

    def test_is_absolute(self):
        column = Column('Column name', data_type=DataTypes.NUMERIC,
                        is_per90=False, is_absolute=True)
        assert column.original_name == 'Column name'
        assert column.data_type == DataTypes.NUMERIC
        assert column.is_per90 is False
        assert column.is_absolute is True
        assert column.is_successful is False
        assert column.is_percentage is False
        assert column.should_convert is True
        assert column.is_calculated is False
        assert column.corresponding_column is None

    def test_is_successfull(self):
        column = Column(
            'Column name', data_type=DataTypes.NUMERIC, is_successful=True)
        assert column.original_name == 'Column name'
        assert column.data_type == DataTypes.NUMERIC
        assert column.is_per90 is True
        assert column.is_absolute is False
        assert column.is_successful is True
        assert column.is_percentage is False
        assert column.should_convert is True
        assert column.is_calculated is False
        assert column.corresponding_column is None

    def test_is_percentage(self):
        column = Column(
            'Column name', data_type=DataTypes.NUMERIC, is_per90=False,
            is_percentage=True)
        assert column.original_name == 'Column name'
        assert column.data_type == DataTypes.NUMERIC
        assert column.is_per90 is False
        assert column.is_absolute is False
        assert column.is_successful is False
        assert column.is_percentage is True
        assert column.should_convert is True
        assert column.is_calculated is False
        assert column.corresponding_column is None

    def test_corresponding_column(self):
        corresponding_column = Column('Corresponding Column',
                                      data_type=DataTypes.NUMERIC)
        column = Column(
            'Column name', data_type=DataTypes.NUMERIC,
            corresponding_column=corresponding_column, is_successful=True)

        cc = column.corresponding_column
        assert cc.original_name == 'Corresponding Column'
        assert cc.data_type == DataTypes.NUMERIC
        assert cc.is_per90 is True
        assert cc.is_absolute is False
        assert cc.is_successful is False
        assert cc.is_percentage is False
        assert column.should_convert is True
        assert column.is_calculated is False
        assert cc.corresponding_column is None

    def test_string_column_is_not_per90(self):
        with pytest.raises(TypeError):
            column = Column('Per 90 string column',  # noqa: F841
                            DataTypes.STRING)

    def test_only_successful_columns_have_corresponding_columns(self):
        corresponding_column = Column('Corresponding Column',
                                      data_type=DataTypes.NUMERIC)
        with pytest.raises(Exception):
            column = Column(  # noqa: F841
                'Column name', data_type=DataTypes.NUMERIC,
                corresponding_column=corresponding_column,
                is_successful=False)

    def test_is_per90_and_is_not_absolute(self):
        with pytest.raises(Exception):
            column = Column('Per 90 column', is_per90=True,  # noqa: F841
                            is_absolute=False)

    def test_is_per90_and_is_not_percentage(self):
        with pytest.raises(Exception):
            column = Column('Per 90 Column', is_per90=True,  # noqa: F841
                            is_percentage=True)

    def test_is_absolute_and_is_not_percentage(self):
        with pytest.raises(Exception):
            column = Column('Absolute Column', is_per90=False,  # noqa: F841
                            is_absolute=True, is_percentage=True)
