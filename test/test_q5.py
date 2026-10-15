import pytest
import runpy
import util


def run_q5(monkeypatch, capsys, year):
    """Run src/q5.py as if the user typed year when asked for input.
       Returns (everything the program printed, number of times input() was called)"""
    input_calls = 0

    def mock_input(prompt=""):
        nonlocal input_calls
        input_calls += 1
        if input_calls > 5:
            pytest.fail("src/q5.py kept asking for input. It should ask for the year only once.", pytrace=False)
        print(prompt + year)
        return year

    monkeypatch.setattr("builtins.input", mock_input)
    # pytest.fail is called after the except blocks so that the original error
    # isn't also printed as part of the test output
    try:
        runpy.run_path(str(util.SRC_DIR / "q5.py"), run_name="__main__")
        return capsys.readouterr().out, input_calls
    except SyntaxError as e:
        # e.filename may be a different file (e.g. q5.py imports a q1.py with a typo)
        filename = util.Path(e.filename).name if e.filename else "q5.py"
        message = (
            f"Python can't understand the code in src/{filename}, so src/q5.py could not be run.\n"
            f"  {type(e).__name__}: {e.msg} (line {e.lineno} of src/{filename})\n"
            f"Run `python src/{filename}` in the terminal to see more details about the error.")
    except Exception as e:
        where = util._line_in_src(e)
        hint = ""
        if isinstance(e, TypeError):
            hint = ("\nHINT: input() always gives you a string (text), even when the user types a number. "
                    "Did you convert it to an int with int() before passing it to your functions?")
        message = (
            f"src/q5.py crashed when the user entered {year}:\n"
            f"  {type(e).__name__}: {e}" + (f" (at {where})" if where else "") + hint + "\n"
            f"Run `python src/q5.py` and enter {year} to see the full error.")
    pytest.fail(message, pytrace=False)


def test_q5_imports_all_of_q1_q2_q3_q4():
    imported = util.imported_modules("q5")
    missing = [name for name in ["q1", "q2", "q3", "q4"] if name not in imported]
    assert missing == [], (
        f"src/q5.py must import the functions you wrote in the other files, but it does not import: {', '.join(missing)}")


def test_q5_does_not_define_any_functions():
    defined = util.defined_function_names("q5")
    assert defined == [], (
        f"src/q5.py should not define any functions, but it defines: {', '.join(defined)}. "
        f"Import the functions you need from the other files, then call them.")


def test_q5_runs_without_crashing(monkeypatch, capsys):
    run_q5(monkeypatch, capsys, "1234")


def test_q5_asks_for_input_once(monkeypatch, capsys):
    output, input_calls = run_q5(monkeypatch, capsys, "1234")
    assert input_calls == 1, (
        f"src/q5.py should call input() exactly once (to ask for the year), but it called input() {input_calls} times.")


def test_q5_does_not_print_functions(monkeypatch, capsys):
    output, input_calls = run_q5(monkeypatch, capsys, "1234")
    assert "<function" not in output, (
        f"Your program printed a function instead of the value it returns:\n{output}\n"
        f"HINT: to call a function you need parentheses and an argument, e.g. is_leapyear(year), not is_leapyear")


@pytest.mark.parametrize("year, animal, century", [
    ("1234", "Horse", "13th century CE"),
    ("2028", "Monkey", "21st century CE"),
])
def test_q5_displays_animal_and_century(monkeypatch, capsys, year, animal, century):
    output, input_calls = run_q5(monkeypatch, capsys, year)
    assert animal in output, (
        f"When the user enters {year}, your program should say that it is the year of the {animal}. Your program printed:\n{output}")
    assert century in output, (
        f"When the user enters {year}, your program should say that it is in the {century}. Your program printed:\n{output}")


def test_q5_displays_leap_year_and_lucky_information(monkeypatch, capsys):
    # 2028 is a leap year and lucky; 1234 is neither, so what the program says about them must differ
    output_2028, input_calls = run_q5(monkeypatch, capsys, "2028")
    output_1234, input_calls = run_q5(monkeypatch, capsys, "1234")
    for word, description, adjective in [("leap", "is a leap year", "a leap year"), ("luck", "is lucky", "lucky")]:
        lines_2028 = [line.replace("2028", "") for line in output_2028.splitlines() if word in line.lower()]
        lines_1234 = [line.replace("1234", "") for line in output_1234.splitlines() if word in line.lower()]
        assert lines_2028, (
            f"Your program should tell the user whether the year {description}. "
            f"When the user entered 2028, your program printed:\n{output_2028}")
        assert lines_2028 != lines_1234, (
            f"Your program says the same thing about 2028 and 1234, but 2028 is {adjective} "
            f"and 1234 is not. Make sure you are using the values returned by is_leapyear and is_year_lucky.")
