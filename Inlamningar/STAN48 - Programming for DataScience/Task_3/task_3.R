############################################################################################################################################
# Preamble
# Make sure working directory as well as all the scripts:
  # 1. print_triangle.R
  # 2. find_pos.R
  # 3. Fibonacci.R
  # 4. Fibonacci.cpp
  # are stored in the same folder as the working directory

setwd('C:/Users/claes/OneDrive/Universitet/DataScience Magisterprogram/STAN48 - Programmering för Data Science/Inlämningar/Task_3')


# Task 20 ===========================================================================================================================================
#########################################################################################
# Exercise 20 (R & Python Lecture_6)
# One can use the command line to uppload a function. 
# For example, %run / source (Python/R) print_triangle would upload the function 
# defined above (see Lecture notes) if it is saved in a separate script with the name print_triangle.py / print_triangle.R (Python/R) . 
# Please, create such a script and run this script to upload the function defined in it. 
# Then invoke the function with several different values of the input.
#########################################################################################

source('print_triangle.R') # Make sure script-file is in the folder as the working directory.

# Task 21 ===========================================================================================================================================
#########################################################################################
# Exercise 21 (Python Lecture_6)
# Create a script only with the function find_pos (see Lecture notes) saved in a separate 
# script that has the same name as the function. 
# Run this script to upload the definition. 
# Then invoke the function with several different values of 
# the input list of different lengths. Consider both real and integer numbers 
# in the input list.
#########################################################################################
#================================
# find_pos=function(v,x){
#   for (i in 1:length(v)){
#     if (v[i]>=x){
#       return(i)
#     }
#   }
# }
# 
# v=c(1,2,5,10)
# print(find_pos(v,-1))
# print(find_pos(v,4))
# print(find_pos(v,11))
#================================
source('find_pos.R')
print(find_pos(seq(100),-1))
print(find_pos(seq(100),8))
print(find_pos(seq(1000),986))
print(find_pos(seq(0, 100, length.out = 100), 25.67))
print(find_pos(seq(0, 100, length.out = 1000), 98.6))


# Task 22 ===========================================================================================================================================
#########################################################################################
# Exercise 22 (Python Lecture_6)
# Modify the function find_pos so that it takes either list or 1-D
# array as the first argument, yields a tuple of two elements 
# (L,L+1) if the second argument x of the function 
# satisfies v[L]<=x<v[L+1], or ('-Inf',0) if x is smaller than 
# all elements in the first argument v, or (len(v),'Inf') 
# if x is larger than all elements in the list v. 
# Additionally to the index range, the function should also return 
# the corresponding value range.
#########################################################################################

# One dimensional array in R will only return the legnth of the array meaning we can check that it a one-dimensional array by looking at the length of the dimensions. 
# length(dim(array)) == 1 if one-dimensional, length(array) != 1d otherwise
# Define a function that finds the index and value range for a given value, x, within a 1-dimensional array or vector
find_pos_mod <- function(variable, x) {
  # Check if the input 'variable' is a valid 1-dimensional array or vector
  if (!(is.vector(variable) || (is.array(variable) && length(dim(variable)) == 1) || (is.list(variable) && length(variable) > 0))) {
    stop("Parameter must be a 1-dimensional array or vector")
  }
  
  # Initialize variables to store the index and value range
  index_range <- NULL
  value_range <- NULL
  
  # Loop through the elements of the 'variable'
  for (i in 1:(length(variable) - 1)) {
    # Check if 'x' is within the range of the current element and the next element
    if (x >= variable[i] && x <= variable[i + 1]) {
      # Set the index range and value range
      index_range <- c(i, i + 1)
      value_range <- c(variable[i], variable[i + 1])
      break  # Exit the loop once a match is found
    }
  }
  
  # If 'index_range' and 'value_range' are still NULL, it means 'x' falls outside the range
  if (is.null(index_range) || is.null(value_range)) {
    # Check if 'x' is less than or equal to the first element
    if (x <= variable[1]) {
      index_range <- c(-Inf, 1)
      value_range <- c(-Inf, variable[1])
    } else if (x >= variable[length(variable)]) {  # Check if 'x' is greater than or equal to the last element
      index_range <- c(length(variable), Inf)
      value_range <- c(variable[length(variable)], Inf)
    }
  }
  
  # Return the calculated 'index_range' and 'value_range' as a list
  return(list(index_range = index_range, value_range = value_range))
}





