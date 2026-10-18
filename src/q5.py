
import q1
import q2
import q3
import q4
"""
In the blocks bellow we are putting all the functions together and asking for the user to input a year

As the return of the leap and lucky year functions were Booleans, i did a conditional to convert in something readable


"""

year = input("Enter a year: ")
print(f"The year {year} is ...")
print(f"...the year of the {q1.get_year_animal(int(year))}")
print(f"...in the {q4.centurize_year(int(year))}")
if q2.is_leapyear(int(year)) == True:
    print(f"...leap year")
else:
    print(f"...not a leap year")
if q3.is_year_lucky(int(year)) == True:
    print(f"...lucky year")
else:
    print(f"...not a lucky year")
    


