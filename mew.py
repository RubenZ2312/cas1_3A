# Read the input number from the user
n = int(input())

# Check if n is a natural number (non-negative integer)
if n < 0:
    print("Please enter a non-negative natural number.")
else:
    # Loop through and print all natural numbers from 0 to n
    for i in range(n + 1):
        print(i)
