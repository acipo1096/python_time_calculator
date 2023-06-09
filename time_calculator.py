import re
import math

def add_time(start, duration, day="None"):

  days_of_week = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'
  }

  # Global variables
  next_day = ""
  formatted_minutes = ""
  days_elapsed = ''
  get_number_of_days = 0
  day_key = ''
  new_time = ''

  # STEP 1: Get the time of day
  get_TOD = start.split(" ")
  time_of_day = get_TOD[1]
  # print("AM or PM? ", time_of_day)

  # STEP 2: Separate hours and minutes for your time
  regex = re.compile('[0-9:]+')
  filtered_string = regex.search(start)
  start_list = filtered_string.group(0).split(":")

  # STEP 3: Separate hours and minutes for your duration count
  filtered_string = regex.search(duration)
  duration_list = filtered_string.group(0).split(":")

  #STEP 4: Define the starting hour; get the combined minutes
  start_hour = int(start_list[0])
  minutes = int(start_list[1]) + int(duration_list[1])

  # STEP 5: Convert PM to military time
  if (time_of_day == "PM"):
    start_hour = start_hour + 12

  hour = start_hour + int(duration_list[0])

  day2 = day.lower()
  day3 = day2.capitalize()

  # For loop to match day with dict day
  for i in range(1, len(days_of_week) + 1, 1):
    if (days_of_week[i] == day3):
      day_key = i

  if (day != "None"):
    if ((hour / 24) > 1):
      get_number_of_days = round(hour / 24)
    else:
      get_number_of_days = math.floor(hour / 24)

    next_day = int(get_number_of_days) + day_key

    # Checks if it's still the same day
    if (next_day == day_key):
      next_day = days_of_week[day_key]
    # Checks for how many days to increment
    elif (next_day <= 7):
      next_day = days_of_week[next_day]
    # Checks for Saturday to Sunday, increments day to Sunday
    elif (next_day == 8 and get_number_of_days == 1):
      next_day = days_of_week[1]
    # If goes into next week; resets the counter so it returns a day of the week
    else:
      next_day = days_of_week[(next_day - get_number_of_days) - 1]

  # STEP 6: Format minutes correctly and ensure they reset to zero on the hour
  if (minutes < 10):
    formatted_minutes = str(minutes).zfill(2)
  elif (minutes > 59):
    if (duration_list[0] == '0'):
      hour = hour + 1
      minutes = minutes - 60
      formatted_minutes = str(minutes).zfill(2)
    else:
      minutes = minutes - 60
      formatted_minutes = str(minutes).zfill(2)
  else:
    formatted_minutes = str(minutes)

  if (duration_list[0] == '0' and duration_list[1] == '00'):
    formatted_minutes = str(minutes).zfill(2)
    if (day != "None"):
      new_time = str(
        start_hour
      ) + ":" + formatted_minutes + ' ' + time_of_day + ', ' + next_day + " (same day)"
    else:
      new_time = str(start_hour) + ":" + formatted_minutes + ' ' + time_of_day
    return new_time

  if (duration_list[0] == '24' and duration_list[1] == '00'):
    formatted_minutes = str(minutes).zfill(2)
    if (day != "None"):
      new_time = str(
        start_hour
      ) + ":" + formatted_minutes + ' ' + time_of_day + ', ' + next_day + " (next day)"
    else:
      new_time = str(
        start_hour
      ) + ":" + formatted_minutes + ' ' + time_of_day + " (next day)"
    return new_time

  if (hour >= 13 and time_of_day == "PM"):
    if (hour > 23):
      get_number_of_days = round(hour / 24)

      if (get_number_of_days > 1):
        days_elapsed = " (" + str(get_number_of_days) + " days later)"
      else:
        days_elapsed = " (next day)"

      new_hour = hour - (24 * get_number_of_days)

      # Catches a negative and brings it back to 12 AM
      if (new_hour < 0):
        new_hour = (new_hour - new_hour) + 12

      formatted_hour = str(new_hour)
      time_of_day = "AM"

      if (day != "None"):
        new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day + ", " + next_day + days_elapsed
      else:
        new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day + days_elapsed

    # Converts AM to PM correctly
    else:
      hour = hour - 12
      formatted_hour = str(hour)
      time_of_day = "PM"
      if (day != "None"):
        new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day + ", " + next_day
      else:
        new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day

  # Time period change at 12 PM
  elif (hour <= 12 and time_of_day == "AM"):
    formatted_hour = str(hour)
    time_of_day = "PM"
    new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day

  # New time is between 1PM and 11:59PM
  elif (hour >= 13 and time_of_day == "AM"):
    formatted_hour = str(hour - 12)
    time_of_day = "PM"
    new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day

  # New time is 12PM - 12:59PM
  else:
    formatted_hour = str(hour)
    new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day


  return new_time