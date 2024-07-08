from enum import Enum


class Status(Enum):
    EXECUTE = 'Execute'
    OMIT = 'Omit'
    EXECUTED = 'Executed'
    OMITTED = 'Omitted'
    NOT_EXECUTED = 'Not Executed'
    NO_ISSUE = '-'
