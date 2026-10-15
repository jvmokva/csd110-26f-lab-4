import util

BOUNDARY_HINT = ("Centuries start with year 1, so a century ends with a year that is a multiple of 100. "
                 "E.g. the 20th century is 1901 to 2000.")
TEENS_HINT = "11, 12 and 13 use the suffix 'th' (11th, 12th, 13th), even though 1, 2 and 3 use 'st', 'nd' and 'rd'."
BCE_HINT = ("Negative years are BCE, and BCE centuries count backwards from year -1: "
            "-1 to -100 is the 1st century BCE, -101 to -200 is the 2nd century BCE, and so on.")


def centurize_year(year):
  """Call the centurize_year function defined in src/q4.py"""
  return util.get_student_function("q4", "centurize_year", "Part 4")(year)


def _test(year, expected, hint=""):
  util.check_returned(f"centurize_year({year})", centurize_year(year), expected, hint)


def test_centurize_year_is_defined():
  util.get_student_function("q4", "centurize_year", "Part 4")


def test_centurize_year_takes_one_parameter():
  function = util.get_student_function("q4", "centurize_year", "Part 4")
  util.check_parameter_count(function, 1, "the year")


def test_centurize_year_returns_instead_of_printing(capsys):
  function = util.get_student_function("q4", "centurize_year", "Part 4")
  util.check_returns_instead_of_printing(capsys, function, 1550)


def test_centurize_year_returns_a_string():
  result = centurize_year(1550)
  assert isinstance(result, str), (
      f"centurize_year(1550) returned {result!r} (a {type(result).__name__}). It must return a string like '16th century CE'.")


# Centuries ending in 'th'
def test_1550_is_16th_CE():
  _test(1550, "16th century CE")


def test_1999_is_20th_CE():
  _test(1999, "20th century CE")


# Centuries ending in 'st', 'nd' and 'rd'
def test_12_is_1st_CE():
  _test(12, "1st century CE")


def test_150_is_2nd_CE():
  _test(150, "2nd century CE")


def test_250_is_3rd_CE():
  _test(250, "3rd century CE")


def test_2020_is_21st_CE():
  _test(2020, "21st century CE")


def test_2150_is_22nd_CE():
  _test(2150, "22nd century CE")


def test_2250_is_23rd_CE():
  _test(2250, "23rd century CE")


# 11th, 12th and 13th are exceptions
def test_1030_is_11th_CE():
  _test(1030, "11th century CE", TEENS_HINT)


def test_1125_is_12th_CE():
  _test(1125, "12th century CE", TEENS_HINT)


def test_1234_is_13th_CE():
  _test(1234, "13th century CE", TEENS_HINT)


# Years at the start and end of a century
def test_100_is_1st_CE():
  _test(100, "1st century CE", BOUNDARY_HINT)


def test_101_is_2nd_CE():
  _test(101, "2nd century CE", BOUNDARY_HINT)


def test_200_is_2nd_CE():
  _test(200, "2nd century CE", BOUNDARY_HINT)


def test_201_is_3rd_CE():
  _test(201, "3rd century CE", BOUNDARY_HINT)


def test_1100_is_11th_CE():
  _test(1100, "11th century CE", BOUNDARY_HINT)


def test_1101_is_12th_CE():
  _test(1101, "12th century CE", BOUNDARY_HINT)


def test_2000_is_20th_CE():
  _test(2000, "20th century CE", BOUNDARY_HINT)


def test_2001_is_21st_CE():
  _test(2001, "21st century CE", BOUNDARY_HINT)


# Year 0 doesn't really exist, but the README says to count it as part of the 1st century CE
def test_0_is_1st_CE():
  _test(0, "1st century CE", "The README says to count year 0 as a 1st century CE year.")


# Negative years are BCE
def test_n1_is_1st_BCE():
  _test(-1, "1st century BCE", BCE_HINT)


def test_n100_is_1st_BCE():
  _test(-100, "1st century BCE", BCE_HINT)


def test_n101_is_2nd_BCE():
  _test(-101, "2nd century BCE", BCE_HINT)


def test_n200_is_2nd_BCE():
  _test(-200, "2nd century BCE", BCE_HINT)


def test_n201_is_3rd_BCE():
  _test(-201, "3rd century BCE", BCE_HINT)


def test_n1145_is_12th_BCE():
  _test(-1145, "12th century BCE", BCE_HINT)


def test_n2145_is_22nd_BCE():
  _test(-2145, "22nd century BCE", BCE_HINT)


def test_q4_has_no_print_calls():
  lines = util.find_print_calls("q4")
  assert lines == [], (
      f"src/q4.py calls print() on line(s) {', '.join(map(str, lines))}. centurize_year should return its result, "
      f"not print it. (Do your experimenting in scratchpad.py!)")
