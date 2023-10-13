# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:48:56 2023
@author: claes
"""
import math
import numpy as np
'''
Exercise 1. 
Write a function that evaluates the circumference of a circle for an arbitrary 
radius that is an argument of this function. If no argument is given the 
function should compute the case of the radius equal to one. 

Omkretsen av en cirkel ges av: 2*pi*r
'''
def circle_circumreference(r = 1):
    return 2 * math.pi * r



'''
Exercise 2. 
Write a function that evaluates the area of a circle.

Arean av en cirkel ges av: pi*r^2
'''
def circle_area(r):
    return math.pi*r**2


'''
Exercise 3. 
Using the two previously written functions and not using any conditional 
instructions of Python ('if') or other so-called control flows, write a 
function that depending on its arguments computes either the area or the 
circumference of a circle with the default being the area of a circle. 
'''
# def circle_calculator(r, compute_area=True):
#     if compute_area:
#         return circle_area(r)
#     else:
#         return circle_circumreference(r)
    
def circle_calculator(r, berakna_area=True):
    funktioner_berakning = {
        True: circle_area,
        False: circle_circumreference
        }
    berakning = funktioner_berakning[berakna_area]
    return berakning(r)


"""
Exercise 4.
Write a function that compute the volume of a sphere with a given radius. 
Without 'if' instruction write a function that depending on the arguments 
computes one of the three above functions, with the default being the volume 
of a sphere.

Volym av an cylinder (sphere) ges av: pi*r**2*h
"""
def circle_nested_function(r = 1, h = 10, function = 'volume'):
    funktioner = {
        'omkrets': circle_circumreference(r = r),
        'area' : circle_area(r = r),
        'volume': circle_area(r = r)*h
        }
    berakning = funktioner[function]
    
    return berakning



"""
Exercise 5. 
Redo Exercises 3 and 4 using the control flow 'if/else'.
"""
def circle_calculator_v2(r, compute_area=True):
    if compute_area:
        return circle_area(r)
    else:
        return circle_circumreference(r)





"""
Exercise 6. 
Using the loop 'for' approximate the definite integral of the function 
exp(x)+log(x) over the interval (1,2) 
using the Riemman sum approximation with 100 terms. 
Evaluate the upper and lower bounds for the integral. 
Use them to provide the upper bound for the error of the computation.

Beräkning av övre och nedre Riemannsummor ges av:
    Lower (L): L(f,P) = sum_{k=1}^N  m_k \delta x_k
    Upper (U): U(f,P) = sum_{k=1}^N  M_k \delta x_k
    
"""
def riemann_sum_approximation_L(a = 1, b = 2, n = 100):
    
    def f(x):
        return math.exp(x) + math.log(x)
    
    delta_x = (b - a) / n
    integral_approximation_lower = 0.0

    for i in range(n):
        x_start = a + i * delta_x
        x_end = a + (i + 1) * delta_x
        x_min = min(f(x_start), f(x_end))
        integral_approximation_lower += x_min * delta_x

    return integral_approximation_lower

def riemann_sum_approximation_U(a = 1, b = 2, n = 100):
    
    def f(x):
        return math.exp(x) + math.log(x)
    
    delta_x = (b - a) / n
    integral_approximation_upper = 0.0

    for i in range(n):
        x_start = a + i * delta_x
        x_end = a + (i + 1) * delta_x
        x_max = max(f(x_start), f(x_end))
        integral_approximation_upper += x_max * delta_x

    return integral_approximation_upper

# def riemann_approximation(partitions = 100):
#     x = np.linspace(1,2,partitions)    # Här är alltså de x-värden vilka kommer evalueras
#     dx = 1/partitions                  # Då vi har 100 partiotions (staplar) är delta-x 1/100 för varje steg
    
#     sum_area_lower = []
#     for i in x:
#         sum_area_lower.append((np.exp(i)+np.log(i))*dx)
        
#     sum_area_upper = []
#     for i in x:
#         sum_area_upper.append((np.exp(i+1)+np.log(i+1))*dx)
        
#     return sum(sum_area_lower), sum(sum_area_upper)



"""
Exercise 7. 
Use the loop 'while' and the upper bound defined in Exercise 6 
to evaluate the integral until its error is less than 0.0001.

Approximering från wolframalpha: 5.05706863159150

Målet blir således att hitta n för vilket Upper_bound - 5.05706863159150 < epsilon = 0.0001
"""

def riemann_find_n(epsilon = 0.0001, n=1):
    n = n
    epsilon = epsilon
    
    while riemann_sum_approximation_U(n=n) - 5.05706863159150 > epsilon:
        n += 1
        
    return n
    





"""
Exercise 8. 
Use 'break' to stop approximating the integral of the same function 
over (0,1) once the values of log(x) will be smaller than -1. 
"""




"""
Exercise 9. 
For the year 2023, create a list of the length 365 that shows what a weekday 
it is for a given day counted starting from January 1 
(which should be counted as the first day). 
"""
weekday_number = {
    1: 'Måndag',
    2: 'Tisdag',
    3: 'Onsdag',
    4: 'Torsdag',
    5: 'Fredag',
    6: 'Lördag',
    7: 'Söndag'}

