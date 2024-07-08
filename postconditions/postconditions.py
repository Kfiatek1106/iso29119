from ..items import Items
from ..postcondition import Postcondition
from ..enum import ConditionType


class Postconditions(Items):

    def __init__(self):
        super().__init__('Post conditions')

    def add(self, value) -> bool:
        if value is not None:
            if isinstance(value, (Postcondition, Postconditions)):
                if isinstance(value, Postcondition):
                    self._items.append(value)
                    return True
                elif isinstance(value, Postconditions):
                    for item in value:
                        self._items.append(item)
                    return True
        return False
