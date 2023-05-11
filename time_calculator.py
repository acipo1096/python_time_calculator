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

  start_hour = int(start_list[0])
  print(time_of_day)

  minutes = int(start_list[1]) + int(duration_list[1])

  if (duration_list[1] == '0:00'):
    print(str(start_hour)) + str(minutes)
    return 0;

  if (duration_list[0] == '24' and duration_list[1] == '00'):
    print(str(start_hour) +":" + str(minutes) + ' ' +time_of_day)
    return 0;

  if (time_of_day == "PM"):
    start_hour = start_hour + 12
    print(start_hour)
  
  hour = start_hour + int(duration_list[0])
    
  
  if (minutes < 10):
    formatted_minutes = str(minutes).zfill(2)
    print(str(hour) + ":" + formatted_minutes)
    
  elif (minutes > 59):
    if (duration_list[0] == '0'):
      hour = hour + 1
      minutes = minutes - 60
      formatted_minutes = str(minutes).zfill(2)
      print(str(hour) + ":" + formatted_minutes)
    else:
      minutes = minutes - 60
      formatted_minutes = str(minutes).zfill(2)
      print(str(hour) + ":" + formatted_minutes)
      
  else:
    formatted_minutes = str(minutes)
    print(str(hour) + ":" + formatted_minutes)

  if (hour >= 13 and time_of_day == "PM"):
    if(hour > 23):
      formatted_hour = str(hour - 24)
      time_of_day = "AM"
      print(formatted_hour + ":" + formatted_minutes + " " + time_of_day + " (next day)")
    else:
      formatted_hour = str(hour)
      time_of_day = "AM"
      print(formatted_hour + ":" + formatted_minutes + " " + time_of_day)

  elif (hour <= 12 and time_of_day == "AM"):
    formatted_hour = str(hour)
    time_of_day = "PM"
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
