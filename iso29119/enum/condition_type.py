from enum import Enum


class ConditionType(Enum):

    PRECONDITION = 'Precondition'
    POST_CONDITION = 'Post condition'
    TEST_CONDITION = 'Test Condition'
    ATTRIBUTE = 'Attribute'
    NOT_SET = 'Condition type not set'
    METADATA = 'Metadata'
