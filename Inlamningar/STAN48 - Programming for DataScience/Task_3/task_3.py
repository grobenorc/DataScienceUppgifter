# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:20:58 2023

@author: claes
"""

import os
import inspect
import time
import numpy as np
os.chdir('C:/Users/claes/OneDrive/Universitet/DataScience Magisterprogram/STAN48 - Programmering för Data Science/Inlämningar/Task_3')


# %% Exercise 20 
'''
#Exercise 20 (R & Python Lecture_6)
#One can use the command line to uppload a function. 
#For example, %run / source (Python/R) print_triangle would upload the function 
#defined above (see Lecture notes) if it is saved in a separate script with the name print_triangle.py / print_triangle.R (Python/R) . 
#Please, create such a script and run this script to upload the function defined in it. 
#Then invoke the function with several different values of the input.
'''
# Det här är ett eget script.
# def print_triangle(n):
#     for i in range(n+1):
#         print("∗"*i) 
        
# print_triangle(5)

runfile('print_triangle.py') # This demands the working directory being in the same folder as the script 'print_triangle.py'

# %% Exercise 21
'''
#Exercise 21 (Python Lecture_6)
#Create a script only with the function find_pos (see Lecture notes) saved in a separate 
#script that has the same name as the function. 
#Run this script to upload the definition. 
#Then invoke the function with several different values of 
#the input list of different lengths. Consider both real and integer numbers 
#in the input list.
'''
#======================    
# def find_pos(v,x):
#     for i in range(len(v)):
#         if v[i]>=x: return i

# v=[1,2,5,10]
# print(find_pos(v,-1))
# print(find_pos(v,4))
# print(find_pos(v,11))
#======================
# %run find_pos.py gives error-message
runfile('find_pos.py') # Same as earlier requires the working directory to be the folder as the script
print(find_pos(range(100),-1))
print(find_pos(range(100),4))
print(find_pos(range(1000),986))
print(find_pos(np.linspace(0, 100, 1000), 25.67))
print(find_pos(np.linspace(0, 100, 1000), 100))


# %% Exercise 22
'''
#Exercise 22 (Python Lecture_6)
#Modify the function find_pos so that it takes either list or 1-D
# array as the first argument, yields a tuple of two elements 
#(L,L+1) if the second argument x of the function 
#satisfies v[L]<=x<v[L+1], or ('-Inf',0) if x is smaller than 
#all elements in the first argument v, or (len(v),'Inf') 
#if x is larger than all elements in the list v. 
#Additionally to the index range, the function should also return 
#the corresponding value range.
'''
def find_pos_mod(v, x):
    try:
        # Check if 'v' is a 1-D NumPy array or a list
        if not ((isinstance(v, np.ndarray) and v.ndim == 1) or isinstance(v, list)):
            raise Exception('Parameter v must be a 1-D NumPy array or a list')
        
        # Initialize variables to store the index and value range
        index_range = None
        value_range = None
        
        # Loop through the elements of 'v'
        for i in range(len(v)):
            # Check if 'x' is greater than or equal to the current element
            if x >= v[i]:
                if i == len(v) - 1:
                    # 'x' is greater than or equal to the last element
                    index_range = (i, i + 1)
                    value_range = (v[i], float('inf'))
                else:
                    # 'x' is within the range of the current and next element
                    if x < v[i + 1]:
                        index_range = (i, i + 1)
                        value_range = (v[i], v[i + 1])
            else:
                if i == 0:
                    # 'x' is smaller than the first element
                    index_range = (float('-inf'), 0)
                    value_range = (float('-inf'), v[0])

        # If 'index_range' and 'value_range' are still None, 'x' falls outside the range
        if index_range is None or value_range is None:
            # 'x' is greater than the last element
            index_range = (len(v), float('inf'))
            value_range = (v[-1], float('inf'))
        
        return index_range, value_range
    
    except Exception as e:
        print(e)
   


# %% Exercise 23
'''
#Exercise 23 (Python Lecture_6)
#Run your program for an input array of 10000000 integers
(if the value is too large, reduce it so that the calculations take place in a reasonable time) 
# and compare it to running it on an array of float values of the same size. 
#Is there any noticable difference in the time the two algorithm are running?
'''
def runtime_program(v,x):
    import time
    start = time.time()
    find_pos_mod(v=v, x=x)
    end = time.time()
    run_time = end-start
    number_type = 'Integer' if all(isinstance(x, (int)) for x in v) else 'Float'
    print(f'Runtime for the function of {number_type}: {run_time:.10f} seconds')


runtime_program(np.linspace(0,100, 10000000), 50)
runtime_program(list(range(10000000)), 5000000)
# runtime_program(np.arange(0,10000000), 5000000)

# Here I use the values the x values to be 50 and 5 000 000 in order for the indexes to be same, 
# i.e. the loop to iterate equal amount of times. 
# We can see that the looping is significantly faster when looping through a list of integers compared to floats.


# %% Exercise 24
'''
#Exercise 24 (Python Lecture_6)
#Modify the function binary_search (see Lecture notes) so that it takes either list or 1-D array 
#as the first argument, yields a tuple of two elements (L,L+1) if the second 
#argument x of the function satisfies v[L]<=x<v[L+1], or ('-Inf',0) if x is 
#smaller than all elements in the first argument v, or (len(v),'Inf') if x is 
#larger than all elements in the list v. Additionally to the index range, 
#the function should also return the corresponding value range. 
#Run this function using the same inputs as in Exercise 23. 
#Are there any observable benefits of the new algorithm, 
#when compared with the previous one?
'''
def binary_search(v, x):
    try:
        if not ((isinstance(v, np.ndarray) and v.ndim == 1) or isinstance(v, list)):
            raise Exception('Parameter v must be a 1-D NumPy array or a list')

        if v[-1] < x:
            return ((len(v), float('inf')), (v[-1], float('inf')))
        elif v[0] > x:
            return ((float('-inf'), 0), (float('-inf'), v[0]))
        else:
            start, end = 0, len(v) - 1
            while start <= end:
                mid = (start + end) // 2
                if v[mid] == x:
                    return ((mid, mid + 1), (v[mid], v[mid + 1]))
                elif v[mid] > x:
                    end = mid - 1
                else:
                    start = mid + 1
            return ((end, start), (v[end], v[start]))
    except Exception as e:
        print(e)

def runtime_program2(v,x):
    import time
    start = time.time()
    binary_search(v=v, x=x)
    end = time.time()
    run_time = end-start
    number_type = 'Integer' if all(isinstance(x, (int)) for x in v) else 'Float'
    print(f'Runtime for the function of {number_type}: {run_time:.16f} seconds')


runtime_program2(np.linspace(0,100, 10000000), 50)
runtime_program2(list(range(10000000)), 5000000)

# There is a big difference in the running time of the two different algorithms. One (the earlier function ) is significantly slower.


# %% Exercise 25
'''
#Exercise 25 (Python & R Lecture_6)
#Benchmark both Python and R-version of the programs find_pos and binary_search (see Lecture notes).
#Are there significant differences between the performances on these two platforms.
'''







# %% Exercise 26
'''
# Exercise 26. (Python Lecture_7; BML model)
# The following is Python implementation of Biham–Middleton–Levine (BML) traffic model
# see the textbook for more details about the model
'''
import numpy as np
import matplotlib.pyplot as plt

class BML:
    def __init__(self, alpha, m, n):
        self.alpha = alpha
        self.shape = (m, n)
        self.initialize_lattice()

    def initialize_lattice(self):
        u = np.random.uniform(0.0, 1.0, self.shape)
        # instead of using default list, we use np.array to create the lattice
        self.lattice = np.zeros_like(u, dtype=int)
        # the parentheses below can’t be ignored
        self.lattice[(u > self.alpha) & (u <= (1.0 + self.alpha) / 2.0)] = 1
        self.lattice[u > (self.alpha + 1.0) / 2.0] = 2
        
        # Shape av storlek MxN som skapar ett gitter / grid / schackbräd
        # Slumptal genereras med uniform fördelning
        # Alpha bestämmer intervallet för vilka värden som ska tilldelas. Då det i vårt fall är 0.4 innebär att:
            # uniform slumptal: 0-0.4 ger en nolla på grid, 0.4-0.7 ger 1 på gitter, >0.7 ger en 2
            
        # Gitter / grid / schackbräda 'korrigeras' med värdena 0,1,2 baserat på slumptalen enligt ovan beskrivet.
        
        
    def odd_step(self):
        # please note that np.where returns a tuple which is immutable
        blue_index = np.where(self.lattice == 1)
        blue_index_i = blue_index[0] - 1
        blue_index_i[blue_index_i < 0] = self.shape[0] - 1
        blue_movable = self.lattice[(blue_index_i, blue_index[1])] == 0
        self.lattice[(blue_index_i[blue_movable],
                      blue_index[1][blue_movable])] = 1
        self.lattice[(blue_index[0][blue_movable],
                      blue_index[1][blue_movable])] = 0
        
        # Vi tar här ut index för vilka positioner som har ett värde om 1 (alltså det tilldelade värdet efter slumptalsgenereringen.)
        

    def even_step(self):
        red_index = np.where(self.lattice == 2)
        red_index_j = red_index[1] + 1
        red_index_j[red_index_j == self.shape[1]] = 0
        red_movable = self.lattice[(red_index[0], red_index_j)] == 0
        self.lattice[(red_index[0][red_movable],
                      red_index_j[red_movable])] = 2
        self.lattice[(red_index[0][red_movable],
                      red_index[1][red_movable])] = 0


    def plot_lattice(self):
        # Define colors for visualization
        colors = {0: 'white', 1: 'blue', 2: 'red'}
        
        # Create a figure and axis for the plot
        fig, ax = plt.subplots()
        
        # Create a grid of squares based on the lattice values
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                square_color = colors[self.lattice[i, j]]
                ax.add_patch(plt.Rectangle((j, i), 1, 1, color=square_color, edgecolor='black'))
        
        # Set axis limits and labels
        ax.set_xlim(0, self.shape[1])
        ax.set_ylim(0, self.shape[0])
        ax.set_aspect('equal')
        ax.set_xticks(range(self.shape[1] + 1))  # +1 to include the last column
        ax.set_yticks(range(self.shape[0] + 1))  # +1 to include the last row
        ax.grid(which='both')
        
        # Show the plot
        plt.show()   

#run the previous code in the console, and create a Class 'BML'

bml = BML(0.4, 5, 5)
bml.lattice
#Execute the above commands two times and check whether the returned arrays differ.

# The arrays are not the same.

np.random.seed(2022)
bml = BML(0.4, 5, 5)
bml.lattice
#Execute the above commands two times and check whether the returned arrays differ.
#You should get the same matrix. Explain the impact of the "np.random.seed(2022)".

# When seeting the random seed we decide, in advance, the sampling algorithm. 
# This means the sampling algorithms are the same both times we run the lines which 
# is not the case in the lines above when not setting the random seed. This is 
# useful for reproducibility in order to get the same results every time, no 
# matter who/which computer is running the code. More specifically random seed 
# is determining the sampling algorithm in the np.random.uniform(0.0, 1.0, self.shape)
# defined in the class. 



# %% Exercise 27
'''
# Exercise 27. (Python Lecture_7; BML model) Execute commands below.

np.random.seed(2022)
bml = BML(0.4, 5, 5)
bml.lattice
bml.odd_step()
bml.lattice
bml.even_step()
bml.lattice

#Explain the impact of the bml.odd_step() and bml.even_step().
'''
np.random.seed(2022)
bml = BML(0.4, 5, 5)
bml.lattice
bml.odd_step()
bml.lattice
bml.even_step()
bml.lattice

# For us to be able to understand what the methods/instances are doing we 
# have to inspect the class defined in the above exercise (26). The odd-step and even-step are functioning like a coordinate plane.
# The coordinate plane is filled with 0,1,2 where 1 represents blue index and 2 represents red index. The blue and red oordinates moves over the whole coordinate plane
# in opposite directions (90 degree angle). The functions / methods instances checks wether there is a color (blue or red, meaning opposite colour) in the directions it wants to move.
# If there isn't a color in the next forward coordinate on the plane it can move forwards. This is represented by the:
    # blue_movable and red_movable within the class that is represented of a boolean value. It can move in the direction if true but cannot move forwards if false.

# As soon as there is an empty with no color in the direction it wants move, the color_movable boolean operator will be true and it will move to that positition.

# All in all, this can be seen something similar to a traffic light, when green light it moves represented by true, and if the red light is red (represented by false) it has to wait for it the light to be green.


# %% Exercise 28
'''
#Exercise 28. (Python Lecture_7; BML model) Experiment with the parameter 'alpha' 
and based on your experiments clarify what does it control.
'''
# As commented above, within the class, alpha decides of which values, generated by the uniform distribution, should be assigned the different colours. 
# It practically decides the different threshholds for the different colours. A higher alpha value gives a lower probability of assigning one or two in the initial lattice / gitter. 
# Meaning a low alpha value will assign many more colours meaning harder to move/a lot more cars with the traffic analogy. It will the be harder for 
# the colours to move because the probability of having a colour in the direction it wants to move is higher.


# Add the following instance to the original class to be able to plot it #
##########################################################################
    # def plot_lattice(self):
    #     # Define colors for visualization
    #     colors = {0: 'white', 1: 'blue', 2: 'red'}
        
    #     # Create a figure and axis for the plot
    #     fig, ax = plt.subplots()
        
    #     # Create a grid of squares based on the lattice values
    #     for i in range(self.shape[0]):
    #         for j in range(self.shape[1]):
    #             square_color = colors[self.lattice[i, j]]
    #             ax.add_patch(plt.Rectangle((j, -i - 1), 1, 1, color=square_color, edgecolor='black'))
        
    #     # Set axis limits and labels
    #     ax.set_xlim(0, self.shape[1])
    #     ax.set_ylim(-self.shape[0], 0)
    #     ax.set_aspect('equal')
    #     ax.set_xticks(range(self.shape[1]))
    #     ax.set_yticks(range(-self.shape[0], 0))
    #     ax.grid(which='both')
        
    #     # Show the plot
    #     plt.show()

##########################################################################

np.random.seed(2022)
bml = BML(0.4, 5, 5)
bml.lattice



bml = BML(0.2, 5, 5)
bml.plot_lattice()

bml = BML(0.3, 5, 5)
bml.plot_lattice()

bml = BML(0.4, 5, 5)
bml.plot_lattice()

# Here we can see that the alpha value determines how many 'coloured boxes' there will be. 
# Continuing on the traffic analogy alpha determines how much traffic there  is.

# Below code is made in order to get a better understanding of the steps that are done.
# Down below is made of two different cases, one where the grid is 5x5, and one with a 10x10 grid. 
# For each of these there are different alpha values.
# Notice that if wemany iterations the algorithm seems to reach a state where the boxes can no longer move in any direction.


def simulate_and_visualize(bml, num_steps):
    import time
    for step in range(num_steps):
        # Perform the odd step and visualize
        bml.odd_step()
        bml.plot_lattice()
        time.sleep(0.03)
        print(f"Iteration: {step+1}")
        # Perform the even step and visualize
        bml.even_step()
        bml.plot_lattice()
        time.sleep(0.03)
        print(f"Iteration: {step+1}")

# simulate_and_visualize(BML(0.2, 5,5), 20)
# simulate_and_visualize(BML(0.3, 5,5), 20)
# simulate_and_visualize(BML(0.4, 5,5), 20)

# simulate_and_visualize(BML(0.2, 10,10), 20)
# simulate_and_visualize(BML(0.3, 10,10), 20)
# simulate_and_visualize(BML(0.4, 10,10), 50)


simulate_and_visualize(BML(0.6, 40,40), 500)


# %% Exercise 30
'''
#Exercise 30. (Python Lecture_7) Summarize in two three sentences what are the 
# differences between 'laziness' and 'eagerness' of languages
# and reflect when one can prefer one over the other.
'''
# Laziness and eagerness are two different concepts/methods for programming languages. It is describing wether an 
# algorithm/calculation is computed as soon as it is encountered in a code-line chunk, or wait until the computed value is needed. 
# Eeagerness means it is computing the value as soon as it is encountered, even though it is not needed at that point in time,
# Laziness on the other hand computes the value only when the computaion is needed in order to compute the 'next calculation' based on that value. 
# Python embraces the eagerness approach.
