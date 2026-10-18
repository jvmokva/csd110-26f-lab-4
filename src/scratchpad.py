# Use comments to manage which of your code files to run

#import q1
#import q2
#import q3
#import q4

# You may add code below here to do your own tests of your functions






def centurize_year(year):
    century = abs(year) // 100
    if abs(year) % 100 != 0:
        century = century + 1
    return print(century)

centurize_year(int(input()))