# Task 23 ===========================================================================================================================================
#########################################################################################
# Exercise 23 (Python Lecture_6)
# Run your program for an input array of 10000000 integers
# (if the value is too large, reduce it so that the calculations take place in a reasonable time) 
# and compare it to running it on an array of float values of the same size. 
# Is there any noticable difference in the time the two algorithm are running?
#########################################################################################
runtime_program <- function(v, x) {
  start_time <- Sys.time()
  find_pos_mod(variable = v, x = x)
  end_time <- Sys.time()
  elapsed_time <- end_time - start_time
  cat("Elapsed time:", elapsed_time, "seconds. \n")
  cat("When run with", length(v), "numbers of type", typeof(v), ".\n")
}
runtime_program(seq(10000000), 5000000)
runtime_program(seq(0,100, length.out = 10000000), 50)

runtime_program(seq(10000000), 8000000)
runtime_program(seq(0,100, length.out = 10000000), 80)

# Running the program with integers seems to be marginally faster.



# Task 24 ===========================================================================================================================================
#########################################################################################
# Exercise 24 and 25 (R Lecture_6)
# is the same as in Python's version, except that first you need 
# to correct the code of the binary search in the same
# manner as in Python's version of the program.
#########################################################################################
# Define a function that performs a binary search to find the index and value range for a given value, x, within a 1-dimensional array or vector
binary_search <- function(v, x) {
  # Check if the input 'v' is a valid 1-dimensional array or vector
  if (!(is.vector(v) || (is.array(v) && length(dim(v)) == 1) || (is.list(v) && length(v) > 0))) {
    stop("Parameter must be a 1-dimensional array or vector")
  }
  
  # Check if 'x' is greater than the last element in the vector
  if (v[length(v)] < x) {
    index_range <- c(length(v), Inf)
    value_range <- c(v[length(v)], Inf)
    return(list(index_range = index_range, value_range = value_range))
  }
  # Check if 'x' is smaller than the first element in the vector
  else if (v[1] > x) {
    index_range <- c(-Inf, 1)
    value_range <- c(-Inf, v[1])
    return(list(index_range = index_range, value_range = value_range))
  }
  # If 'x' is within the vector, perform a binary search
  else {
    start <- 1
    end <- length(v)
    
    while (start <= end) {
      mid <- (start + end) %/% 2
      if (v[mid] == x) {
        index_range <- c(mid, mid + 1)
        value_range <- c(v[mid], ifelse(mid == length(v), Inf, v[mid + 1]))
        return(list(index_range = index_range, value_range = value_range))
      }
      # If 'x' is smaller than the middle element, update 'end'
      else if (v[mid] > x) {
        end <- mid - 1
      }
      # If 'x' is larger than the middle element, update 'start'
      else {
        start <- mid + 1
      }
    }
    
    # If 'x' was not found in the vector, return the range where it should be inserted
    if (start > 1) {
      index_range <- c(start - 1, start)
      value_range <- c(v[start - 1], ifelse(start == length(v) + 1, Inf, v[start]))
    } else {
      # If 'start' is 1, then 'x' should be inserted before the first element
      index_range <- c(-Inf, 1)
      value_range <- c(-Inf, v[1])
    }
    return(list(index_range = index_range, value_range = value_range))
  }
}





# Task 26 ===========================================================================================================================================
#########################################################################################
# Exercise 26
# Run your program for an input array of 10000000 integers
# (if the value is too large, reduce it so that the calculations take place in a reasonable time) 
# and compare it to running it on an array of float values of the same size. 
# Is there any noticable difference in the time the two algorithm are running?
#########################################################################################
runtime_program2 <- function(v, x) {
  start_time <- Sys.time()
  binary_search(v=v, x=x)
  end_time <- Sys.time()
  elapsed_time <- end_time - start_time
  cat("Elapsed time:", elapsed_time, "seconds. \n")
  cat("When run with", length(v), "numbers of type", typeof(v), ".\n")
}
runtime_program2(seq(10000000), 5000000)
runtime_program2(seq(0,100, length.out = 10000000), 50)

# There is a noticable difference between the two algorithms. Binary search is significantly faster than previous code. In fact it is about 10 times faster (it varies a little bit from time to time, and also at which index the x lies. Binary search is not as dependent on the index as the previous algorithm because of the architecture of finding the position (diving the 'search window' in two each time.)


# Task 29 ===========================================================================================================================================
#########################################################################################
#Exercise 29. (R Lecture 7) Use 'detectCores()' to find out how many processors are available on your computer. 
#Report the outcome (my had 10). Rewrite the above code (see Lecture notes) to compute the integral discussed in Exercise 6. 
#Discuss the accuracy and the speed of the method of Riemann sums with the Monte Carlo one. 
library(parallel)
number_cores <- detectCores()
# My computer has 8 cores.

