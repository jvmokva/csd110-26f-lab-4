import ast
import pytest
import util


def is_year_lucky(year):
    """Call the is_year_lucky function defined in src/q3.py"""
    return util.get_student_function("q3", "is_year_lucky", "Part 3")(year)


def check_lucky(year, expected, reason):
    util.check_returned(f"is_year_lucky({year})", is_year_lucky(year), expected, reason)


def test_is_year_lucky_is_defined():
    util.get_student_function("q3", "is_year_lucky", "Part 3")


def test_is_year_lucky_takes_one_parameter():
    function = util.get_student_function("q3", "is_year_lucky", "Part 3")
    util.check_parameter_count(function, 1, "the year")


def test_is_year_lucky_returns_instead_of_printing(capsys):
    function = util.get_student_function("q3", "is_year_lucky", "Part 3")
    util.check_returns_instead_of_printing(capsys, function, 28)


def test_is_year_lucky_returns_a_boolean():
    for year in [28, 2001]:
        result = is_year_lucky(year)
        assert isinstance(result, bool), (
            f"is_year_lucky({year}) returned {result!r} (a {type(result).__name__}). It must return True or False "
            f"(a bool, without quotes).")


# Lucky years: leap years that are divisible by 7 or 13
def test_28_is_lucky_year():
    check_lucky(28, True, "28 is a leap year and is divisible by 7, so it IS lucky.")


def test_52_is_lucky_year():
    check_lucky(52, True, "52 is a leap year and is divisible by 13, so it IS lucky.")


def test_1820_is_lucky_year():
    check_lucky(1820, True, "1820 is a leap year and is divisible by 7 (and 13), so it IS lucky.")


# Leap years that are not divisible by 7 or 13
def test_2000_is_not_lucky_year():
    check_lucky(2000, False, "2000 is a leap year, but it is not divisible by 7 or 13, so it is NOT lucky.")


# Years divisible by 7 or 13 that are not leap years
def test_26_is_not_lucky_year():
    check_lucky(
        26, False, "26 is divisible by 13, but it is not a leap year, so it is NOT lucky.\n"
        "HINT: `and` is evaluated before `or`. Use parentheses to control which parts of your expression go together.")


def test_21_is_not_lucky_year():
    check_lucky(21, False, "21 is divisible by 7, but it is not a leap year, so it is NOT lucky.")


def test_91_is_not_lucky_year():
    check_lucky(
        91, False, "91 is divisible by 7 and 13, but it is not a leap year, so it is NOT lucky.\n"
        "HINT: `and` is evaluated before `or`. Use parentheses to control which parts of your expression go together.")


def test_2100_is_not_lucky_year():
    check_lucky(
        2100, False, "2100 is divisible by 7, but it is not a leap year (divisible by 100 but not 400), so it is NOT lucky.\n"
        "HINT: use your is_leapyear function from q2 rather than just checking whether the year is divisible by 4.")


def test_0_is_lucky_year():
    check_lucky(0, True, "0 is a leap year (it is divisible by 400) and is divisible by 7 (and 13), so it IS lucky.")


def test_q3_imports_is_leapyear_from_q2():
    assert "q2" in util.imported_modules("q3"), (
        "src/q3.py must import q2 (e.g. `import q2` or `from q2 import is_leapyear`) so it can use is_leapyear.")
    assert "is_leapyear" not in util.defined_function_names("q3"), (
        "src/q3.py should not contain its own definition of is_leapyear. Delete it and import is_leapyear from q2 instead!")


def test_is_year_lucky_calls_is_leapyear():
    tree = util.parse_source("q3")
    lucky = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == "is_year_lucky"]
    assert lucky, "Define a function named is_year_lucky in src/q3.py, as described in Part 3 of the README."
    calls = [
        node for node in ast.walk(lucky[0]) if isinstance(node, ast.Call) and (
            (isinstance(node.func, ast.Name) and node.func.id == "is_leapyear") or
            (isinstance(node.func, ast.Attribute) and node.func.attr == "is_leapyear"))
    ]
    assert calls, (
        "is_year_lucky should call your is_leapyear function (from q2) to check whether the year is a leap year, "
        "instead of repeating the leap year calculation.")


def test_q3_has_no_print_calls():
    lines = util.find_print_calls("q3")
    assert lines == [], (
        f"src/q3.py calls print() on line(s) {', '.join(map(str, lines))}. is_year_lucky should return its result, "
        f"not print it. (Do your experimenting in scratchpad.py!)")
