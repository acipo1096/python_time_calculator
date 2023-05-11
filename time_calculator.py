import re


def add_time(start, duration, **day):

  days_of_week = {
    'Sunday': 1,
    'Monday': 2,
    'Tuesday': 3,
    'Wednesday': 4,
    'Thursday': 5,
    'Friday': 6,
    'Saturday': 7
  }

  formatted_minutes = ""

  get_TOD = start.split(" ")
  time_of_day = get_TOD[1]
  print("The time of day is: ", time_of_day)

  regex = re.compile('[0-9:]+')
  filtered_string = regex.search(start)
  start_list = filtered_string.group(0).split(":")
  print("Start list: ", start_list)

  filtered_string = regex.search(duration)
  duration_list = filtered_string.group(0).split(":")
  print("Duration list: ", duration_list)

  hour = int(start_list[0]) + int(duration_list[0])
  minutes = int(start_list[1]) + int(duration_list[1])
  if (minutes < 10):
    formatted_minutes = str(minutes).zfill(2)
    print(str(hour) + ":" + formatted_minutes)
  elif (minutes > 59):
    minutes = minutes - 60
    formatted_minutes = str(minutes).zfill(2)
    print(str(hour) + ":" + formatted_minutes)
  else:
    formatted_minutes = str(minutes)
    print(str(hour) + ":" + formatted_minutes)

  if (hour >= 13 and time_of_day == "PM"):
    formatted_hour = str(hour - 12)
    time_of_day = "AM"
    print(formatted_hour + ":" + formatted_minutes + " " + time_of_day)
    
  elif (hour >= 13 and time_of_day == "AM"):
    formatted_hour = str(hour - 12)
    time_of_day = "PM"
    print(formatted_hour + ":" + formatted_minutes + " " + time_of_day)   
    
  elif (hour < 13 and time_of_day == "PM"):
    formatted_hour = str(hour)
    print(formatted_hour + ":" + formatted_minutes + " " + time_of_day)

  new_time = 0
  return new_time
