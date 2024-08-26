# Function to check if a number is prime
def is_prime(n):
    # Check if the number is less than or equal to 1
    if n <= 1:
        return False
    # Check for factors from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    # If no factors found, the number is prime
    return True

# Loop through numbers from 1 to 100
for number in range(1, 101):
    if is_prime(number):
        print(number)