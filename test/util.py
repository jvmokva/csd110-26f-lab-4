import ast
import difflib
import importlib
import inspect
import pytest
import traceback
from pathlib import Path
from types import TracebackType

from conftest import InputCalledDuringTest

SRC_DIR = Path(__file__).resolve().parent.parent / "src"


def read_source(module_name):
  """Return the text of src/<module_name>.py"""
  return (SRC_DIR / f"{module_name}.py").read_text()


def parse_source(module_name):
  """Parse src/<module_name>.py so tests can check how it is written"""
  try:
    return ast.parse(read_source(module_name))
  except SyntaxError as e:
    message = (
        f"Python can't understand the code in src/{module_name}.py, so it could not be checked.\n"
        f"  {type(e).__name__}: {e.msg} (line {e.lineno} of src/{module_name}.py)\n"
        f"Run `python src/{module_name}.py` in the terminal to see more details about the error.")
  pytest.fail(message, pytrace=False)


def _line_in_src(exc):
  """Describe where in the student's src/ files an exception happened, e.g. 'line 4 of src/q2.py'"""
  for frame in reversed(traceback.extract_tb(exc.__traceback__)):
    path = Path(frame.filename).resolve()
    if path.parent == SRC_DIR:
      return f"line {frame.lineno} of src/{path.name}"
  return None


def import_student_module(module_name):
  """Import src/<module_name>.py. If the file can't be imported, fail the current
     test with a short explanation (rather than stopping the whole test run)"""
  # pytest.fail is called after the except blocks so that the original error
  # isn't also printed as part of the test output
  try:
    return importlib.import_module(module_name)
  except SyntaxError as e:
    # e.filename may be a different file (e.g. q3.py imports a q2.py with a typo)
    filename = Path(e.filename).name if e.filename else f"{module_name}.py"
    message = (
        f"Python can't understand the code in src/{filename}, so it could not be tested.\n"
        f"  {type(e).__name__}: {e.msg} (line {e.lineno} of src/{filename})\n"
        f"Run `python src/{filename}` in the terminal to see more details about the error.")
  except InputCalledDuringTest:
    message = (
        f"src/{module_name}.py (or a file it imports) calls input() as soon as it is imported.\n"
        f"Files q1.py to q4.py should only define functions. To try out your functions, call them "
        f"from scratchpad.py instead.")
  except Exception as e:
    where = _line_in_src(e)
    message = (
        f"src/{module_name}.py crashed while it was being imported, so its functions could not be tested.\n"
        f"  {type(e).__name__}: {e}" + (f" (at {where})" if where else "") + "\n"
        f"Run `python src/{module_name}.py` in the terminal to see the full error.")
  pytest.fail(message, pytrace=False)


def get_student_function(module_name, function_name, readme_part):
  """Return the function named function_name from src/<module_name>.py, or fail
     the current test with a helpful message if it doesn't exist"""
  module = import_student_module(module_name)
  function = getattr(module, function_name, None)
  if callable(function):
    return function

  message = f"Define a function named {function_name} in src/{module_name}.py, as described in {readme_part} of the README."
  defined = [name for name, value in vars(module).items() if inspect.isfunction(value)]
  close = difflib.get_close_matches(function_name, defined, n=1)
  if close:
    message += f"\nYou defined a function named {close[0]}. Check the spelling: the name must be exactly {function_name}"
  pytest.fail(message, pytrace=False)


def check_parameter_count(function, count, description):
  """Fail with a helpful message if function doesn't take exactly count parameters"""
  params = inspect.signature(function).parameters
  if len(params) != count:
    pytest.fail(
        f"{function.__name__} must have exactly {count} parameter{'s' if count != 1 else ''} ({description}), "
        f"but yours has {len(params)}: def {function.__name__}({', '.join(params)}):",
        pytrace=False)


def check_returned(call, actual, expected, explanation=""):
  """Compare the value a student function returned with the expected value.
     call is a description of the call, like 'is_leapyear(1900)'.
     explanation (optional) says why expected is correct."""
  if actual == expected and type(actual) == type(expected):
    return

  why = f"\n{explanation}" if explanation else ""

  if actual is None:
    pytest.fail(none_returned_hint(call), pytrace=False)

  if type(actual) != type(expected):
    pytest.fail(
        f"{call} returned {actual!r} (a {type(actual).__name__}), but it should return "
        f"{expected!r} (a {type(expected).__name__})." +
        (" Note that True and False must not have quotes around them." if isinstance(expected, bool) else "") +
        why,
        pytrace=False)

  if isinstance(expected, str):
    pytest.fail(f"{call} returned the wrong string.{why}\n" + compare_strings(expected, actual), pytrace=False)

  pytest.fail(f"{call} returned {actual!r}, but it should return {expected!r}.{why}", pytrace=False)


def compare_strings(expected, actual):
  """Show two one-line strings one above the other, with a ^ under the first
     character that differs (so the difference can be seen without colours)"""
  first_difference = next(
      (i for i, (e, a) in enumerate(zip(expected, actual)) if e != a), min(len(expected), len(actual)))
  # +1 for the opening quote that repr() adds
  result = (f"  Expected: {expected!r}\n"
            f"  Returned: {actual!r}\n"
            f"            {' ' * (first_difference + 1)}^ first difference")
  if actual.lower() == expected.lower():
    result += "\nHINT: the only difference is upper/lower case letters."
  elif actual.strip() == expected.strip():
    result += "\nHINT: the only difference is extra spaces at the start or end."
  return result


