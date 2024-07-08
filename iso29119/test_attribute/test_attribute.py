from ..condition import Condition
from ..enum import *


class TestAttribute(Condition):

    def __init__(self, title: str = None):
        super().__init__(title, ConditionType.ATTRIBUTE)
        self.__expected = None
        self.__actual = None

    def __str__(self):
        return (f'Expected value: {self.__expected}\n'
                f'Actual value: {self.__actual} \n')

    @property
    def expected(self) -> str:
        return self.__expected

    @expected.setter
    def expected(self, value: str) -> None:
        if value is not None:
            if isinstance(value, str):
                self.__expected = value

    @property
    def actual(self) -> str:
        return self.__actual

    @actual.setter
    def actual(self, value: str) -> None:
        if value is not None:
            if isinstance(value, str):
                self.__actual = value

    def verify(self):
        self.final_result = FinalResult.NO_ISSUE

        if self.__expected is not None and self.__actual is not None:

            if self.__expected == self.__actual:
                self.final_result = FinalResult.PASS

            else:
                self.final_result = FinalResult.FAIL

            self._info = f'[Expected: {self.__expected}, Actual: {self.__actual}]'

        elif self.__expected is not None and self.__actual is None:
            self.__actual = ''
            self.final_result = FinalResult.FAIL

        elif self.__expected is None and self.__actual is not None:
            self.__expected = ''
            self.final_result = FinalResult.ATTENTION

        else:
            return True
