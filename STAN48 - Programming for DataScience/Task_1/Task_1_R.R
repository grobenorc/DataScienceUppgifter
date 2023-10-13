# -------------------------------------
# Script: 

# Author: Claes Croneborg

# Ämne: 

# Beskrivning:

# License: MIT

# Encoding: UTF-8-SV
Sys.setlocale("LC_ALL", "sv_SE.UTF-8")

# Paket:
require(tidyverse)
require(readxl)
require(ggthemes)

# Paket andra


# Working directory
setdw("---")


# @param
#

# ====================================================================
# @return
#


# -------------------------------------

# Exercise 1. ====
# Write a function that evaluates the circumference of a circle for 
# an arbitrary radius that is an argument of this function. If no argument is 
# given the function should compute the case of the radius equal to one. 

circle_circumreference <- function(r=1) {
  return(2*pi*r)
}


# Exercise 2. ====
# Write a function that evaluates the area of a circle.
circle_area <- function(r=1) {
  return(pi*r**2)
}


# Exercise 3. ====
# Using the two previously written functions and not using any 
# conditional instructions of Python ('if') or other so-called control flows, 
# write a function that depending on its arguments computes either the area or 
# the circumference of a circle with the default being the area of a circle. 

circle_calculator1 <- function(funktion='area', r = 1) {
  funktioner = list(
    omkrets = circle_circumreference,
    area = circle_area
  )
  berakning = funktioner[[funktion]](r)
  
  return(berakning)
}


# Exercise 4. ====
# Write a function that compute the volume of a sphere with a given radius. 
# Without 'if' instruction write a function that depending on the arguments 
# computes one of the three above functions, with the default being the volume 
# of a sphere.  

circle_calculator2 <- function(funktion='volym', r = 1) {
  volume_sphere <- function(r=r) {
    return((4*pi*r**3)/3)
  }
  
  funktioner = list(
    omkrets = circle_circumreference,
    area = circle_area,
    volym = volume_sphere
  )
  berakning = funktioner[[funktion]](r)
  
  return(berakning)
}

# Exercise 5. ====
# Redo Exercises 3 and 4 using the control flow 'if/else'.
circle_calculator2_V2 <- function(funktion='volym', r=1) {
  if (funktion=='omkrets') {
    circle_circumreference(r=r)
  } else if (funktion=='area'){
    circle_area(r=r)
  } else {
    return((4*pi*r**3)/3)
  }
}


# Exercise 6. ====
# Using the loop 'for' approximate the definite integral of the 
# function exp(x)+log(x) over the interval (1,2) using the Riemman sum 
# approximation with 100 terms. Evaluate the upper and lower bounds for 
# the integral. Use them to provide the upper bound for the error 
# of the computation.

f <- function(x) {
  return(log(x) + exp(x))
}

partitions=100
x=seq(1,2,length.out=partitions)
delta_x=(max(x)-min(x))/(partitions-1)


# Initiera Upper Riemann Sum
URS <- 0
# Calculate the Upper Riemann Sum
for (i in 1:partitions) {
  URS <- URS + (min(x)/partitions) * f(min(x) + (i/partitions))
}
print(URS)

# Initiera Lower Riemann Sum
LRS <- 0
# Beräkna Lower Riemann Sum
for (i in 0:(partitions-1)) {
  LRS <- LRS + (min(x)/partitions) * f(min(x) + (i/partitions))
}
print(LRS)


# Exercise 7. ====
# Exercise 7. Use the loop 'while' and the upper bound defined in Exercise 6 to 
# evaluate the integral until its error is less than 0.0001.


# 1/n <= |f(a)-f(b)|
f <- function(x) {
  return(log(x) + exp(x))
}


# Initiera n till 1
n<-1
a<-1
b<-2
# Bestäm vilket värde på error du vill ha
error<-0.0001

while ( (1/n*abs(f(a)-f(b))) > error) {
  n = n+1
}

print(n)

# Exercise 8. ====
# Use 'break' to stop approximating the integral of the same function over (0,1) 
# once the values of log(x) will be smaller than -1. 

f <- function(x) {
  return(log(x) + exp(x))
}

# Intiera en ny Riemann-summa för den nya beräkningen
RS_2 = 0
for (i in rev(seq(0,1,length.out=partitions))) {
  if ( log(i) < -1 ){
    break
  }
  RS_2 = RS_2 + f(i)*delta_x
}



# Exercise 9 ====


# Define a vector of weekdays
weekdays <- c("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# Define the year and starting date
year <- 2023
start_day_index <- 1  # January 1, 2023, is a Sunday

# Create a list of weekdays for the year 2023
weekday_list <- character(365)

# Initialize a variable to keep track of the current day index
current_day_index <- start_day_index

# Iterate through the days of the year and populate the weekday list
for (i in 1:365) {
  weekday_list[i] <- weekdays[current_day_index]
  # Update current_day_index for the next day
  if (current_day_index == 7) {
    current_day_index <- 1  # Start over from Sunday
  } else {
    current_day_index <- current_day_index + 1
  }
}

# Print the weekday list
print(weekday_list)


# Exercise 10 ====
# Can't be done in R.

# Because it can't e done there is no difference.
