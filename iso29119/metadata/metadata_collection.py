from ..item import Item
from ..items import Items
from ..metadata import MetadataBase
from abc import abstractmethod


class MetadataCollection(Items):

    def __init__(self, title: str = None):
        super().__init__(title)

    @abstractmethod
    def __str__(self):
        pass

    def add(self, value) -> bool:
        if value is not None:
            if isinstance(value, (MetadataBase, MetadataCollection)):
                if isinstance(value, MetadataBase):
                    self._items.append(value)
                    return True
                elif isinstance(value, MetadataCollection):
                    for item in value:
                        self._items.append(item)
                    return True
        return False
