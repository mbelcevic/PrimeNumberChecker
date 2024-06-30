def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input
user_input = input("Enter a number: ")

try:
    num = int(user_input)
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
