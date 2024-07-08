from ..items import Items
from ..test_condition import TestCondition


class TestConditions(Items):

    def __init__(self):
        super().__init__('Test Conditions')

    def add(self, value) -> bool:
        if value is not None:
            if isinstance(value, (TestCondition, TestConditions)):
                if isinstance(value, TestCondition):
                    self._items.append(value)
                    return True
                elif isinstance(value, TestConditions):
                    for item in value:
                        self._items.append(item)
                    return True
        return False
