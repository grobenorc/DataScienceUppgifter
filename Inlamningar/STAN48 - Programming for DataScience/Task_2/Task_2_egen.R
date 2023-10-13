# Task 12 ---- 

sieve_of_eratosthenes <- function(n = 10^6) {
  is_prime <- rep(TRUE, n + 1)
  is_prime[1] <- FALSE
  i <- 2
  while (i^2 <= n) {
    if (is_prime[i]) {
      j <- i^2
      while (j <= n) {
        is_prime[j] <- FALSE
        j <- j + i
      }
    }
    i <- i + 1
  }
  primes <- (2:n)[is_prime[2:n]]
  return(primes)
}
print(head(sieve_of_eratosthenes(), 10)) # Example usage

# Task 13 ----
#Exercise 13. (R & Python) One of the challenging problems in matrix algebra 
#is computing an inverse of a matrix, i.e. for a given matrix finding 
#the matrix that when two are multiplied then yield the identity matrix. 
#Using the tools given in lectire notes, for a given list of 100 non-zero entries, 
#define the matrix that has the entries of this list on the diagonal 
#and zeros off the diagonal. Find the inverse of such a matrix 
#and verify that it is indeed the inverse by using the matrix product.  

create_diagonal_matrix <- function(non_zero_entries) {
  # Create a diagonal matrix with the given non-zero entries on the diagonal.
  diagonal_matrix <- matrix(0, nrow = length(non_zero_entries), ncol = length(non_zero_entries))
  for (i in 1:length(non_zero_entries)) {
    diagonal_matrix[i, i] <- non_zero_entries[i]
  }
  return(diagonal_matrix)
}

# Example usage:

non_zero_entries <- 1:100
diagonal_matrix <- create_diagonal_matrix(non_zero_entries)

inverse_diagonal_matrix <- function(diagonal_matrix) {
  # Compute the inverse of a diagonal matrix.
  inverse_matrix <- matrix(0, nrow = nrow(diagonal_matrix), ncol = ncol(diagonal_matrix))
  for (i in 1:nrow(diagonal_matrix)) {
    inverse_matrix[i, i] <- 1 / diagonal_matrix[i, i]
  }
  return(inverse_matrix)
}

# Example usage:

inverse_matrix <- inverse_diagonal_matrix(diagonal_matrix)

# Print the inverse matrix.
print(inverse_matrix)


# Task 14 ----
# Exercise 14. (R) Investigate the following instructions.

x <- c(1,2,3)
y <- c(4,5,6)
z <- c(7,8,9)
x*x%*%z*z
(x*x)%*%(z*z)
x%*%z*x%*%z
z%*%x*z%*%x
t(z)%*%t(x)*t(z)%*%t(x)
y%*%t(y)
t(y)%*%y
Y=array(y,c(1,3))
Y==t(y)
v%*%v
t(v)%*%v
v%*%t(v)
# Does the order in the matrix multiplication matter? Are the vector identical to matrices with one column (one row)?

# Comment:
# The order of matrix multiplication does matter for the provided instructions, and the results vary depending on the order of operands. 
# Additionally, vectors are not identical to matrices with one column (one row). Vectors in R are treated as one-dimensional 
# arrays, and their multiplication behavior differs from that of matrices.



# Task 15 ----
# Exercise 15. (R & Python) Create a simple telephone book with five entries using a dictionary in Python
# and names of elements in a vector/list in R. 
# An entry should be recognized by a name and yields a telephone number.
phone_book <- list(
  'Johan Andersson' = '0700000001',
  'Johan Pettersson' = '0700000002',
  'Johan Svensson' = '0700000003',
  'Karin Andersson' = '0700000004',
  'Karin Pettersson' = '0700000005'
)


# Task 16 ----
#Exercise 16. (R & Python) Enhance your telephone book by implementing it as a data frame. 
#Add "first name", "last name", "email"  fields. 

phone_book_enhanced <- list(
  'first name' = c('Johan', 'Johan', 'Johan', 'Karin', 'Karin'),
  'last name' = c('Andersson', 'Pettersson', 'Svensson', 'Andersson', 'Pettersson'),
  'email' = c('johan@andersson.com', 'johan@pettersson.com', 'johan@svensson.com', 'karin@andersson.com', 'karin@pettersson.com'),
  'phone number' = c('0700000001', '0700000002', '0700000003', '0700000004', '0700000005')
)
phone_book_enhanced_df <- as.data.frame(phone_book_enhanced)




# Task 17 ----
mute_array_in_place <- function(array) {
  # Generate random numbers for each element of the array.
  random_numbers <- sample(1:15, length(array), replace = TRUE)
  
  # Add the random numbers to the array.
  array <- array + random_numbers
  
  # Return the muted array.
  return(array)
}

# Example usage:

array <- c(1, 2, 3)

# Print the address of the array before muting it.
# print(address(array))
print(array)

# Mute the array.
muted_array <- mute_array_in_place(array)

# Print the address of the array after muting it.
# print(address(muted_array))
print(muted_array)


# Task 18 ----
#Exercise 18. (R & Python) Implement all standard arithmetic operations (subtraction, multiplication, and division) within the class of complex numbers.
ComplexNumber <- setRefClass("ComplexNumber",
                             fields = list(real = "numeric",
                                           imaginary = "numeric"),
                             methods = list(
                               initialize = function(real, imaginary) {
                                 self$real <- real
                                 self$imaginary <- imaginary
                               },
                               add = function(other) {
                                 real_result <- self$real + other$real
                                 imag_result <- self$imaginary + other$imaginary
                                 return(ComplexNumber$new(real_result, imag_result))
                               },
                               subtract = function(other) {
                                 real_result <- self$real - other$real
                                 imag_result <- self$imaginary - other$imaginary
                                 return(ComplexNumber$new(real_result, imag_result))
                               },
                               multiply = function(other) {
                                 real_result <- self$real * other$real - self$imaginary * other$imaginary
                                 imag_result <- self$real * other$imaginary + self$imaginary * other$real
                                 return(ComplexNumber$new(real_result, imag_result))
                               },
                               divide = function(other) {
                                 denominator <- other$real^2 + other$imaginary^2
                                 real_result <- (self$real * other$real + self$imaginary * other$imaginary) / denominator
                                 imag_result <- (self$imaginary * other$real - self$real * other$imaginary) / denominator
                                 return(ComplexNumber$new(real_result, imag_result))
                               }
                             )
)




