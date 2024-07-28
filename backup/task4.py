#Task 4: Move lines 2-14 into a function named fib_sum
fib_1 = 0
fib_2 = 1

# List to store Fibonacci numbers
fibonacci_sequence = [fib_1, fib_2]

# Generate Fibonacci sequence up to the 10th digit
for i in range(2, 10):
    next_fib = fib_1 + fib_2
    fibonacci_sequence.append(next_fib)
    fib_1 = fib_2
    fib_2 = next_fib
return sum(fibonacci_sequence)


# Calculate the sum of the Fibonacci sequence
sum_fibonacci = fib_sum()