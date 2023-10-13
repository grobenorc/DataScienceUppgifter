# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 08:49:21 2023

@author: xxx
"""
# %% Preamble
import math
import numpy as np
from numpy import linalg
import random
import pandas as pd

# %% Task 12
'''
Exercise 12 (R & Python). Use the modulo operator and list subsampling to program extraction 
of the prime numbers among the first milion integers based on the 
Eratosthenes (250s BCE) algorithm (the sieve algorithm).
'''
def sieve_of_eratosthenes(n=10**6+1):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(1, 10**6+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    primes = [i for i in range(2, n+1) if is_prime[i]]
    return primes


# %% Task 13
'''
Exercise 13. (R & Python) One of the challenging problems in matrix algebra 
is computing an inverse of a matrix, i.e. for a given matrix finding 
the matrix that when two are multiplied then yield the identity matrix. 
Using the tools given in lecture notes, for a given list of 100 non-zero entries, 
define the matrix that has the entries of this list on the diagonal 
and zeros off the diagonal. Find the inverse of such a matrix 
and verify that it is indeed the inverse by using the matrix product.  
'''
def random_integers(count):
    """
    ----------
    count : TYPE
        DESCRIPTION.

    Returns
    -------
    Array
        Return an array of random integers between -10-10 except 0.

    """
    random_integers = []
    len_list = 0

    while len_list<count:
        if random.randint(-10, 10) !=0:
            random_integers.append(random.randint(-10, 10))
            len_list += 1
    
    return np.array(random_integers)


matrix_entries = random_integers(100) # This function is used mainly for the purpose of trying the two next functions.

# define the matrix that has the entries of this array on the diagonal
matrix_entries_diag = np.diag(matrix_entries)

# Find the inverse of that a matrix
def inverse_diagonal_matrix(diagonal_matrix):
  """Computes the inverse of a diagonal matrix.

  Args:
    diagonal_matrix: A diagonal matrix.

  Returns:
    The inverse of the given diagonal matrix.
  """

  inverse_matrix = np.diag(1.0 / diagonal_matrix.diagonal())
  return inverse_matrix

# Example usage should return the identity matrix
matrix_entries_diag@inverse_diagonal_matrix(matrix_entries_diag)



# %% Task 14
'''
Exercise 14. (Python) Investigate the following instructions.
np.dot(x.T*y,x*z) # --> 674
np.dot(x*z,x.T*y) # --> 674
np.dot(y,y.T) # --> 77 
np.dot(y.T,y) # --> 77
Y=np.reshape(y,(1,3)) 
np.dot(Y,Y.T) # --> array([[77]])
np.dot(Y.T,Y) # array([[16, 20, 24],
                       [20, 25, 30],
                       [24, 30, 36]])
    
Does the order in the matrix multiplication matter? 
Are the lists identical to arrays with one column (one row)?
'''
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

x = np.array(x)
y = np.array(y)
z = np.array(z)

np.dot(x.T*y,x*z) # --> 674
np.dot(x*z,x.T*y) # --> 674
np.dot(y,y.T) # --> 77 
np.dot(y.T,y) # --> 77
Y=np.reshape(y,(1,3)) 
np.dot(Y,Y.T) # --> array([[77]])
np.dot(Y.T,Y) # array([[16, 20, 24],
              #        [20, 25, 30],
              #        [24, 30, 36]])

'''
Order does matter if the array is of larger dimension than 1. When we reshape
the y (from 1 dimension) to Y (two dimension) the order does matter. According
to the matrix-multiplication rules the dot product of the matrices then changes.
'''


# %% Task 15
'''
#Exercise 15. (R & Python) Create a simple telephone book with five entries using a dictionary in Python
and names of elements in a vector/list in R. 
#An entry should be recognized by a name and yields a telephone number. 
'''
phone_book = {'Johan Andersson': '0700000001',
              'Johan Pettersson': '0700000002',
              'Johan Svensson': '0700000003',
              'Karin Andersson': '0700000004',
              'Karin Pettersson': '0700000005'}


# %% Task 16
'''
#Exercise 16. (R & Python) Enhance your telephone book by implementing it as a data frame. 
#Add 'first name', 'last name', 'email'  fields.
'''
phone_book_enhanced = {
    'first name': ['Johan', 'Johan', 'Johan', 'Karin', 'Karin'],
    'last name': ['Andersson', 'Pettersson', 'Svensson', 'Andersson', 'Pettersson'],
    'email': ['johan@andersson.com', 'johan@pettersson.com', 'johan@svensson.com', 'karin@andersson.com', 'karin@pettersson.com'],
    'phone number': ['0700000001', '0700000002', '0700000003', '0700000004', '0700000005']
}
phone_book_enhanced_df = pd.DataFrame(phone_book_enhanced)


# %% Task 17
'''
#Exercise 17. 
#(Python, see: lines 10-37 in Lecture_05_P)
#(R, see: lines 70-80 in Lecture_05_R) 
#Write a function that has an array as an argument but no explicit output.
#The elements of this array will be changed (muted) inside the function by adding 
#random numbers and you want the resulting matrix to be used after 
#the function is called. 
'''

def mute_array_in_place(array):
  """Mutes the elements of the given array by adding random numbers.

  Args:
    array: A NumPy array.
  """

  # Generate random numbers for each element of the array.
  random_numbers = np.random.randint(1,15, size=len(array))

  # Add the random numbers to the array.
  array += random_numbers

# Example usage:

array = np.array([1, 2, 3])

# Print the address of the array before muting it.
print(hex(id(array)))
print(array)

# Mute the array.
mute_array_in_place(array)

# Print the address of the array after muting it.
print(hex(id(array)))
print(array)


# %% Task 18
'''
#Exercise 18. (R & Python) Implement all standard arithmetic operations (subtraction, multiplication, and division) within the class of complex numbers. 
'''

# Define a class for complex numbers
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Method for addition
    def add(self, other):
        real_result = self.real + other.real
        imag_result = self.imaginary + other.imaginary
        return ComplexNumber(real_result, imag_result)

    # Method for subtraction
    def subtract(self, other):
        real_result = self.real - other.real
        imag_result = self.imaginary - other.imaginary
        return ComplexNumber(real_result, imag_result)

    # Method for multiplication
    def multiply(self, other):
        real_result = self.real * other.real - self.imaginary * other.imaginary
        imag_result = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_result, imag_result)

    # Method for division
    def divide(self, other):
        denominator = other.real**2 + other.imaginary**2
        real_result = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag_result = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_result, imag_result)
    
# Exempel
z1 = ComplexNumber(3, 4)
z2 = ComplexNumber(1, 2)



# %% Task 19

# %%% Part 1
'''
#=================
#Exercise 19. (Python) Explain different level of the accessibilities in the code below. 
#Comment on possible reasons a programer may have for a particular restriction of the accessibility. 
#Part 1: defining a class Employee
class Employee:
    # constructor
    def __init__(self, name, sal):
        self.name = name;
        self.sal = sal;


JS=Employee('John Smith',3000)
JS.name
JS.sal

JS.name='JS'
JS.sal='3000$'
'''
class Employee:
    # constructor
    def __init__(self, name, sal):
        self.name = name;
        self.sal = sal;


JS=Employee('John Smith',3000)
JS.name
JS.sal

JS.name='JS'
JS.sal='3000$'

'''
Comment:
    The class Employee contains of two instances; name and salary which are both declared as public.
    Being declared as public is done for easy access, both inside as well as outside the class meaning 
    you can acces methods and instances from outside of the class.
'''

# %%% Part 2
'''
#Part 2: defining a class Employee
class Employee:
    # constructor
    def __init__(self, name, sal):
        self._name = name;   # protected attribute 
        self._sal = sal;     # protected attribute
   

        

JS=Employee('John Smith',3000)
JS._name
JS._sal

#This can be useful when there is a child class extending the class Employee. Then it can also access the protected member variables of the class Employee. Consider

# defining a child class
class HR(Employee):# member function task
	def task(self):
		print("We manage Employees")
		print(self._name)
		print(self._sal)
        

#Demonstrate that one can access protected member variable of class Employee from the class HR.

result=HR('John',3000)
result._name
result._sal
result.task()

result._name='Jane'
result._sal=1000
result.task()
#We manage Employees
#Jane
#1000


#Actually 'restricted' access is a fake concept in Python, as the access is not restricted in any sense (C-langauge provides a true accessibility restrictions)
#For private attributes and methods there are some messages that mimics restrictions (but they can be overide, so they are not real either)
'''
'''
Comment:
    Here we can se that the instances of the class HR is protected due to having _instance in the class Employee.
    This gives access only within the function or a subclass meaning it can not be directly accessed outside of the class, in comparison with the public class.
'''

# %%% Part 3
'''
# Part3: defining class Employee
class Employee:
    def __init__(self, name, sal):
        self.__name = name;    # private attribute 
        self.__sal = sal;      # private attribute
        
        
# defining a child class
class HR(Employee):# member function task
	def task(self):
		print("We manage Employees")
		print(self.__name)
		print(self.__sal)
        

#Demonstrate that one cannot access private member variable of class Employee from the class HR.

result=HR('John',3000)
result.__name
result.__sal
result.task()

#Python performs name mangling of private variables to pretend restricted access. Every member with a double underscore will be changed to _object._class__variable. So, it can still be accessed from outside the class, but the practice should be refrained.


result._Employee__name

#=================
'''
'''
Comment: 
    Lastly this class is private which means that the instances and methods are only accessed within the class. And instance or method can therefor not be accessed
    from any other subclass or outside of the class. This is the most 'protected' accessibility.
    When trying to access the attribute from the subclass will now throw an error, due to the attribute not being within the Sub class.
'''


'''
Comment:
    Overall the different accessibility methods are used to protect, or not protect, attributes, instances and methods being being applied/used/initiated/changed.
    It gives the programmer the choice of preventing failures 
'''