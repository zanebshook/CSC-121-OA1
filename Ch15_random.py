from random import choice #import choice function from random module
class RandomWalk: #create class for our random walk
    def __init__(self, num_points=5000):  #sets number of points to 5000 
        self.num_points = num_points
        self.x_values = [0]  #create lists for x and y values 
        self.y_values = [0]  #first point will be 0,0
    def fill_walk(self):
        #while there are less than 5000 values in the self.x_values list:
        while len(self.x_values) < self.num_points:
            #x value can either go up or down, distance can be  from 0 to 4
            x_direction = choice([1, -1])  
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance #step distance in x direction
            #y value can either go up or down, distance can be  from 0 to 4
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance #step distance in y direction
            if x_step == 0 and y_step == 0: #reject moves that go nowhere
                continue
            #if the step has no distance generate a new step:
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            #add this new step to the lists 
            self.x_values.append(x) 
            self.y_values.append(y)