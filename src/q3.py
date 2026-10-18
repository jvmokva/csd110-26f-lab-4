import q2

def is_year_lucky(year):
    """
This function pick the leap year previously checked and verify if the year is also an lucky year



    """
    leap_result = q2.is_leapyear(year)
    if leap_result == True and (year % 7 == 0 or year % 13 == 0):
        return True
    else:
        return False
    