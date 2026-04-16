# Get a number from the user and convert it to an integer
n = int(input("Enter a whole number to find its factorial: "))

# Define a recursive function that calculates factorial
def factorial_recursive(x):
    # Base case: if x is 0 or 1, factorial is 1 (stop recursion)
    if x == 0 or x == 1:
        return 1
    # Recursive case: x! = x * (x-1)!
    else:
        return x * factorial_recursive(x - 1)

# Call the function with the user's number and store the result
result = factorial_recursive(n)

# Print the result in a readable format
print(f"The factorial of {n} is {result}")

