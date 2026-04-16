# Get the position from the user and convert to integer
n = int(input("Enter the position (1st, 2nd, 3rd, etc.) in Fibonacci: "))

# Define a recursive function that returns the nth Fibonacci number
def fibonacci_recursive(x):
    # Base case 1: if position is 1, Fibonacci number is 0
    if x == 1:
        return 0
    # Base case 2: if position is 2, Fibonacci number is 1
    elif x == 2:
        return 1
    # Recursive case: Fib(x) = Fib(x-1) + Fib(x-2)
    else:
        return fibonacci_recursive(x - 1) + fibonacci_recursive(x - 2)

# Call the function with the user's position and store the result
result = fibonacci_recursive(n)

# Print the result in a readable format
print(f"The Fibonacci number at position {n} is {result}")