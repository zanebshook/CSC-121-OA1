"""Downloading Data"""
#import necessary modules
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
#create a variable for where we are getting our data
path = Path('weather_data/sitka_weather_2021_simple.csv')
#use splitlines method to get a list of all the lines in the file
#assign them to a variable called lines
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines) #create a reader object to parse each line
header_row = next(reader) #call next() once to get the header of each row
#number each header as its position in the list
for index, column_header in enumerate(header_row):
    print(index, column_header)

"""Extract and Read Data"""
#create an empty list to hold the dates and high temperatures
dates, highs = [], []
for row in reader:
    high = int(row[4]) #pull the value from row 4 as an integer
    #convert the date from a string
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    highs.append(high) #add it to the list 'highs'
    dates.append(current_date) #add it to the list 'dates'

"""Plotting Data in a Temperature Chart"""
#plot high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red') #plot list of highs in red
#set axes labels, title, and tick parameters
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #auto format the x-axis dates
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()