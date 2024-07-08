from ..condition import Condition
from ..enum import ConditionType


class Postcondition(Condition):

    def __init__(self, title: str = None):
        super().__init__(title, ConditionType.PRECONDITION)
