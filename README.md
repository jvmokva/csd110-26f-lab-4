# Lab 4 - Boolean Expressions and Conditionals

## Setup

1. Click the "**Use this template**" button near the top of this repository on GitHub
2. Set the following properties on the GitHub repository, then click "Create repository":
    - **Owner**: your GitHub username (NOT the course organization)
    - **Name**: csd110-26f-lab-4
    - **Visibility**: Private
3. In your new repository, go to Settings -> Collaborators, and add your instructor as a collaborator.
4. Create a branch named `lab-4` on which to do your lab work
5. Create a Codespace on that branch, and open it (give it a few minutes to initialize)
6. In your Codespace terminal, verify your setup using `gh lab setup-check`

## Overview 

In this lab you will create several small functions that use Boolean expressions and conditional statements to perform simple computations.  You will also create a small program that uses these functions to display information about a year entered by the user.

## Required Reading 

It is assumed that you have watched all lecture videos and completed readings and practice exercises up to the end of Chapter 5 (not including Chapter 4) in the course textbook.  If you have not done so yet, you should! 

### Reflections

As you are working on your lab, help yourself remember important things by taking notes in `reflections.md`. Record notes about anything you think important to remember, any problems you encountered and how you resolved them, and any remaining questions you may still have.

> **NOTE**: `reflections.md` is a 'markdown' file.  Markdown is a markup language that has simple syntax for adding formatting to plain text documents. See [this documentation on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to learn how to format text in a markdown file.

### AI Use

> **IMPORTANT**: ***Failure to include an accurate AI Use Statement as described below may result in a lab grade deduction of up to 100% depending on your instructor's evaluation of how well you understand the code you submit***

You MAY use AI as a LEARNING AID to help you understand topics you are needing extra help with.
You may NOT use AI to do your work for you or to avoid having to think and learn on your own.

#### AI Use Statement

**Whether or not you use AI**, you MUST include an AI Use Statement in your `reflections.md` document that indicates clearly:

- Which specific AI tools you used in the completion of this lab (or an explicit statement that you did not use any AI tools).
- Links to or copies of **ALL** AI chats you had related to this assignment. 

> **IMPORTANT:** if sharing a link, do NOT simply copy the URL from your browser; you MUST click the **Share** button and create a public link.

Examples:
- I used ChatGPT to help me better understand the lab requirements.  Below are links to my ChatGPT chats.
- I used Claude to give me examples of statements vs expressions in Python.  Below are links to my conversation.
- I did not use any AI tools to complete this lab.

### Running your code

#### From the terminal

1. Open the terminal (View -> Terminal)
2. Enter a command like the following `python path/to/script.py`.  For example, to run the `q1.py` script in the `src` folder, run `python src/q1.py`.

#### Using the debugger

1. Open the Python file you want to run
2. Open the 'Run and Debug' panel (right side, right-arrow icon with bug in lower left corner). 
3. Make sure the "Python Debugger: Current File" configuration is selected in the dropdown at the top of the panel.
4. Click the green arrow button to run the currently opened Python file

### Testing your code

A set of tests have been prepared for this lab that will help you determine if your code is correct or not.

#### Running tests 

| Task | Command | Example |
|------|---------|---------|
| Run all tests | `pytest` | `pytest` |
| Stop at the first failing test while working | `pytest -x` | `pytest -x` |
| Run one test file | `pytest <path_to_file>` | `pytest test/test_q1.py` |
| Run one test function | `pytest <path_to_file>::<function_name>` | `pytest test/test_q2.py::test_1900_is_not_leap_year` | 

While working, use `pytest -x` to focus on one failure at a time. Fix that issue and run the same command again to continue through the tests. Once the tests are passing this way, run `pytest` to check the entire lab.

#### Reading test output

The output of the tests will give you an indication of which tests passed or failed. For any failed tests, you will also see messages that should help you determine why the test failed.

Here are some tips for dealing with failing tests:

1. The name of the test itself usually gives a clue as to what the test is checking (e.g. `test_1900_is_not_leap_year`).
2. Read the message under the test name. It usually says which function call was tested, what your function returned, what it should have returned, and why.
3. When a string is wrong, the message shows the "Expected" and "Returned" values one above the other, with a `^` under the first character that is different.
4. If a line starting with `src/` appears in the output, it shows the line in **your** code where the problem happened.
5. The tests for each part are in order, starting with the simplest. Fix the first failing test before worrying about later ones. Often fixing one test fixes other failing tests as well.
6. When working on a failing test, run just that test (see above) so you can focus on its output without having to wade through the output of all the other tests.

#### Passing tests does not guarantee correctness

If all the tests passed, you can be reasonably sure that your code is correct, **BUT PASSING ALL TESTS DOES NOT NECESSARILY MEAN YOU WILL GET 100%** because some grades are assigned to non-coding tasks, and it is sometimes possible to create incorrect programs that do pass the tests.

##  Instructions 

> **IMPORTANT**: Any time you must name functions or variables, you are expected to use meaningful names.  Failing to do so will result in a lower grade. You should also employ meaningful code comments when there are non-obvious things to discuss about how your code works.

> **IMPORTANT**: Don't forget to include appropriate docstrings for all your functions. Failing to do so will result in a lower grade.

> **IMPORTANT**: Most of the functions you create in this lab are **PURE** functions, meaning they simply accept values and return values but have no other side effect. In order to test that your functions are working, you may wish to write some code that calls them and prints the returned values. Do so in the `scratchpad.py` file and **NOT** in the other lab code files. Module files should not produce output when imported.

> **NOTE REGARDING YEARS**: In all functions below that accept a year value, you may assume that the value given will be an integer. Negative years must be accepted, and represent years B.C.E.  E.g. The year -543 would represent the year 543 B.C.E.

### Part 1 - Determine the Chinese Zodiac animal of a year

Create a function that takes a year and returns (as a string) the animal for that year in the Chinese Zodiac.

1. In `q1.py`, define a **PURE** function named `get_year_animal`

   1. The function's input is an integer representing the current year
   2. The function must return a string corresponding to the animal for the given year in the Chinese Zodiac, (i.e., one of Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig).

        > **NOTE:** You do NOT need to take into account that the Chinese new year starts on different days than in the Gregorian calendar. Assume that the given year corresponds to that Chinese year. E.g. 2000 yields the value `"Dragon"` and 1970 yields `"Dog"`.  See [this Wikipedia article](https://en.wikipedia.org/wiki/Chinese_zodiac) to determine which years correspond to which animals.

        > **HINT:** The modulus operator `%` is very useful here! Every 12 years, the same list of animals cycles. The year 2020 was a year of the Rat, and 2020 divided by 12 has a remainder of 4.  In fact, _any_ year with a remainder of 4 when divided by 12 will _also_ be a year of the Rat, etc. You can use this fact to create a multi-branch conditional statement that determines which string to return in your function.

### Part 2 - Determine if a year is a leap year

Create a Boolean function that takes a year and returns `True` if it is a leap year, or `False` otherwise.

1. In `q2.py`, define a **PURE Boolean** function named `is_leapyear`

    1. The function's input is an integer year value
    2. The function returns `True` if the given year is a leap year and `False` otherwise

       > **NOTE:** a leap year must be divisible by 4, BUT years that are ALSO divisible by 100 are NOT leap years unless they are ADDITIONALLY divisible by 400. That is, if a year is divisible by 100 but NOT 400 it is NOT a leap year. (See https://www.mathsisfun.com/leap-years.html)

### Part 3 - Determine if a year is lucky

For this part, we'll define a 'lucky year' as one that is both a leap year and divisible by one of the numbers 7 or 13. Your job is to write a function that determines if a given year is lucky according to this definition.

1. In `q3.py` define a **PURE Boolean** function named `is_year_lucky`
    1. The function's input is a integer year value
    2. The function returns `True` if the given year is a leap year AND is divisible by either 7 or 13; it returns `False` otherwise.
       
       > **NOTE:** Be careful about operator precedence!
       
    4. Yes, you should import the `is_leapyear` function you just created and call it as part of the body of this function.


### Part 4 - Determine a year's century

Create a function that takes a year and returns a string of the form "Nth century CE" or "Nth century BCE" (where N is the actual number of the century) based on the given year.  (See the examples below.)

1. In `q4.py` define a **PURE** function named `centurize_year`
    
    2. The function's input is an integer year value
    3. The function returns a string of the form `#<suffix> century <era>` where `#` is replaced by the numeric century, `<suffix>` is replaced by one of `st`, `nd`, `rd`, or `th`, and `<era>` is either `CE` or `BCE` depending on the year.

       > **NOTE:** Assume you are working with the [Gregorian Calendar](https://www.khanacademy.org/humanities/ap-art-history/start-here-apah/brief-histories-apah/a/common-questions-about-dates) where there is no year 0 (in your code, just count it as a first-century year), and centuries start with the year 1. E.g. 2000 was the last year in the the 20th century and 2001 was the first year of the 21st century. See the tests, and the examples below for more examples of correct century labels.

       > **HINT:** Consider breaking this problem into smaller pieces. E.g. First determine the numeric century, then determine the suffix, then determine the era, and finally combine these pieces into a single string to return. Perhaps create helper functions to do some of these subtasks!

       > **HINT:** The `%` operator will be helpful here again.

   **Examples:**
   ```python
   centurize_year(2020) # returns "21st century CE"
   centurize_year(100)  # returns "1st century CE"
   centurize_year(101)  # returns "2nd century CE"
   centurize_year(1100) # returns "11th century CE"
   centurize_year(1101) # returns "12th century CE"
   centurize_year(0)    # returns "1st century CE"
   centurize_year(-1)   # returns "1st century BCE"
   centurize_year(-100) # returns "1st century BCE"
   centurize_year(-101) # returns "2nd century BCE"
   ```

### Part 5 - Put it all together!

In this part, you will make use of all the pure functions you've created in this lab and pull them together into an interactive program.

1. Do your work for this part in `q5.py` using the code you have already created (imported, **NOT copied**):
1. Prompt the user to enter a year
2. Display complete information about the year the user enters, including
    
    1. Which Chinese zodiac animal corresponds to that year
    2. Which century the year is in
    3. Whether the year is a leap year
    4. Whether the year is lucky

   **Example program output:**

   ```sh
   Enter a year: 1234
   The year 1234 is...
   ...the year of the Horse
   ...in the 13th century CE
   ...not a leap year
   ...not a lucky year
   ```

   > **NOTE:** Your code should work similar, but does not need to produce exactly the same output

## Reflect

Did you take notes in `reflections.md` as you worked? (See the [Reflections](#reflections) instructions above.) You should!

Did you document your AI usage adequately? (See the [AI Use](#ai-use) instructions above.) You must!

## Submission

1. **Test** your code to verify that it is working as expected (see the [Testing your code](#testing-your-code) section above).
1. **Commit** all changes in your lab files with meaningful commit messages.
2. **Push** your commits to GitHub
3. **Verify** that the code on GitHub is correct
4. Create a **Pull request** using your lab branch as the 'compare' branch and the main branch as the 'base'
5. Navigate to the "Files Changed" tab of your pull request, and **copy the URL** to this page into the lab folder on the LMS.

## Rubric

See the rubric attached to this lab in the LMS
