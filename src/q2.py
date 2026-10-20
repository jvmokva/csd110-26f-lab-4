import q1

def is_leapyear(y): 
    """ 
    This function check if the year picked is a leapyear.
    If it is will return true, if its not, will return False
    
    """
    if y % 4 == 0:
        if y % 100 == 0:
                if y % 400 == 0:
                    return True
                else:
                    return False
        else:
            return True    
    else:
        return False



