import pytest
import util

ANIMALS = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]


def get_year_animal(year):
  """Call the get_year_animal function defined in src/q1.py"""
  return util.get_student_function("q1", "get_year_animal", "Part 1")(year)


def check_animal(expected, *years):
  for year in years:
    util.check_returned(
        f"get_year_animal({year})", get_year_animal(year), expected,
        f"{year} % 12 is {year % 12}, and every year with that remainder is a year of the {expected}.")


def test_get_year_animal_is_defined():
  util.get_student_function("q1", "get_year_animal", "Part 1")


def test_get_year_animal_takes_one_parameter():
  function = util.get_student_function("q1", "get_year_animal", "Part 1")
  util.check_parameter_count(function, 1, "the year")


def test_get_year_animal_returns_instead_of_printing(capsys):
  function = util.get_student_function("q1", "get_year_animal", "Part 1")
  util.check_returns_instead_of_printing(capsys, function, 2020)


def test_get_year_animal_returns_a_valid_animal_name():
  for year in range(2020, 2032):
    animal = get_year_animal(year)
    assert animal is not None, util.none_returned_hint(f"get_year_animal({year})")
    assert animal in ANIMALS, (
        f"get_year_animal({year}) returned {animal!r}, which is not one of the animal names listed in the README.\n"
        f"Your function must return exactly one of these strings (spelling and capitalization matter): "
        f"{', '.join(ANIMALS)}")


# The years in the README examples
def test_2000_is_year_of_the_dragon():
  check_animal("Dragon", 2000)


def test_1970_is_year_of_the_dog():
  check_animal("Dog", 1970)


# One test per animal. Each checks a recent year, then older years in the same
# position of the 12-year cycle (to catch code that only works for recent years)
def test_year_of_the_rat():
  check_animal("Rat", 2020, 820, 220)


def test_year_of_the_ox():
  check_animal("Ox", 2021, 821, 221)


def test_year_of_the_tiger():
  check_animal("Tiger", 2022, 822, 222)


def test_year_of_the_rabbit():
  check_animal("Rabbit", 2023, 823, 223)


def test_year_of_the_dragon():
  check_animal("Dragon", 2024, 824, 224)


def test_year_of_the_snake():
  check_animal("Snake", 2025, 825, 225)


def test_year_of_the_horse():
  check_animal("Horse", 2026, 826, 226)


def test_year_of_the_goat():
  check_animal("Goat", 2027, 827, 227)


def test_year_of_the_monkey():
  check_animal("Monkey", 2028, 828, 228)


def test_year_of_the_rooster():
  check_animal("Rooster", 2029, 829, 229)


def test_year_of_the_dog():
  check_animal("Dog", 2030, 830, 230)


def test_year_of_the_pig():
  check_animal("Pig", 2031, 831, 231)


def test_q1_has_no_print_calls():
  lines = util.find_print_calls("q1")
  assert lines == [], (
      f"src/q1.py calls print() on line(s) {', '.join(map(str, lines))}. get_year_animal should return its result, "
      f"not print it. (Do your experimenting in scratchpad.py!)")
