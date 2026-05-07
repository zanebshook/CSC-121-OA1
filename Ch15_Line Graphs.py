#Generating Data
#Simple Line Graph 
import matplotlib.pyplot as plt #import matplotlib as a variable
input_values = [1, 2, 3, 4, 5] #values for x-axis
squares = [1, 4, 9, 16, 25] #values for y-axis
plt.style.use('seaborn-v0_8')  #selecting a desired style of plot
fig, ax = plt.subplots()  #function to generate plots
ax.plot(input_values, squares, linewidth=3)  #plot data and setting line width
#declare title and label axes
ax.set_title("Square Numbers as a Line Graph", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)  #sizing tick labels
plt.show()  #opens the viewer for the plot

#Plot and Style Individual Points
plt.style.use('seaborn-v0_8')  #selecting a desired style of plot
fig,ax = plt.subplots()  #function to generate plots
ax.scatter(input_values, squares, s=100) #'s argument' to set size of dots
#declare title and label axes
ax.set_title("Square Numbers in Individual Points", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)  #sizing tick labels
plt.show()  #opens the viewer for the plot

#Calculate Data Automatically- with a custom color
x_values = list(range(1, 1001))  #declare a range for x axis from 1 to 1000
#below square every value in the range given in x_values
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8')  #selecting a desired style of plot
fig, ax = plt.subplots()  #function to generate plots
ax.scatter(x_values, y_values, color='red', s=10)
    #declares which values to plot, color scale and size of dots
#declare title and label axes
ax.set_title("Square Numbers, Generated Automatically in Red", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)  #sizing tick labels
ax.axis([0, 1100, 0, 1_100_000]) #set range for x and y axis
ax.ticklabel_format(style='plain') #customize tick labels 
plt.show()  #opens the viewer for the plot

#Calculate Data Automatically- with a color scale
x_values = list(range(1, 1001))  #declare a range for x axis from 1 to 1000
#below square every value in the range given in x_values
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8')  #selecting a desired style of plot
fig, ax = plt.subplots()  #function to generate plots
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
    #declares which values to plot, color scale and size of dots
#declare title and label axes
ax.set_title(
    "Square Numbers, Generated Automatically With Color Scale", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)  #sizing tick labels
ax.axis([0, 1100, 0, 1_100_000]) #set range for x and y axis
ax.ticklabel_format(style='plain') #customize tick labels 
plt.show()  #opens the viewer for the plot