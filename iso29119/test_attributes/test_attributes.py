from ..items import Items
from ..test_attribute import TestAttribute


class TestAttributes(Items):

    def __init__(self, title: str = None):
        super().__init__(title)

    def add(self, value) -> bool:
        if value is not None:
            if isinstance(value, (TestAttribute, TestAttributes)):
                if isinstance(value, TestAttribute):
                    self._items.append(value)
                    return True
                elif isinstance(value, TestAttributes):
                    for item in value:
                        self._items.append(item)
                    return True
        return False
