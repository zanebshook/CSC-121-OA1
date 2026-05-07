import plotly.express as px  #import plotly.express as a variable 'px'
from die import Die #import Die class
die = Die() #create an instance of a die
results = []  #create and empty list to store results
for roll_num in range(1000):  #roll the die 1000 times
    result = die.roll()  #a variable for each roll of the die
    results.append(result)  #store the results to empty list 'results'

"""Analyze Results"""
frequencies = []  #empty list to store frequencies
poss_results = range(1, die.num_sides + 1)  #possible results of rolling the die
#for each possible results in the range poss_results, count how many times 
#each result appears in the list 'results'. store it in the list 'frequencies'
for value in poss_results:  
    frequency = results.count(value)  
    frequencies.append(frequency)  
print(frequencies)

"""Visualize Results of Rolling One D6 1000 Times"""
#create a bar graph showing the frequency of each possible result
title = "Results of Rolling One D6 1000 Times" 
labels = {'x': 'Result', 'y': 'Frequency of Result'}
#call plotly and plug in variable for x/y values, title, and axis labels
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()