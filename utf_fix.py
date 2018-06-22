import csv
from datetime import datetime
import pytz

def counter(to_be_counted):
  count = 0
  for each in to_be_counted:
    count += 1
  return count

def timestamp_format(timestamp_line):
  pacific_tz = pytz.timezone('US/Pacific')
  converted_time = datetime.strptime(timestamp_line, "%m/%d/%y %I:%M:%S %p")
  pacific_time = converted_time.replace(tzinfo=pacific_tz)
  eastern_tz = pytz.timezone('US/Eastern')
  eastern_time = pacific_time.astimezone(eastern_tz).replace(tzinfo=None)
  return eastern_time

def address_format(address_line):
  return address_line

def zip_format(zip_line):
  newstring = zip_line
  count = counter(zip_line)
  while count < 5:
    newstring = "0" + newstring
    count = counter(newstring)
  return newstring
  
def name_format(name_line):
  uppercase_name_line = name_line.upper()
  return uppercase_name_line
  
def duration_format(foo_duration, bar_duration):
  foo_duration_split_time = foo_duration.split(':')
  foo_duration_hour = foo_duration_split_time[0]
  foo_duration_minute = foo_duration_split_time[1]
  foo_duration_second = foo_duration_split_time[2]

  bar_duration_split_time = bar_duration.split(':')
  bar_duration_hour = bar_duration_split_time[0]
  bar_duration_minute = bar_duration_split_time[1]
  bar_duration_second = bar_duration_split_time[2]

  foo_duration_seconds = (int(foo_duration_hour)*3600) + (int(foo_duration_minute)*60) + float(foo_duration_second)
  bar_duration_seconds = (int(bar_duration_hour)*3600) + (int(bar_duration_minute)*60) + float(bar_duration_second)

  return (foo_duration_seconds, bar_duration_seconds) 

def total_duration_calculation(duration):
  total_duration = duration[0] + duration[1]
  return total_duration

def read_file():
  file_list = []
  with open('sample.csv', newline='') as File:
    reader = csv.reader(File)
    for i, row in enumerate(reader):
      if i != 0:
        timestamp = timestamp_format(row[0])
        zip_code = zip_format(row[2])
        address = address_format(row[1])
        name = name_format(row[3])
        duration = duration_format(row[4], row[5])
        total_duration = total_duration_calculation(duration)
        file_list.append([timestamp, address, zip_code, name, duration[0], duration[1], total_duration, row[7]])
    return file_list

def write_file():
  broken_file = read_file()
  with open('normalized.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Address', 'ZIP', 'FullName', 'FooDuration', 'BarDuration', 'TotalDuration', 'Notes'])
    
    for line in broken_file:
      writer.writerow(line)
      
      
if __name__ == "__main__":
  write_file()