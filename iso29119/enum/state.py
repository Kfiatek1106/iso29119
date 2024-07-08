from enum import Enum


class State(Enum):
    PRESENT = 'Present'
    NOT_PRESENT = 'Not present'
    NO_ISSUE = '-'
    NOT_APPLICABLE = 'Not applicable'
    NOT_AVAILABLE = 'Not available'
    MISSING = 'Missing'
    REDUNDANT = 'Redundant'
