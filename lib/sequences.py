#!/usr/bin/env python3

def print_fibonacci(length):
    # Handle edge cases for length 0, 1, or 2
    if length <= 0:
        fibonacci_sequence = []
    elif length == 1:
        fibonacci_sequence = [0]
    else:
        # first two Fib numbers
        fibonacci_sequence = [0, 1]
        # for any length of nums
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
    
    print(fibonacci_sequence)
    return fibonacci_sequence

print(print_fibonacci(10)) # first 10 Fibonacci nums