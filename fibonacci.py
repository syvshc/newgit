#!/usr/bin/env python3
"""
Fibonacci Sequence Implementation
This script provides multiple ways to generate and work with Fibonacci numbers.
"""


def fibonacci_iterative(n):
    """
    Generate first n Fibonacci numbers using iterative approach.

    Args:
        n (int): Number of Fibonacci numbers to generate

    Returns:
        list: List of first n Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence


def fibonacci_generator(n):
    """
    Generator function for Fibonacci sequence.

    Args:
        n (int): Number of Fibonacci numbers to generate

    Yields:
        int: Next Fibonacci number
    """
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def fibonacci_recursive(n):
    """
    Calculate nth Fibonacci number using recursion (not efficient for large n).

    Args:
        n (int): Position in Fibonacci sequence (0-indexed)

    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoization(n, memo=None):
    """
    Calculate nth Fibonacci number using memoization for efficiency.

    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        memo (dict): Dictionary to store computed values

    Returns:
        int: The nth Fibonacci number
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def main():
    """Main function to demonstrate different Fibonacci implementations."""
    print("=" * 50)
    print("Fibonacci Sequence Demonstrations")
    print("=" * 50)

    # Iterative approach
    n = 15
    print(f"\n1. First {n} Fibonacci numbers (iterative):")
    print(fibonacci_iterative(n))

    # Generator approach
    print(f"\n2. First {n} Fibonacci numbers (generator):")
    print(list(fibonacci_generator(n)))

    # Recursive approach (for small numbers)
    print(f"\n3. 10th Fibonacci number (recursive):")
    print(fibonacci_recursive(10))

    # Memoization approach
    print(f"\n4. 20th Fibonacci number (memoization):")
    print(fibonacci_memoization(20))

    # Display as a formatted table
    print(f"\n5. Fibonacci sequence table:")
    print("-" * 30)
    print(f"{'n':>5} | {'Fibonacci(n)':>15}")
    print("-" * 30)
    for i in range(min(n, 20)):
        print(f"{i:>5} | {fibonacci_memoization(i):>15}")
    print("-" * 30)


if __name__ == "__main__":
    main()
