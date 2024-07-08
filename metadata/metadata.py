from ..condition import Condition
from ..enum import ConditionType
from abc import abstractmethod


class MetadataBase(Condition):

    def __init__(self, title: str = None):
        super().__init__(title, ConditionType.METADATA)
        self._info: str = ''

    @abstractmethod
    def __str__(self):
        pass
