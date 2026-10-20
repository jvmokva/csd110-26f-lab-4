def get_year_animal(year): 
    """ 
    This function will receive a value (year) and return the correspondent Chinese Animal of the year 
    The value must be a int
    """

    if year % 12 == 1:
        return "Rooster"
    if year % 12 == 2:
        return "Dog"
    if year % 12 == 3:
        return "Pig"
    if year % 12 == 4:
        return "Rat"
    if year % 12 == 5:
        return "Ox"
    if year % 12 == 6:
        return "Tiger"
    if  year % 12 == 7:
        return "Rabbit"
    if  year % 12 == 8:
        return "Dragon"
    if year % 12 == 9:
        return "Snake"
    if year % 12 == 10:
        return "Horse"
    if year % 12 == 11:
        return "Goat"
    else:
        return "Monkey"
    


