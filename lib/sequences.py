#!/usr/bin/env python3

def print_fibonacci(length):
    # Handle edge cases for length 0, or 1
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


def print_fibonacci2(length):
    if length <= 0:
        fib_sequence = []
    elif length == 1:
        fib_sequence = [0]
    else:
        fib_sequence = [0, 1]
        for _ in range(length-2): 
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
    print(fib_sequence)
    return fib_sequence
print(print_fibonacci2(3))