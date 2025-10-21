# Name: Alexander Ramirez
# Course number: CIS261 Week 2
# Assignment Title: Iterative and Recursive Functionality Lab document
# Date: 10/21/25

# This program calculates the factorial of a number using both
# iterative and recursive methods.

# --- Part 1: Iterative Factorial Function ---

# This program calculates the factorial of a number using both
# iterative and recursive methods.

# --- Part 1: Iterative Factorial Function ---

def calculate_factorial_iterative(n):
    """
    Calculates the factorial of a non-negative integer 'n' using a for loop (iterative method).
    
    Args:
        n (int): The number for which to calculate the factorial.
        
    Returns:
        int/str: The calculated factorial or an error message if n is negative.
    """
    # Factorial is only defined for non-negative integers
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    # Base case: Factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    
    result = 1
    
    # Use a for loop to multiply numbers from 2 up to n
    for i in range(2, n + 1):
        result *= i
        
    return result

# --- Part 2: Recursive Factorial Function ---

def calculate_factorial_recursive(n):
    """
    Calculates the factorial of a non-negative integer 'n' using recursion.
    
    Args:
        n (int): The number for which to calculate the factorial.
        
    Returns:
        int/str: The calculated factorial or an error message if n is negative.
    """
    # Handle negative input
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    # Base case: Stops the recursion
    if n == 0 or n == 1:
        return 1
    
    # Recursive step: n * factorial(n - 1)
    return n * calculate_factorial_recursive(n - 1)

# --- Part 3: Execution and Output ---

def main():
    """
    Calls both factorial functions five times with specific numbers and prints the results.
    """
    test_numbers = [0, 1, 5, 7, 10]
    
    print("-" * 60)
    print("Factorial Calculation using Iterative and Recursive Functions")
    print("-" * 60)

    # Display Iterative Results
    print("\n--- Iterative Factorial Results ---")
    for num in test_numbers:
        result = calculate_factorial_iterative(num)
        print(f"Factorial of {num} (Iterative): {result}")

    # Display Recursive Results
    print("\n--- Recursive Factorial Results ---")
    for num in test_numbers:
        result = calculate_factorial_recursive(num)
        print(f"Factorial of {num} (Recursive): {result}")
    
    print("-" * 60)

if __name__ == "__main__":
    main()