#Necessary modules for evaluatingtheperformance.
require(parallel)
require(microbenchmark)


# The function we want to intergrate. (The same as previous lab done in exercise 6).
f <- function(x) {
  return(log(x) + exp(x))
}

monte_carlo_integration <- function(n) {
  x_values <- runif(n, 1, 2)  # Uniformly sample points from [1,2]
  x_eval <- sapply(x_values, f)  # Compute f(x) for each sampled x
  integral_approximation <- (2-1) * mean(x_eval)  # Average and multiply by interval length
  return(integral_approximation)
}


# Parallelized Monte Carlo integration method
monte_carlo_parallel <- function(n) {
  require(purrr)
  num_cores <- detectCores() - 1
  num_simulations_per_core <- n %/% num_cores
  
  # Initiate a cluster of workers.
  cl <- makeCluster(num_cores)
  
  # Pass functions and variables to the seperate workers.
  clusterExport(cl, c("monte_carlo_integration", "f"))
  
  # Use parLapply to compute monte_carlo_integration in parallel.
  results <- parLapply(cl, rep(num_simulations_per_core, num_cores), function(each_n) {
    # Run monte_carlo_integration and return the result
    result <- monte_carlo_integration(each_n)
    return(result)
  })
  
  # Stop cluster.
  stopCluster(cl)
  
  # Compute means of each simulation.
  mean_results <- map_vec(results, mean)
  
  return(mean(mean_results))
}

# Compare the methods using a larger n for better accuracy
n <- 1e6  # Number of samples/simulations

print(paste("Monte Carlo method:", monte_carlo_integration(n)))
print(paste("Parallel Monte Carlo method:", monte_carlo_parallel(n)))
print(paste("The difference in computing-time between the two:", abs(monte_carlo_integration(n) - monte_carlo_parallel(n))))

# Comparison in speed using microbenchmark
# Measure execution-time for the Monte Carlo method with no parallel.
monte_carlo_time <- microbenchmark(
  ordinary = monte_carlo_integration(n),
  times = 100  
)

# Measure execution-time for the parallel Monte Carlo computation.
monte_carlo_parallel_time <- microbenchmark(
  parallel = monte_carlo_parallel(n),
  times = 100  
)

# Print each execution time.
print(monte_carlo_time)
print(monte_carlo_parallel_time)

# Comment on difference: 
# Surprisingly the calculations are a bit faster for the 'normal' method and the mean time is therefor lower.
# mean normal: 1.67 seconds, mean parallel: 1.82 seconds. 
# However one should notice that the parallel seems to be a bit more stable due to the lower range of max-min (normal intervall: 4.486-0.981, parallel intervall: 3.007 - 1.605. 



# Task 31 ===========================================================================================================================================
#########################################################################################
# Exercise 31. (R Lecture 7) Make comparison of the speed of different implementation of Fibonacci code in R and
# varying also the number of generated elements of the Fibonacci sequence. 
# Summarize your results in a simple table and draw the conclusions.
#########################################################################################
library(microbenchmark)
library(Rcpp)
sourceCpp('Fibonacci.cpp')
source('Fibonacci.R')

res_benchmark_1 <- microbenchmark::microbenchmark(Fibonacci_native(5),
                               Fibonacci(5), 
                               times=250)
microbenchmark::microbenchmark(Fibonacci_native(5),
                               Fibonacci(5), 
                               times=250)

res_benchmark_2 <- microbenchmark::microbenchmark(Fibonacci_native(10),
                                                  Fibonacci(10), 
                                                  times=250)
microbenchmark::microbenchmark(Fibonacci_native(10),
                               Fibonacci(10), 
                               times=250)

res_benchmark_3 <- microbenchmark::microbenchmark(Fibonacci_native(20),
                                                  Fibonacci(20), 
                                                  times=250)
microbenchmark::microbenchmark(Fibonacci_native(20),
                               Fibonacci(20), 
                               times=250)


library(ggplot2)
ggplot2::autoplot(res_benchmark_1) + ggtitle('Distribution of Runtime of Native R vs. C++')
ggplot2::autoplot(res_benchmark_2) + ggtitle('Distribution of Runtime of Native R vs. C++')
ggplot2::autoplot(res_benchmark_3) + ggtitle('Distribution of Runtime of Native R vs. C++')


# We can see that the C++ performs the calculation a lot faster. As we can see in the plots it seems like the difference of the running times increases as we increase n (compare differences when 5,10,20). Notice the different measure of unit of the benchmarking output.