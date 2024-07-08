from ..test_case import TestCase
from ..test_cases import TestCases
from iso29119.enum import FinalResult


def make_test_case(title: str, act: str | None, exp: str | None) -> TestCase:
    tc = TestCase(name=title)
    tc.actual = act
    tc.expected = exp
    tc.validate()
    return tc


def make_test_case_title(title: str, id_: int = None) -> str:
    return title if id_ is None else f'{title} [{id_}]'


def process_multiply_values(title: str, actual: list, expected: list) -> TestCases:
    def expected_items() -> None:
        nonlocal title, results_expected, actual, expected
        missing_fl: bool

        for exp in expected:
            missing_fl = False
            for act in actual:
                if exp == act:
                    tc_ = make_test_case(title, act, exp)
                    results_expected.append(tc_)
                    missing_fl = True

            if missing_fl is False:
                if missing_fl is False:
                    tc_ = make_test_case(title, act=None, exp=exp)
                    results_expected.append(tc_)

    def redundant_items() -> None:
        nonlocal title, results_redundant, actual, expected
        redundant_fl: bool

        for act_ in actual:
            redundant_fl = False
            for exp_ in expected:
                if act_ == exp_:
                    redundant_fl = True

            if redundant_fl is False:
                tc_ = make_test_case(title, act=act_, exp=None)
                tc_.result = FinalResult.ATTENTION.value
                testcases.append(tc_)

    testcases = TestCases(name=title)
    results_expected = TestCases(name=title)
    results_redundant = TestCases(name=title)

    expected_items()
    redundant_items()

    if len(results_expected) > 0:
        testcases.append(results_expected)

    if len(results_redundant) > 0:
        testcases.append(results_redundant)

    return testcases
