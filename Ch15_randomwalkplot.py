import matplotlib.pyplot as plt
from Ch15_random import RandomWalk
while True: #while loop to keep making new walks
    rw = RandomWalk(50_000)  #create a variable for the RandomWalk class
    rw.fill_walk()  #call the fill_walk method to generate points for the walk
    plt.style.use('classic')  
    fix, ax = plt.subplots(figsize=(15, 9))  #set size of the plotting window
    #create a variable for the 'c argument' as a range equal to number of steps
    point_numbers = range(rw.num_points)
    #put this range into the c argument, select blue color map, no edge colors
    ax.scatter(
        rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=1)  
    ax.set_aspect('equal')
    #emphasize first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(
        rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #removing axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break