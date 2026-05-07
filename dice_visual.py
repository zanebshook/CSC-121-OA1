import plotly.express as px  #import plotly.express as a variable 'px'
from die import Die #import Die class
die_1 = Die() #create an instance of a die
die_2 = Die() #create another instance of a die
results = []  #create and empty list to store results
for roll_num in range(1000):  #roll the dice 1000 times
    #the result is the 2 dice added together
    result = die_1.roll() + die_2.roll()
    results.append(result)  #store the results to empty list 'results'

"""Analyze Results"""
frequencies = []  #empty list to store frequencies
max_result = die_1.num_sides + die_2.num_sides #the max result of rolling 2 dice
poss_results = range(2, max_result+1)  #possible results of rolling the dice
#for each possible results in the range poss_results, count how many times 
#each result appears in the list 'results'. store it in the list 'frequencies'
for value in poss_results:  
    frequency = results.count(value)  
    frequencies.append(frequency)  
print(frequencies)

"""Visualize Results of Rolling Two D6 Dice 1000 Times"""
#create a bar graph showing the frequency of each possible result
title = "Results of Rolling Two D6 Dice 1000 Times" 
labels = {'x': 'Result', 'y': 'Frequency of Result'}
#call plotly and plug in variable for x/y values, title, and axis labels
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
#customize the labels of each tick
fig.update_layout(xaxis_dtick=1)
fig.show()