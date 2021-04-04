import re


class ColumnName():
    def __init__(self, name: str) -> None:
        self.name = name

    def rm_special_characters(self):
        intermediate = re.sub(r',|/', '', self.name).strip()
        self.name = re.sub(r' +', ' ', intermediate)
        return self

    def percentage_symbol_to_literal(self):
        self.name = self.name.replace('%', 'percentage')
        return self

    def titles_join_lower(self):
        self.name = '_'.join(self.name.lower().split(' '))
        return self

    def convert(self):
        return self.rm_special_characters() \
            .percentage_symbol_to_literal() \
            .titles_join_lower()

    def __repr__(self) -> str:
        return self.name
