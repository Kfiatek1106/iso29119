from ..utilities import *
from ..item import Item
from ..enum import ConditionType, FinalResult


class Condition(Item):

    def __init__(self, title: str = None, condition_type: ConditionType = ConditionType.NOT_SET):
        super().__init__(title, FinalResult.FAIL)
        self._type: ConditionType = condition_type
        self._info: str = ''

    def __str__(self):
        output = (f'{self._type.value} '
                  f'[{set_final_result_colour_font(self.final_result)}] '
                  f'{set_white_colour(self.title)} ')

        max_ = 100
        diff = max_ - (len(self.title) + len(self.final_result.value) + len(self._info))
        tab = [' ' for i in range(diff)]
        output += f'{"".join(tab)}{self._info}'
        return output

    @property
    def type(self) -> ConditionType:
        return self._type

    @property
    def info(self) -> str:
        return self._info

    @info.setter
    def info(self, value: str) -> None:
        if value is not None:
            if isinstance(value, str):
                self._info = value
