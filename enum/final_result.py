from enum import Enum


class FinalResult(Enum):
    PASS = 'Pass'
    FAIL = 'Fail'
    NO_ISSUE = "-"
    ATTENTION = 'Attention'
    WARNING = 'Warning'