def none_returned_hint(call):
  return (f"{call} returned None. This usually means your function has no `return` statement for this case, "
          f"or uses print() where it should use return.")


def check_returns_instead_of_printing(capsys, function, *args):
  """Fail with a helpful message if calling function prints something or returns None"""
  call = f"{function.__name__}({', '.join(repr(a) for a in args)})"
  result = function(*args)
  printed = capsys.readouterr().out
  if printed != "":
    pytest.fail(
        f"{call} printed {printed.strip()!r}. Functions in this lab must *return* their result instead of printing it. "
        f"(Use print() in scratchpad.py or q5.py to display what your functions return.)",
        pytrace=False)
  if result is None:
    pytest.fail(none_returned_hint(call), pytrace=False)
  return result


def find_print_calls(module_name):
  """Return the line numbers of all print() calls in src/<module_name>.py (comments are ignored)"""
  tree = parse_source(module_name)
  return [
      node.lineno for node in ast.walk(tree)
      if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print"
  ]


def imported_modules(module_name):
  """Return the set of module names imported by src/<module_name>.py"""
  tree = parse_source(module_name)
  names = set()
  for node in ast.walk(tree):
    if isinstance(node, ast.Import):
      names.update(alias.name for alias in node.names)
    elif isinstance(node, ast.ImportFrom) and node.module:
      names.add(node.module)
  return names


def defined_function_names(module_name):
  """Return the names of all functions defined in src/<module_name>.py"""
  tree = parse_source(module_name)
  return [node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]


def red(s):
  return "\033[0;91m" + s + "\033[39m\033[49m"  #"\033[0m"


def green(s):
  return "\033[0;92m" + s + "\033[39m\033[49m"  #"\033[0m"


def purple(s):
  return "\033[0;95m" + s + "\033[39m\033[49m"  #"\033[0m"


def show_ws(s):
  """Render spaces as a visible middle dot so space differences (e.g. missing
     trailing spaces) are obvious even without color support"""
  return s.replace(' ', '·')


def trimlines(str):
  """Remove empty rows at the end of text so trailing blank lines don't cause
     spurious differences. Line widths are left untouched so real trailing
     space mismatches between truth and test remain visible in diff()"""
  lines = str.split("\n")
  lines.reverse()
  first_non_empty_line_idx = 0
  for line in lines:
    if line.strip() != "":
      break
    first_non_empty_line_idx += 1
  lines = lines[first_non_empty_line_idx:]
  lines.reverse()

  return "\n".join(lines)


def output_is_equivalent(truth, test, trim=False):
  if trim:
    truth = trimlines(truth)
    test = trimlines(test)
  return truth == test


def diff(truth, test):
  truth = trimlines(truth)
  test = trimlines(test)

  test = test.split("\n")
  d = ""
  y = 0
  for line in truth.split("\n"):

    # Truth drawing has more rows than test drawing
    if y >= len(test):
      d += purple(show_ws(line) + "↵")
    else:
      x = 0
      for expected in line:
        # truth line continues beyond end of test line: the remaining
        # expected characters (including this one) were never typed
        if x >= len(test[y]):
          d += purple(show_ws(line[x:])) + red("↵")
          x = len(line)
          break
        else:
          yours = test[y][x]
          if yours == expected:
            d += green(show_ws(expected))
          elif yours != ' ':
            # show what was actually typed; a colored space would be invisible
            d += red(show_ws(yours))
          else:
            d += purple(show_ws(expected))
        x += 1

      # test line continues beyond end of truth line: the extra
      # characters (including the one at x) were unexpected
      if x < len(test[y]):
        d += purple("↵") + red(show_ws(test[y][x:]) + "↵")
      elif x == len(test[y]):
        d += green("↵")

    d += "\n"

    y += 1

  # Test drawing has more rows than truth drawing
  if y < len(test):
    d += red("↵\n".join(show_ws(l) for l in test[y:]) + "↵\n")

  return d


def format_message(msg, expected, yours):
  theDiff = ""
  try:
    theDiff = diff(expected, yours)
  except Exception:
    print(traceback.format_exc())

  return f"{msg}\nExpected: (↵ represents end of line; · represents a space)\n" + show_ws(expected).replace(
      '\n', '↵\n'
  ) + f"\nBut got:\n" + show_ws(yours).replace("\n", "↵\n") + (
      f"\nDifference: ({green('green')}=correct; {purple('purple')}=expected but missing; {red('red')}=unexpected)\n{theDiff}"
      if theDiff else "")


def mock_input_func(answers):
  i = 0

  def _in(p):
    nonlocal i
    try:
      r = answers[i]
      print(p + r)
    except IndexError:
      raise IOError(
          "Test expected program to be done but it is still awaiting input")
    i += 1
    return r

  return _in


def expect_assertion_error(f, fname, argnum, argtypestr):
  try:
    f()
  except AssertionError as e:
    pass
  except:
    assert False, f"The {fname} function must raise an AssertionError if the {argnum} argument {argtypestr}"


def assert_assertion_message_equals(f, msg, argnum, argtypestr):
  with pytest.raises(AssertionError) as err:
    f()

  assert msg == str(
      err.value
  ), f"The raised error must have the message '{msg}' when the {argnum} argument {argtypestr}"
