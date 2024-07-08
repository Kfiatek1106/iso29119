from abc import abstractmethod
from ..condition import Condition
from ..enum import ConditionType, FinalResult
from ..test_attribute import TestAttribute
from ..test_attributes import TestAttributes


class TestCondition(Condition):

    def __init__(self, title: str = None):
        super().__init__(title, ConditionType.TEST_CONDITION)
        self._attributes: TestAttributes = TestAttributes()
        self._expected = None
        self._actual = None

    @property
    @abstractmethod
    def expected(self):
        pass

    @expected.setter
    @abstractmethod
    def expected(self, value) -> None:
        pass

    @property
    @abstractmethod
    def actual(self):
        pass

    @actual.setter
    @abstractmethod
    def actual(self, value) -> None:
        pass

    def _verify(self):
        if self._expected is not None and self._actual is not None:

            if self._expected == self._actual:
                self._final_result = FinalResult.PASS

            else:
                self._final_result = FinalResult.FAIL

            self.__info = f'[Expected: {self._expected}, Actual: {self._actual}]'

        elif self._expected is not None and self._actual is None:
            self._actual = ''
            self._final_result = FinalResult.FAIL

        elif self._expected is None and self._actual is not None:
            self._expected = ''
            self._final_result = FinalResult.ATTENTION

        else:
            return True

    @abstractmethod
    def verify(self):
        pass

    def add_attribute(self, value: TestAttribute) -> bool:
        if value is not None:
            if isinstance(value, TestAttribute):
                self._attributes.add(value)
                return True
        return False
