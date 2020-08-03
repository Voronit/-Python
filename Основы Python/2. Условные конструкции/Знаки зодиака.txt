month = input ("Enter the month of your birth: ")
day = int(input ("Enter your birthday: "))
if month == "January":
  if (day >= 1 and day < 21):
    print("You are Capricorn")
  else:
    print("You are Aquarius")
elif month == "February":
  if (day >= 1 and day < 19):
    print("You are Aquarius")
  else:
    print("You are Pisces")
elif month == "March":
  if (day >= 1 and day < 21):
    print("You are Pisces")
  else:
    print("You are an Aries")
elif month == "April":
  if (day >= 1 and day < 21):
    print("You are an Aries")
  else:
    print("You are a Taurus")
elif month == "May":
  if (day >= 1 and day < 22):
    print("You are a Taurus")
  else:
    print("You are Gemini")
elif month == "June":
  if (day >= 1 and day < 22):
    print("You are Gemini")
  else:
    print("You are Cancer")
elif month == "July":
  if (day >= 1 and day < 23):
    print("You are Cancer")
  else:
    print("You are a lion")
elif month == "August":
  if (day >= 1 and day < 24):
    print("You are a lion")
  else:
    print("You are Virgo")
elif month == "September":
  if (day >= 1 and day < 24):
    print("You are Virgo")
  else:
    print("You are Libra")
elif month == "October":
  if (day >= 1 and day < 24):
    print("You are Libra")
  else:
    print("You are a Scorpio")
elif month == "November":
  if (day >= 1 and day < 23):
    print("You are a Scorpio")
  else:
    print("You are a Sagittarius")
else:
  if (day >= 1 and day < 22):
    print("You are a Sagittarius")
  else:
    print("You are Capricorn")