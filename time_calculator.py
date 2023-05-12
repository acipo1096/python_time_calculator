import re

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
  formatted_minutes = ""
  days_elapsed = ''
  get_number_of_days = ''
  # day_key = ''
  new_time = ''

  # STEP 1: Get the time of day
  get_TOD = start.split(" ")
  time_of_day = get_TOD[1]
  # print("AM or PM? ", time_of_day)

  # STEP 2: Separate hours and minutes for your time
  regex = re.compile('[0-9:]+')
  filtered_string = regex.search(start)
  start_list = filtered_string.group(0).split(":")
  print("Start list: ", start_list)
  
  # STEP 3: Separate hours and minutes for your duration count
  filtered_string = regex.search(duration)
  duration_list = filtered_string.group(0).split(":")
  print("Duration list: ", duration_list)

  #STEP 4: Define the starting hour; get the combined minutes
  start_hour = int(start_list[0])
  minutes = int(start_list[1]) + int(duration_list[1])

  def getDay():
    day2 = day.lower()
    day3 = day2.capitalize()
    # For loop to match day with dict day
    for i in range(1,len(days_of_week),1):
        if (days_of_week[i] == day3):
          global day_key
          day_key = i
  getDay()

  
  # STEP 5: Check if time is returning itself or 24 hours in advance
  if (duration_list[0] == '0' and duration_list[1] == '00'):
    formatted_minutes = str(minutes).zfill(2)
    new_time = str(start_hour) +":" + formatted_minutes + ' ' + time_of_day
    print(new_time)
    return new_time;
  if (duration_list[0] == '24' and duration_list[1] == '00'):
    formatted_minutes = str(minutes).zfill(2)
    new_time = str(start_hour) +":" + formatted_minutes + ' ' + time_of_day + " (next day)"
    print(new_time)
    return new_time;

  # STEP 6: Convert PM to military time
  if (time_of_day == "PM"):
    start_hour = start_hour + 12
  hour = start_hour + int(duration_list[0])

  # STEP 7: Format minutes correctly and ensure they reset to zero on the hour
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

  if (hour >= 13 and time_of_day == "PM"):
    if(hour > 23):
      get_number_of_days = round(hour / 24)
      
      if(day != "None"):
        print("day key= ",day_key)
        next_day = int(get_number_of_days) + day_key
        if (next_day <= 7):
          next_day = days_of_week[next_day]
        else: 
          next_day = days_of_week[next_day - get_number_of_days]

      if(get_number_of_days > 1):
        days_elapsed = " (" +str(get_number_of_days) + " days later)"
      else:
        days_elapsed = " (next day)"
      
      new_hour = hour - (24*get_number_of_days)

      # Catches a negative and brings it back to 12 AM
      if(new_hour < 0):
        new_hour = (new_hour - new_hour) + 12
      
      formatted_hour = str(new_hour)
      time_of_day = "AM"

      if(day != "None"):
        new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day +", " + next_day + days_elapsed
      else:
        new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day + days_elapsed
    # Converts AM to PM correctly
    else:
      hour = hour - 12
      formatted_hour = str(hour)
      time_of_day = "PM"
      new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day

  # New time is ???
  elif (hour <= 12 and time_of_day == "AM"):
    formatted_hour = str(hour)
    time_of_day = "PM"
    new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day

  # New time is between 1PM and 11:59PM
  elif (hour >= 13 and time_of_day == "AM"):
    formatted_hour = str(hour - 12)
    time_of_day = "PM"
    new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day

  # elif (hour == 12 and time_of_day == "PM"):
  # New time is 12PM - 12:59PM
  else:
    formatted_hour = str(hour)
    new_time = formatted_hour + ":" + formatted_minutes + " " + time_of_day
    

  print(new_time) 
  return new_time