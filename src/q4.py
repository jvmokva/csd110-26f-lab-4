


def centurize_year(year):
    century = abs(year) // 100
    if year == 0:
        year = year + 1
    if abs(year) % 100 != 0:
        century = century + 1
    if year < 0:
        era = "BCE"
    else:
        era = "CE"
    if century % 100 in (11, 12, 13):
        suffix = "th"
    elif century % 10 == 1:
        suffix = "st"
    elif century % 10 == 2:
        suffix = "nd"
    elif century % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{century}{suffix} century {era}"