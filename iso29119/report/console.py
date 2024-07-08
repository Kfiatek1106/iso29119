from ..test_case import TestCase
from ..test_cases import TestCases
from ..utilities import *
from ..condition import Condition
from ..items import Items
from prettytable import *


def console_print_conditions_details(conditions: Items):
    condition_: Condition

    if conditions is not None:
        if isinstance(conditions, Items):
            print(f'{conditions.title}')

            for condition_ in conditions:
                print(condition_)

        dash = ['-' for i in range(136)]
        print(''.join(dash))


ALIGN_LEFT = 'l'
ALIGN_RIGHT = 'r'
ALIGN_CENTRE = 'c'

TEST_CASE_ID = 'Test Case ID'
TITLE = 'Title'
RESULT = 'Result'
STATUS = 'Status'
STATE = 'State'


def console_print_test_case_report(tc: TestCase) -> None:
    def add_condition(condition_: Condition, divider: bool = False) -> None:
        nonlocal table
        table.add_row(row=[condition_.type.value,
                           condition_.title,
                           set_final_result_colour_font(condition_.final_result),
                           set_status_colour_font(condition_.status),
                           set_state_colour_font(condition_.state)], divider=divider)

    def add_conditions(conditions_: Items) -> None:
        counter = 0
        divider: bool = False
        for condition_ in conditions_:
            counter += 1
            if counter == len(conditions_):
                divider = True
            add_condition(condition_, divider)

    table = PrettyTable()
    table.title = f'Test Case Report: {tc.title}'
    table.set_style(SINGLE_BORDER)
    table.field_names = ['', TITLE, RESULT, STATUS, STATE]
    table._min_width = {'': 22, TITLE: 100, RESULT: 10, STATUS: 20, STATE: 20}
    table._max_width = {'': 22, TITLE: 100, RESULT: 10, STATUS: 20, STATE: 20}

    table.align[TEST_CASE_ID] = ALIGN_LEFT
    table.align[TITLE] = ALIGN_LEFT
    table.align[RESULT] = ALIGN_CENTRE
    table.align[STATUS] = ALIGN_CENTRE
    table.align[STATE] = ALIGN_CENTRE

    condition: Condition

    add_conditions(tc.preconditions)
    add_conditions(tc.test_conditions)
    add_conditions(tc.postconditions)

    print(table)


def console_print_test_status_report(tcs: TestCases) -> None:

    def add_record(tc_: TestCase) -> None:
        nonlocal table

        table.add_row([tc.unique_id,
                       tc.title,
                       set_final_result_colour_font(tc.final_result),
                       set_status_colour_font(tc.status),
                       set_state_colour_font(tc.state)])

    tc: TestCase
    table = PrettyTable()
    table.title = f'Test Cases (Status) Report: {tcs.title}'
    table.set_style(SINGLE_BORDER)
    table.field_names = [TEST_CASE_ID, TITLE, RESULT, STATUS, STATE]
    table._min_width = {TEST_CASE_ID: 22, TITLE: 100, RESULT: 10, STATUS: 20, STATE: 20}
    table._max_width = {TEST_CASE_ID: 22, TITLE: 100, RESULT: 10, STATUS: 20, STATE: 20}
    table.align[TEST_CASE_ID] = ALIGN_LEFT
    table.align[TITLE] = ALIGN_LEFT
    table.align[RESULT] = ALIGN_CENTRE
    table.align[STATUS] = ALIGN_CENTRE
    table.align[STATE] = ALIGN_CENTRE

    for tc in tcs:
        add_record(tc)

    print(table)

    for tc in tcs:
        console_print_test_case_report(tc)
