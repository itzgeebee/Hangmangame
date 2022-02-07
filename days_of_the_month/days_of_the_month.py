#This is a program that takes in two arguments "year" and "month" and returns how many days the month contains


def is_leap(year):
  """This function takes in an argument "year" checks if a year is a leap year; will come in handy when checking february"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year_entered, month_entered):
  """This function takes in two variables year_entered and month_enterd returns the number of days in a month for a particular year"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month_entered > 12 or month_entered < 1:
    return "Invalid Input, please select between 1 and 12"
  if month_entered == 2 and is_leap(year_entered):
        return 29
  return (month_days[month_entered - 1])


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)