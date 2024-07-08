from ..item import Item
from ..enum import Priority, FinalResult, State, Status
from ..preconditions import Preconditions
from ..postconditions import Postconditions
from ..test_conditions import TestConditions
from ..utilities import *


class TestCase(Item):

    def __init__(self, unique_id: str = None, title: str = None):
        super().__init__(title)
        self.__unique_id: str = ''
        self.__desc: str = ''
        self.__priority: Priority = Priority.NONE
        self.__req_id: str = ''
        self.__preconditions: Preconditions = Preconditions()
        self.__postconditions: Postconditions = Postconditions()
        self.__test_conditions: TestConditions = TestConditions()

        self.unique_id = unique_id

    def __str__(self):
        return (f'Test Case ID \t{self.__unique_id} \n'
                f'Title: \t\t{self.title} \n'
                f'Result: \t\t{set_final_result_colour_font(self.final_result)}\n'
                f'Status: \t\t{set_status_colour_font(self.status)}\n'
                f'State: \t\t\t{set_state_colour_font(self.state)}\n'
                f'\n\n'# f'Description: {self.desc}\n'
                f'{self.preconditions}\n'
                f'{self.test_conditions}\n'
                f'{self.postconditions}\n')

    @property
    def unique_id(self) -> str:
        return self.__unique_id

    @unique_id.setter
    def unique_id(self, value: str) -> None:
        if value is not None:
            if isinstance(value, str):
                self.__unique_id = value

    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, value: str) -> None:
        if value is not None:
            if isinstance(value, str):
                self.__desc = value

    @property
    def priority(self) -> Priority:
        return self.__priority

    @priority.setter
    def priority(self, value: Priority) -> None:
        if value is not None:
            if isinstance(value, Priority):
                self.__priority = value

    @property
    def req_id(self) -> str:
        return self.__req_id

    @req_id.setter
    def req_id(self, value: str) -> None:
        if value is not None:
            if isinstance(value, str):
                self.__req_id = value

    @property
    def preconditions(self) -> Preconditions:
        return self.__preconditions

    @preconditions.setter
    def preconditions(self, value: Preconditions) -> None:
        if value is not None:
            if isinstance(value, Preconditions):
                self.__preconditions = value

    @property
    def postconditions(self) -> Postconditions:
        return self.__postconditions

    @postconditions.setter
    def postconditions(self, value: Postconditions) -> None:
        if value is not None:
            if isinstance(value, Postconditions):
                self.__postconditions = value

    @property
    def test_conditions(self) -> TestConditions:
        return self.__test_conditions

    @test_conditions.setter
    def test_conditions(self, value) -> None:
        if value is not None:
            if isinstance(value, TestConditions):
                self.__test_conditions = value

    def verify(self) -> bool:
        self.__preconditions.verify()

        if self.__preconditions.final_result == FinalResult.PASS:
            self.__test_conditions.verify()

            if self.__test_conditions.final_result == FinalResult.PASS:
                self.__postconditions.verify()

        # if self.__postconditions.final_result == FinalResult.PASS:
        #     self.final_result = FinalResult.PASS

        return True
