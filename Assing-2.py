# Use the Python loops to print number-increasing 
# reverse pyramid pattern.

# Define the starting number of elements in the top row
n = 6

# Loop through the rows in reverse order
for i in range(n, 0, -1):
    # Print numbers from 1 to the current row number
    for j in range(1, i + 1):
        print(j, end=' ')
    # Print a newline after each row
    print()