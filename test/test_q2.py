import pytest
import util


def is_leapyear(year):
    """Call the is_leapyear function defined in src/q2.py"""
    return util.get_student_function("q2", "is_leapyear", "Part 2")(year)


def check_leapyear(year, expected, reason):
    util.check_returned(f"is_leapyear({year})", is_leapyear(year), expected, reason)


def test_is_leapyear_is_defined():
    util.get_student_function("q2", "is_leapyear", "Part 2")


def test_is_leapyear_takes_one_parameter():
    function = util.get_student_function("q2", "is_leapyear", "Part 2")
    util.check_parameter_count(function, 1, "the year")


def test_is_leapyear_returns_instead_of_printing(capsys):
    function = util.get_student_function("q2", "is_leapyear", "Part 2")
    util.check_returns_instead_of_printing(capsys, function, 2004)


def test_is_leapyear_returns_a_boolean():
    for year in [2004, 2001]:
        result = is_leapyear(year)
        assert isinstance(result, bool), (
            f"is_leapyear({year}) returned {result!r} (a {type(result).__name__}). It must return True or False "
            f"(a bool, without quotes).")


# Rule 1: years divisible by 4 are leap years, other years are not
def test_2004_is_leap_year():
    check_leapyear(2004, True, "2004 is divisible by 4 (and not by 100), so it IS a leap year.")


def test_2001_is_not_leap_year():
    check_leapyear(2001, False, "2001 is not divisible by 4, so it is NOT a leap year.")


def test_2312_is_leap_year():
    check_leapyear(2312, True, "2312 is divisible by 4 (and not by 100), so it IS a leap year.")


def test_1836_is_leap_year():
    check_leapyear(1836, True, "1836 is divisible by 4 (and not by 100), so it IS a leap year.")


def test_2002_is_not_leap_year():
    check_leapyear(2002, False, "2002 is not divisible by 4, so it is NOT a leap year.")


# Rule 2: ...except years divisible by 100 are NOT leap years...
def test_1900_is_not_leap_year():
    check_leapyear(1900, False, "1900 is divisible by 100 but not by 400, so it is NOT a leap year.")


def test_2100_is_not_leap_year():
    check_leapyear(2100, False, "2100 is divisible by 100 but not by 400, so it is NOT a leap year.")


# Rule 3: ...unless they are also divisible by 400
def test_2000_is_leap_year():
    check_leapyear(2000, True, "2000 is divisible by 400, so it IS a leap year.")


def test_1600_is_leap_year():
    check_leapyear(1600, True, "1600 is divisible by 400, so it IS a leap year.")


def test_2400_is_leap_year():
    check_leapyear(2400, True, "2400 is divisible by 400, so it IS a leap year.")


def test_q2_has_no_print_calls():
    lines = util.find_print_calls("q2")
    assert lines == [], (
        f"src/q2.py calls print() on line(s) {', '.join(map(str, lines))}. is_leapyear should return its result, "
        f"not print it. (Do your experimenting in scratchpad.py!)")
