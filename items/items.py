from abc import abstractmethod
from ..item import Item
from ..enum import *
from ..utilities import *


class Items(Item):

    def __init__(self, title: str = None):
        super().__init__(title)
        self._items: list = list()
        self.__passes: int = 0
        self.__fails: int = 0
        self.__attn: int = 0

        self.__counter: int = 0
        self.__iter = None

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        self.__counter = 0
        self.__iter = iter(self._items)
        return self

    def __next__(self):
        if self.__counter < len(self):
            self.__counter += 1
            return next(self.__iter)
        raise StopIteration

    def __str__(self):
        return (f'{self.title}\n'
                f'Result: \t\t{set_final_result_colour_font(self.final_result)}\n'
                f'Status: \t\t{self.status}\n'
                f'State: \t\t\t{self.state}\n'
                f'Total Items: \t{len(self)} [100.00%] \n'
                f'Passes: \t\t{self.__passes} [{print_in_percen(self.__passes, len(self))}] \n'
                f'Fails: \t\t\t{self.__fails} [{print_in_percen(self.__fails, len(self))}] \n'
                f'Attentions: \t{self.__attn} [{print_in_percen(self.__attn, len(self))}] \n')

    @property
    def passes(self) -> int:
        return self.__passes

    @property
    def fails(self) -> int:
        return self.__fails

    @property
    def attentions(self) -> int:
        return self.__attn

    @abstractmethod
    def add(self, value) -> bool:
        pass

    def get(self):
        return self

    def verify(self) -> bool:
        self.final_result = FinalResult.NO_ISSUE
        self.__passes = 0
        self.__fails = 0
        self.__attn = 0

        for item in self._items:
            if item is not None:
                if isinstance(item, Item):

                    if item.final_result == FinalResult.PASS:
                        self.__passes += 1

                    elif item.final_result == FinalResult.FAIL:
                        self.__fails += 1

                    elif item.final_result == FinalResult.ATTENTION:
                        self.__attn += 1
                    else:
                        pass

        if len(self) > 0:
            self.final_result = FinalResult.PASS

            if self.__fails > 0:
                self.final_result = FinalResult.FAIL

        self.status = Status.EXECUTED

        return True
