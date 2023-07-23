short_months = {3, 5, 8, 10}

day_of_week = 0 # Monday
day_of_month = 0
month = 0
year = 1900

count =  0

def is_leapyear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True

while True:

    if day_of_week == 6 and day_of_month == 0 and year != 1900:
        count += 1
    
    day_of_month += 1
    day_of_week += 1
    day_of_week %= 7

    if month == 1: # Feb
        if day_of_month == 29 or (not is_leapyear(year) and day_of_month == 28):
            month += 1
            day_of_month = 0
    elif month in short_months:
        if day_of_month == 30:
            month += 1
            day_of_month = 0
    else:
        if day_of_month == 31:
            month += 1
            day_of_month = 0

    if month == 12:
        year += 1
        month = 0

    if year == 2001:
        break

print(count)
