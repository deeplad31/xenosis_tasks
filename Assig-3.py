# Hollow Diamond Pyramid 

def print_hollow_diamond(n):
    if n < 1:
        print("Size should be greater than 0")
        return
    
    # Print the upper half of the diamond
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
                    
    # Print the lower half of the diamond
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Size of the diaond
# size = 6

# Get the size of the diamond from the user
size = int(input("Enter the size of the diamond: "))
print_hollow_diamond(size)