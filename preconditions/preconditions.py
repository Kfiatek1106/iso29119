from ..items import Items
from ..enum import ConditionType
from ..precondition import Precondition


class Preconditions(Items):

    def __init__(self):
        super().__init__('Preconditions')

    def add(self, value) -> bool:
        if value is not None:
            if isinstance(value, (Precondition, Preconditions)):
                if isinstance(value, Precondition):
                    self._items.append(value)
                    return True
                elif isinstance(value, Preconditions):
                    for item in value:
                        self._items.append(item)
                    return True
        return False
