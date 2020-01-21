day1 = "Monday"
day2 = "Tuesday"
day3 = "Wednesday"
day4 = "Thursday"
day5 = "Friday"
day6 = "Saturday"
day7 = "Sunday"
  #function returns day of the week
def tell_day_january(date):
  if date == 6 or date == 13 or date == 20 or date == 27:
    return day1
  elif date == 7 or date == 14 or date == 21 or date == 28:
    return day2
  elif date == 1 or date == 8 or date == 15 or date == 22 or date == 29:
    return day3
  elif date == 2 or date == 9 or date == 16 or date == 23 or date == 30:
    return day4
  elif date == 3 or date == 10 or date == 17 or date == 24 or date == 31:
    return day5 + ", cheers to the freakin weekend"
  elif date == 4 or date == 11 or date == 18 or date == 25:
	  return day6 + ", cheers to the freakin weekend"
  elif date == 5 or date == 12 or date == 19 or date == 26:
    return day7 + ", cheers to the freakin weekend"
  #end day of the week function
#todays_date = input("enter todays date")
calendar_date = tell_day_january(17)
print("Hello World! Today is " + calendar_date + ".")