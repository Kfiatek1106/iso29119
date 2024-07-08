from ..items import Items
from ..test_case import TestCase


class TestCases(Items):

    def __init__(self, title: str = None):
        super().__init__(title)

    def add(self, value) -> bool:
        if value is not None:
            if isinstance(value, (TestCase, TestCases)):
                if isinstance(value, TestCase):
                    self._items.append(value)
                    return True
                elif isinstance(value, TestCases):
                    for item in value:
                        self._items.append(item)
                    return True
        return False
