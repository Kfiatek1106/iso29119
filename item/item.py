from abc import ABC, abstractmethod
from ..enum import *


class Item(ABC):

    def __init__(self, title: str = '',
                 final_result_: FinalResult = FinalResult.NO_ISSUE,
                 status_: Status = Status.NO_ISSUE,
                 state_: State = State.NO_ISSUE):

        self._final_result: FinalResult
        self._status: Status
        self._state: State
        self._title: str = ''

        self.title = title
        self.final_result = final_result_
        self.state = state_
        self.status = status_

    @abstractmethod
    def __str__(self):
        pass

    @property
    def final_result(self) -> FinalResult:
        return self._final_result

    @final_result.setter
    def final_result(self, value: FinalResult) -> None:
        if value is not None:
            if isinstance(value, FinalResult):
                self._final_result = value

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, value: Status) -> None:
        if value is not None:
            if isinstance(value, Status):
                self._status = value

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, value: State) -> None:
        if value is not None:
            if isinstance(value, State):
                self._state = value

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if value is not None:
            if isinstance(value, str):
                self._title = value
