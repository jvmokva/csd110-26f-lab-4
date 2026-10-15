import pytest


class InputCalledDuringTest(Exception):
  pass


@pytest.fixture(autouse=True)
def block_input(monkeypatch):
  """Replace input() so that code which asks for input fails with a clear
     message instead of pytest's confusing 'reading from stdin' error.
     (Tests that need input, like the q5 tests, provide their own input())"""

  def _input(prompt=""):
    raise InputCalledDuringTest(
        "Your code called input() while being tested. Functions in q1.py to q4.py "
        "get the year through their parameter; they should not ask the user for it. "
        "If you added code to try out your function, move it into scratchpad.py.")

  monkeypatch.setattr("builtins.input", _input)
