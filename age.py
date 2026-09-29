from datetime import datetime
date = datetime.now()
date = date.strftime("%Y-%m-%d %H:%M:%S")
date = date.split()
current_date = date[0].split("-")
current_date.reverse()
current_day = int(current_date[0])
current_month = int(current_date[1])
current_year = int(current_date[2])
given_date = input("Give a date in the format (dd-mm-yyyy): ")
given_date = given_date.split("-")
try:
    given_year = int(given_date[2])
    given_day = int(given_date[0])
    given_month = int(given_date[1])
except:
    given_year = False
    given_day = False
    given_month = False


def days_of_month(month: int):
    if month == 2:
        return 29
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def age(day, month, year):
    if not (day and month and year):
        return "This format is not valid"
    if month > 12 or day > days_of_month(month):
        return "Not a valid date"
    elif current_year < year:
        return "this date has not occured yet"
    elif current_month < month and current_year <= year:
        return "this date has not occured yet"
    elif current_day < day and current_month <= month and current_year <= year:
        return "this date has not occured yet"
    if month < current_month or (month <= current_month and day < current_day):
        age = current_year - year
    else:
        age = current_year - year - 1
    if age < 0:
        age = 0
    return age


print(age(given_day, given_month, given_year))
