from colorama import Fore
from enum import Enum
from ..enum import *


def validate_input(value: str) -> str:
    if isinstance(value, (str, int, float)):
        return str(value)
    return ''


def set_red_colour(value: str):
    return f'{Fore.RED}{value}{Fore.RESET}'


def set_green_colour(value: str):
    return f'{Fore.GREEN}{value}{Fore.RESET}'


def set_yellow_colour(value: str) -> str:
    return f'{Fore.YELLOW}{value}{Fore.RESET}'


def set_white_colour(value: str):
    return f'{Fore.WHITE}{value}{Fore.RESET}'


def set_light_white_color(value: str):
    return f'{Fore.LIGHTWHITE_EX}{value}{Fore.RESET}'


def set_enum_green_colour(value: Enum):
    return set_green_colour(value.value)


def set_enum_red_colour(value: Enum):
    return set_red_colour(value.value)


def set_enum_yellow_colour(value: Enum):
    return set_yellow_colour(value.value)


def set_enum_white_colour(value: Enum):
    return set_white_colour(value.value)


def set_final_result_colour_font(value: Enum) -> str:

    if value == FinalResult.PASS:
        result = set_enum_green_colour(value)

    elif value == FinalResult.FAIL:
        result = set_enum_red_colour(value)

    elif value == FinalResult.ATTENTION:
        result = set_enum_yellow_colour(value)

    else:
        result = value.value

    return result


def set_status_colour_font(value: Enum) -> str:

    if value == Status.EXECUTED:
        result = set_enum_green_colour(value)

    else:
        result = value.value

    return result


def set_condition_type_colour_font(value: Enum) -> str:
    output = set_enum_yellow_colour(value)
    if value == ConditionType.ATTRIBUTE:
        output += f'\t\t\t'
    else:
        output += f'\t\t'
    return output


def set_state_colour_font(value: Enum) -> str:

    if value == Status.EXECUTED:
        result = set_enum_green_colour(value)

    else:
        result = value.value

    return result


def successful_desc() -> str:
    return set_green_colour('successful')


def unsuccessful_desc() -> str:
    return set_red_colour('unsuccessful')
